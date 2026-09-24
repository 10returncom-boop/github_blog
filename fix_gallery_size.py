filepath = r"D:\www\325-public\index.html"

with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

# 去掉第一張圖片的 tall class，讓所有圖片統一大小
content = content.replace('<div class="gallery-item tall">', '<div class="gallery-item">')

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(content)

print("Done: all gallery images now uniform size.")
