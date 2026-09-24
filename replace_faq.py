import re

filepath = r"D:\www\325-public\index.html"

with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

# 找到附錄B卡片的開頭和結尾
old_start = '<!-- ===== 附錄B：延伸閱讀 ===== -->'
old_end_marker = '</article>\n\n</main>'

# 定位舊卡片
start_idx = content.find(old_start)
if start_idx == -1:
    print("ERROR: Could not find appendix B start")
    exit(1)

# 找到這個 article 的結尾
end_search = content.find(old_end_marker, start_idx)
if end_search == -1:
    print("ERROR: Could not find appendix B end")
    exit(1)

end_idx = end_search + len('</article>')

# 新的 FAQ 卡片 HTML
faq_html = '''<!-- ===== 附錄B：FAQ 常見問題 ===== -->
<article class="chapter-card reveal" id="reading">
  <div class="chapter-hero">
    <span class="chapter-number">FAQ</span>
    <img src="assets/appendix-blueprint.jpg" alt="常見問題解答">
    <div class="chapter-overlay">
      <h2 class="chapter-title">常見問題</h2>
      <p class="chapter-subtitle">關於 OKU 與這次參訪，你可能想知道</p>
    </div>
  </div>
  <div class="chapter-body">
    <p class="chapter-excerpt">
      整理大家最常問的問題，從酒店基本資訊到參訪注意事項，一次說清楚。
    </p>
    <div class="chapter-tags">
      <span class="tag">活動資訊</span>
      <span class="tag">交通方式</span>
      <span class="tag">酒店特色</span>
    </div>
    <button class="chapter-expand-btn" onclick="toggleCard('reading')">
      展開常見問題
      <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
        <polyline points="6 9 12 15 18 9"/>
      </svg>
    </button>
    <div class="chapter-full-content">
      <div class="chapter-full-inner">
        <h3>Q1：OKU 歐酷酒店是什麼時候開幕的？</h3>
        <p>
          OKU 於 2025 年 10 月正式開幕，位於台中市中區成功路 357 號，前身為老牌的櫻田百貨。由國際頂級酒店設計團隊 HBA Studio 操刀改造，是一棟由老百貨重生的 Art Deco 精品酒店。
        </p>

        <h3>Q2：這次參訪活動是免費的嗎？</h3>
        <p>
          活動每人新台幣 1,200 元，費用已包含晚餐 Buffet。其餘場地、分享會、酒款等費用皆由郭宜書董事長贊助。當天報到時以現金支付即可。
        </p>

        <h3>Q3：沒有開車，要怎麼到達 OKU？</h3>
        <p>
          OKU 位於台中中區，距離台中火車站步行約 10 分鐘。可搭火車到台中火車站，再沿中華路、成功路步行抵達。活動現場也備有美酒，強烈建議不要開車前來。
        </p>

        <h3>Q4：如果開車，停車場在哪裡？</h3>
        <p>
          推薦停放於第二市場（興中）停車場，停好車後沿大誠街、成功路步行即可抵達酒店，步行時間約 5 分鐘。
        </p>

        <h3>Q5：OKU 最具代表性的地標是什麼？</h3>
        <p>
          大廳中央那座三層樓高的巨型酒塔。金色黃銅框架，垂直貫穿三層樓，是踏入酒店第一眼的視覺焦點，也是 OKU 的精神象徵。
        </p>

        <h3>Q6：誰是 OKU 的創辦人？</h3>
        <p>
          郭宜書董事長，大家都稱他「郭哥」。他不計成本投入這項老建築再生計畫，希望為台中舊城留下一件傳世的建築作品，而非只是一間追求獲利的飯店。
        </p>

        <h3>Q7：OKU 獲得過什麼國際獎項？</h3>
        <p>
          OKU 已獲得米其林指南推薦酒店認證，館內的艾莉蕬酒吧也入圍 2026 全球餐廳與酒吧設計大獎，是台灣少數同時在建築室內與餐飲酒吧兩大領域都獲得國際肯定的精品酒店。
        </p>

        <h3>Q8：這次參訪活動的行程是什麼？</h3>
        <table class="info-table">
          <tr><th>15:30</th><td>報到入場</td></tr>
          <tr><th>16:00–17:00</th><td>歐酷酒店分享會</td></tr>
          <tr><th>17:00–18:00</th><td>共學分享與交流討論</td></tr>
          <tr><th>18:00–20:30</th><td>Lumen 餐廳 Buffet 晚餐</td></tr>
        </table>
      </div>
    </div>
  </div>
</article>'''

# 替換舊內容
new_content = content[:start_idx] + faq_html + content[end_idx:]

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(new_content)

print("Done! Appendix B replaced with FAQ section.")
