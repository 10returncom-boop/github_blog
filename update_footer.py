filepath = r"D:\www\325-public\index.html"

with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

old_footer = '''<footer class="footer">
  <div class="footer-title">OKU舊城風華</div>
  <p class="footer-text">
    本書記錄 2026 年 9 月 27 日台中歐酷酒店 OKU 共學參訪活動。<br>
    建築是凝固的城市記憶，每一面磚牆都在訴說舊城的故事。
  </p>
</footer>'''

new_footer = '''<footer class="footer">
  <div class="footer-title">OKU舊城風華</div>
  <p class="footer-text">
    記錄東海EMBA於 2026 年 9 月 27 日台中歐酷酒店 OKU 共學參訪活動。<br>
    建築是凝固的城市記憶，每一面磚牆都在訴說舊城的故事。
  </p>
  <p class="footer-text" style="margin-top: 1.5rem; padding-top: 1.5rem; border-top: 1px solid var(--border);">
    規劃設計開發：張書欣<br>
    TEL：0968-222201　LINE：331.today
  </p>
</footer>'''

content = content.replace(old_footer, new_footer)

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(content)

print("Footer updated.")
