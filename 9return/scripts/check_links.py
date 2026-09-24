# -*- coding: utf-8 -*-
"""
check_links.py — 檢查所有HTML中的內部連結是否有效
用法: python check_links.py [--root 站點根目錄]
"""
import os, re, argparse

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--root', default=os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    args = ap.parse_args()
    html_files = []
    for root, dirs, files in os.walk(args.root):
        if '.git' in root or 'scripts' in root: continue
        for f in files:
            if f.endswith('.html'):
                html_files.append(os.path.join(root, f))
    broken = 0
    checked = 0
    for fp in html_files:
        with open(fp, 'r', encoding='utf-8') as f: content = f.read()
        hrefs = re.findall(r'href=["\']([^"\']+)["\']', content)
        for href in hrefs:
            if href.startswith(('http','#','mailto:','tel:','javascript:','${')): continue
            href = href.split('#')[0]
            if not href: continue
            target = os.path.normpath(os.path.join(os.path.dirname(fp), href))
            if not os.path.exists(target):
                rel = fp.replace(args.root,'')
                print(f'  BROKEN: {rel} -> {href}')
                broken += 1
            checked += 1
    print(f'Checked {checked} links, {broken} broken')

if __name__ == '__main__':
    main()
