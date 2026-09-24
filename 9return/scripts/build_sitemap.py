# -*- coding: utf-8 -*-
"""
build_sitemap.py — 掃描所有HTML並生成sitemap.xml + robots.txt
用法: python build_sitemap.py [--base https://9return.com.tw]
"""
import os, argparse
from datetime import datetime

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--base', default='https://9return.com.tw')
    ap.add_argument('--root', default=os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    args = ap.parse_args()
    urls = []
    for root, dirs, files in os.walk(args.root):
        if any(d in root for d in ['.git','scripts','assets','node_modules']): continue
        for f in files:
            if f.endswith('.html'):
                rel = os.path.relpath(os.path.join(root,f), args.root).replace('\\','/')
                urls.append(f'{args.base}/{rel}')
    urls.sort()
    sm = '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
    for u in urls:
        sm += f'  <url><loc>{u}</loc><changefreq>weekly</changefreq><priority>0.8</priority></url>\n'
    sm += '</urlset>\n'
    with open(os.path.join(args.root,'sitemap.xml'),'w',encoding='utf-8') as f: f.write(sm)
    with open(os.path.join(args.root,'robots.txt'),'w',encoding='utf-8') as f:
        f.write(f'User-agent: *\nAllow: /\nSitemap: {args.base}/sitemap.xml\n')
    print(f'sitemap.xml: {len(urls)} URLs')

if __name__ == '__main__':
    main()
