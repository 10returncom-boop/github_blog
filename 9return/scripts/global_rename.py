# -*- coding: utf-8 -*-
"""
global_rename.py — 全域取代HTML中的舊站名
用法: python global_rename.py --old "舊名" --new "新名" [--root 站點根目錄]
"""
import os, argparse

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--old', required=True)
    ap.add_argument('--new', required=True)
    ap.add_argument('--root', default=os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    args = ap.parse_args()
    total = 0
    for root, dirs, files in os.walk(args.root):
        if '.git' in root: continue
        for f in files:
            if f.endswith('.html'):
                fp = os.path.join(root, f)
                with open(fp, 'r', encoding='utf-8') as fh: content = fh.read()
                c = content.count(args.old)
                if c:
                    content = content.replace(args.old, args.new)
                    with open(fp, 'w', encoding='utf-8') as fh: fh.write(content)
                    rel = fp.replace(args.root,'')
                    print(f'  {rel}: {c}x')
                    total += c
    print(f'Total: {total} replacements')

if __name__ == '__main__':
    main()
