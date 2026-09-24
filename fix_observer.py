filepath = r"D:\www\325-public\index.html"

with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

# 修正：讓 observer 觀察所有 .reveal 元素，不只 .chapter-card
old_js = '''document.querySelectorAll('.chapter-card').forEach(el => {
  observer.observe(el);
});'''

new_js = '''document.querySelectorAll('.reveal').forEach(el => {
  observer.observe(el);
});'''

content = content.replace(old_js, new_js)

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(content)

print("Fixed: observer now watches all .reveal elements including galleries.")
