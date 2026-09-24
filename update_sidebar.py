filepath = r"D:\www\325-public\index.html"

with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

content = content.replace('附錄B 延伸閱讀', 'FAQ 常見問題')

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(content)

print("Sidebar updated.")
