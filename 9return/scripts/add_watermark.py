# -*- coding: utf-8 -*-
"""
add_watermark.py — 批次為圖片加上左下角浮水印
用法: python add_watermark.py <圖片目錄> [--text 欣媒體] [--font-size 13] [--skip icons]
"""
import os, argparse
from PIL import Image, ImageDraw, ImageFont

FONTS = [r'C:\Windows\Fonts\msjhbd.ttc', r'C:\Windows\Fonts\msjh.ttc', r'C:\Windows\Fonts\mingliu.ttc']

def get_font(size):
    for fp in FONTS:
        if os.path.exists(fp):
            return ImageFont.truetype(fp, size)
    return ImageFont.load_default()

def add_watermark(img_path, text='欣媒體', font_size=13, padding=8):
    img = Image.open(img_path).convert('RGBA')
    layer = Image.new('RGBA', img.size, (0,0,0,0))
    draw = ImageDraw.Draw(layer)
    font = get_font(font_size)
    bbox = draw.textbbox((0,0), text, font=font)
    tw, th = bbox[2]-bbox[0], bbox[3]-bbox[1]
    x, y = padding, img.size[1] - th - padding - 2
    for dx,dy in [(-1,0),(1,0),(0,-1),(0,1),(-1,-1),(1,-1),(-1,1),(1,1)]:
        draw.text((x+dx,y+dy), text, font=font, fill=(0,0,0,180))
    draw.text((x,y), text, font=font, fill=(255,255,255,220))
    result = Image.alpha_composite(img, layer).convert('RGB')
    ext = os.path.splitext(img_path)[1].lower()
    if ext == '.webp': result.save(img_path, 'WEBP', quality=85)
    elif ext in ('.jpg','.jpeg'): result.save(img_path, 'JPEG', quality=90)
    elif ext == '.png': result.save(img_path, 'PNG')

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('directory')
    ap.add_argument('--text', default='欣媒體')
    ap.add_argument('--font-size', type=int, default=13)
    ap.add_argument('--skip', nargs='*', default=['icons'])
    args = ap.parse_args()
    count = 0
    for root, dirs, files in os.walk(args.directory):
        if any(s in root for s in args.skip): continue
        for f in files:
            if f.lower().endswith(('.webp','.jpg','.jpeg','.png')):
                fp = os.path.join(root, f)
                fs = args.font_size - 4 if 'thumbs' in root else args.font_size
                add_watermark(fp, args.text, max(fs,7))
                count += 1
    print(f'Done: {count} images watermarked')

if __name__ == '__main__':
    main()
