filepath = r"D:\www\325-public\index.html"

with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

# 替換側邊欄標題
content = content.replace('<div class="sidebar-title">本書目錄</div>', '<div class="sidebar-title">探索這趟旅程</div>')

# 替換側邊欄導覽項目
old_nav = '''<ul class="sidebar-nav" id="sidebarNav">
    <li><a onclick="scrollToChapter('ch1')">第一章 活動邀約</a></li>
    <li><a onclick="scrollToChapter('ch2')">第二章 建築重生</a></li>
    <li><a onclick="scrollToChapter('ch3')">第三章 空間美學</a></li>
    <li><a onclick="scrollToChapter('ch4')">第四章 在地脈絡</a></li>
    <li><a onclick="scrollToChapter('ch5')">第五章 參訪手記</a></li>
    <li><a onclick="scrollToChapter('ch6')">第六章 後記</a></li>
    <li><a onclick="scrollToChapter('appendix')">附錄A 專業名詞</a></li>
    <li><a onclick="scrollToChapter('reading')">FAQ 常見問題</a></li>
  </ul>'''

new_nav = '''<ul class="sidebar-nav" id="sidebarNav">
    <li><a onclick="scrollToChapter('ch1')">赴一場舊城盛宴</a></li>
    <li><a onclick="scrollToChapter('ch2')">從櫻田百貨到 Art Deco</a></li>
    <li><a onclick="scrollToChapter('ch3')">走進三層酒塔</a></li>
    <li><a onclick="scrollToChapter('ch4')">舊城的靈魂脈絡</a></li>
    <li><a onclick="scrollToChapter('ch5')">沙龍共學之夜</a></li>
    <li><a onclick="scrollToChapter('ch6')">凝固的城市記憶</a></li>
    <li><a onclick="scrollToChapter('appendix')">關鍵詞小辭典</a></li>
    <li><a onclick="scrollToChapter('reading')">你可能想知道</a></li>
  </ul>'''

content = content.replace(old_nav, new_nav)

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(content)

print("Sidebar updated with engaging labels.")
