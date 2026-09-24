# 欣矩陣 ∞ 欣媒體 — 9return.com.tw

> 旗下 30 大網站入口，沒有做不到，只有想不到。跨產業垂直站點全面佈局。

## 網站架構

```
9return.com.tw/
├── index.html              # 門戶首頁（17張卡片 bento grid）
├── dashboard.html          # 九回房地觀測站
├── sitemap.xml             # SEO站點地圖（27 URL）
├── robots.txt              # 爬蟲規則
├── README.md               # 本說明書
├── assets/                 # 靜態資源
│   ├── card-01~17.webp     # 卡片背景圖（1024×1024 webp）
│   ├── og/                 # OG分享圖
│   └── brand-banners/      # 品牌橫幅
├── counties/               # 8縣市不動產頁
├── jinyong-psychology/     # 金庸人物與心理學
│   ├── index.html          # 100人物圖譜+QUIZ
│   └── about.html          # 設計者張書欣
├── hongloumeng/            # 夢見紅樓夢的家
│   ├── index.html
│   └── about.html
├── classic-architecture/   # 古代建築還原記
│   ├── index.html
│   ├── arch-01~10.html     # 10大建築頁
│   ├── about.html
│   └── sitemap.html
└── scripts/                # Python維護腳本
```

## 卡片清單（17張）

| # | 卡片名稱 | 狀態 | 連結 |
|---|---------|------|------|
| 1 | 金庸人物與心理學 | 上線 | ./jinyong-psychology/ |
| 2 | 三三藝 331 Gallery | 上線 | # |
| 3 | ZooTecture 入梯 | 上線 | # |
| 4 | Petlogic毛毛邏輯 | 上線 | # |
| 5 | 夢見紅樓夢的家 | 上線 | ./hongloumeng/ |
| 6 | 古代建築還原記 | 上線 | ./classic-architecture/ |
| 7 | 順寵毛小孩 | 上線 | # |
| 8 | 安寵好好學 | 上線 | # |
| 9 | 寵物空間好好裝 | 上線 | # |
| 10 | 九回房地觀測站 | 上線 | ./dashboard.html |
| 11 | 虛擬試衣間 | 即將上線 | ./index.html |
| 12 | 經濟學的小遊戲 | 即將上線 | ./index.html |
| 13 | 星象命盤占星 | 即將上線 | ./index.html |
| 14 | 三國演義 vs 賽局 | 即將上線 | ./index.html |
| 15 | 以物易物好好玩 | 即將上線 | ./index.html |
| 16 | Infucoco愛幻想 | 即將上線 | ./index.html |
| 17 | 音樂家都很怪 | 即將上線 | ./index.html |

## 全域樣式變數

| 變數 | 值 | 說明 |
|------|-----|------|
| Header/Footer 背景 | #0a0a0a | 黑底 |
| Header/Footer 文字 | #e2e8f0 | 白字 |
| Hover 底線 | #ef4444 2px | 紅色底線 |
| 卡片標題字型 | 28px | 全部卡片統一（含大卡） |
| 卡片描述字型 | 14px | 全部卡片統一 |
| 即將上線標籤 | #fbbf24 | 黃色 |
| OG圖 | 1200×630 webp | og-brand-main.webp |
| 卡片圖 | 1024×1024 webp q=85 | 絕對無文字 |

## 設計者資訊

- **設計者**：張書欣
- **關於頁**：https://9return.com.tw/jinyong-psychology/about.html
- **Email**：zootecture@gmail.com
- **Line**：331.today
- **電話**：0968222201
- **服務**：網站規劃 / 設計 / 開發 / 網路行銷與策略聯盟

## 維護說明

### 新增卡片
1. 在 `index.html` 的 bento grid 中新增 `<a class="card card-N">` 區塊
2. 卡片圖放入 `assets/card-NN-name.webp`（1024×1024，無文字）
3. 更新 `網站導覽_SITES.json` 和變數表
4. 更新 `sitemap.xml`

### 變更卡片順序
1. 調整 `index.html` 中卡片區塊順序
2. 重新編號 `card-N` class 和 `card-num`
3. 重新命名對應圖檔
4. 執行 `scripts/reorder_cards.py` 輔助

### 卡片圖片規範
- **絕對不可含任何文字、字母、數字、商標、印章、書法**
- 統一 1024×1024 WebP quality=85
- 生成後需目視檢查隱藏文字（書本封面、黑板、招牌、物品標籤）

### 浮水印
- 文字：欣媒體
- 位置：左下角
- 字型：微軟正黑體 10pt
- 執行：`scripts/add_watermark.py <目錄>`

## 文件清單

- `統一導航系統_規格書.docx` — 完整規格（v2.3）
- `網站導覽_變數調整表.xlsx` — 變數/卡片/圖片/文件清單
- `網站導覽_SITES.json` — 結構化卡片資料
- `sitemap.xml` — SEO站點地圖

---

*版本 v2.3 | 2026-09-03 | 張書欣*
