# 欣媒體 MyMatrix — 網站規格書與變數區

> 版本：v1.0 | 更新日期：2026-08-30
> 網址：https://9return.com.tw/
> 設計規劃開發：張書欣

---

## 一、網站概覽

| 項目 | 說明 |
|------|------|
| 網站名稱 | 【欣媒體】MyMatrix |
| 頁面標題 | 【欣媒體】沒有做不到，只有想不到 |
| 語言 | 繁體中文（zh-Hant） |
| 架構 | 單頁式（Single Page）+ 內頁連結 |
| 部署 | GitHub Pages |
| 主要頁面 | index.html（首頁）、dashboard.html（不動產觀測站） |

---

## 二、檔案結構

```
9return.com.tw/
├── index.html              # 首頁（含內嵌 CSS/JS）
├── dashboard.html          # 不動產觀測站內頁
├── SPEC.md                 # 本規格書
├── README.md               # 專案說明
└── assets/                 # 圖片資源
    ├── favicon.png         # 網站圖標
    ├── og-image-new.png    # FB/Line 分享預覽圖
    ├── bg-main.webp        # 全站背景底圖
    ├── hero-bg.jpg         # Hero 區背景圖
    ├── card-01-gallery.jpg     # 卡片01：三三藝
    ├── card-02-zootecture.jpg  # 卡片02：入梯毛孩
    ├── card-03-petlogic.jpg     # 卡片03：毛毛邏輯
    ├── card-04-pets.jpg         # 卡片04：順寵圖鑑
    ├── card-05-education.jpg    # 卡片05：安寵好好學
    ├── card-06-realestate.jpg   # 卡片06：不動產觀測站
    └── 331yi-01~10-*.jpg       # 三三藝 10 張 1:1 藝術圖
```

---

## 三、CSS 變數區（`:root`）

### 3.1 顏色變數

| 變數名稱 | 色碼 | 用途 |
|----------|------|------|
| `--bg` | `#08080A` | 全站背景主色（近黑） |
| `--bg-2` | `#0E0E12` | 背景次色 |
| `--white` | `#F2F0EB` | 主文字白色（暖白） |
| `--white-dim` | `rgba(242,240,235,0.6)` | 次要文字（60% 透明度） |
| `--white-faint` | `rgba(242,240,235,0.25)` | 最弱文字/分隔線（25%） |
| `--accent` | `#E8C84B` | 黃色（強調色 1） |
| `--accent-2` | `#FF6B35` | 橘色（強調色 2） |
| `--accent-3` | `#4ECDC4` | 青色（強調色 3，用於光暈） |

### 3.2 字型變數

| 變數名稱 | 字型堆疊 | 用途 |
|----------|----------|------|
| `--font-display` | `'Playfair Display', 'Noto Sans TC', Georgia, serif` | 標題字型（襯線） |
| `--font-sans` | `'Space Grotesk', 'Noto Sans TC', sans-serif` | 內文字型（無襯線） |
| `--font-tc` | `'Noto Sans TC', 'Space Grotesk', sans-serif` | 中文內文 |

### 3.3 動畫緩動變數

| 變數名稱 | 值 | 用途 |
|----------|-----|------|
| `--ease` | `cubic-bezier(0.16, 1, 0.3, 1)` | 主要緩動（進入） |
| `--ease-out` | `cubic-bezier(0.22, 1, 0.36, 1)` | 出場緩動 |

---

## 四、文字內容變數區

### 4.1 SEO / 社群分享

| 項目 | 目前值 | 位置 |
|------|--------|------|
| 頁面標題 `<title>` | 【欣媒體】沒有做不到，只有想不到 | `<head>` |
| OG 標題 | 【欣媒體】欣的媒體矩陣 MyMatrix | `<meta property="og:title">` |
| OG 描述 | 欣媒體旗下6大網站入口——三三藝 331 Gallery、ZooTecture入梯毛孩、Petlogic毛毛邏輯、不動產觀測站、順寵圖鑑、安寵好好學等 | `<meta property="og:description">` |
| OG 圖片 | `assets/og-image-new.png` | `<meta property="og:image">` |
| OG 網址 | `https://9return.com.tw/` | `<meta property="og:url">` |
| 網站名稱 | 【欣媒體】MyMatrix | `<meta property="og:site_name">` |
| Twitter 標題 | 【欣媒體】MyMatrix 沒有做不到，只有想不到 | `<meta name="twitter:title">` |
| Twitter 圖片 | `assets/og-image-new.png` | `<meta name="twitter:image">` |
| Favicon | `assets/favicon.png` | `<link rel="icon">` |
| 主題色 | `#08080A` | `<meta name="theme-color">` |

### 4.2 Header 導覽列

| 元素 | 目前值 |
|------|--------|
| 品牌名 | 欣媒體 |
| 品牌標語 | 沒有做不到，只有想不到 |
| 黃點尺寸 | `8px`（含脈動動畫 3s） |
| 回首頁文字 | 回首頁 |
| 分隔符 | ｜ |
| 電話號碼 | 0968-222201 |
| Nav padding | `18px 40px` |
| Nav 背景 | `rgba(8,8,10,0.45)` + `blur(20px)` |
| 品牌字級 | `13px` / 粗體 600 |

### 4.3 Hero 主標題

| 元素 | 目前值 | 樣式 |
|------|--------|------|
| 第一行 | xMedia | 白色，`clamp(52px, 9vw, 130px)` |
| 第二行 | 欣媒體 | 深黃色描邊 `#DAA520`，1.5px，透明填色 |
| 兩行間距 | `0.5em` | — |
| 標題行高 | `1.0` | — |
| 標題字距 | `0.02em` | — |
| Hero 頂部 padding | `28px` | — |
| Hero 背景圖 | `https://aka.doubaocdn.com/s/2UNMAy1OAh` | 含暗色漸層遮罩 |
| 敘述文字 | 【欣媒體】旗下六大網站入口——從藝品藝廊到毛孩生活，從房地資訊到寵物知識，每一個連結都是一個獨立的內容世界，卻又是一個矩陣的世界... | 白色 `16px`，最大寬 640px，置中 |
| 敘述與標題間距 | `36px` | — |
| 標題上升動畫 | `1s`，延遲 `0.3s` / `0.45s` | — |
| 對齊方式 | 置中（`text-align: center`） | — |

### 4.4 跑馬燈

| 參數 | 目前值 |
|------|--------|
| 滾動速度 | `18s` 循環（線性） |
| 字級 | `24px` |
| 字重 | `700`（粗體） |
| 顏色 | 深黃色 `#DAA520` |
| hover 顏色 | 白色 `#F2F0EB` |
| 項目間距 | `48px` |
| 圓點大小 | `10px`（深黃色） |
| 頂部 padding | `50px`（閃過固定 nav） |
| 底部 padding | `6px` |

#### 跑馬燈 6 站內容（重複 2 次循環）

| # | 文字 | 連結 |
|---|------|------|
| 1 | 三三藝 331 Gallery | `https://331.today` |
| 2 | ZooTecture入梯毛孩 | `https://zootecture.com` |
| 3 | Petlogic毛毛邏輯 | `https://petlogic.org` |
| 4 | Vocus 順寵圖鑑 | `https://vocus.cc/salon/zootecture` |
| 5 | Vocus 安寵好好學 | `https://vocus.cc/salon/petlogic` |
| 6 | 不動產觀測站 | `./dashboard.html` |

### 4.5 六張卡片（Bento Grid）

| 全域參數 | 目前值 |
|----------|--------|
| 格子欄數 | `4 欄` |
| 格子高度 | `260px` |
| 卡片間距 | `48px` |
| 區塊 padding | `56px 40px 72px` |
| 文字對齊 | 置中（`text-align: center`） |
| 分類標籤字級 | `11px` |
| 卡片名稱字級 | `28px`（預設） |
| 描述字級 | `16px` |
| 網址字級 | `16px` |

#### 卡片個別設定

| # | 卡片名稱 | 分類 | 網域/副標 | 圖片路徑 | 連結 | 格子跨度 | 名稱字級 |
|---|----------|------|-----------|----------|------|----------|----------|
| 01 | 三三藝 331 Gallery | Art Gallery | 331.today | `assets/card-01-gallery.jpg` | `https://331.today` | 2欄×2列 | `36px` |
| 02 | ZooTecture 入梯毛孩 | Pet Architecture | zootecture.com | `assets/card-02-zootecture.jpg` | `https://zootecture.com` | 1欄×1列 | `28px` |
| 03 | Petlogic 毛毛邏輯 | Pet Lifestyle | petlogic.org | `assets/card-03-petlogic.jpg` | `https://petlogic.org` | 1欄×1列 | `28px` |
| 04 | Vocus 順寵圖鑑 | Pet Encyclopedia | Pets Salon | `assets/card-04-pets.jpg` | `https://vocus.cc/salon/zootecture` | 1欄×1列 | `28px` |
| 05 | Vocus 安寵好好學 | Pet Education | Petlogic Salon | `assets/card-05-education.jpg` | `https://vocus.cc/salon/petlogic` | 1欄×1列 | `28px` |
| 06 | 不動產觀測站 | Real Estate | 9return.com.tw | `assets/card-06-realestate.jpg` | `./dashboard.html` | 4欄×1列 | `38px` |

#### 卡片描述

| # | 描述 |
|---|------|
| 01 | 【三三藝】當代藝品展售與藝術家平台，以數位畫廊的形式呈現精品藝術收藏，匯聚兩岸三地新銳與資深藝術家作品。 |
| 02 |【ZooTecture】毛孩與空間的對話。 |
| 03 |【Petlogic】用邏輯理解毛孩。 |
| 04 | Vocus 寵物品種圖鑑百科。 |
| 05 | Vocus 寵物照護知識學堂。 |
| 06 |【九回房地】台灣房地產資訊與建案資料平台，提供最完整的房屋交易、行情與區域分析，是購屋與投資者的專業參考入口。 |

### 4.6 Footer

| 元素 | 目前值 |
|------|--------|
| 聯絡電話 | 0968-222201 |
| Line ID | 331.today |
| 設計規劃開發 | 張書欣 |
| 資訊字級 | `24px` |
| 標籤字級 | `14px` |
| 版權文字 | © 2026 六站聯播 · 設計規劃開發：張書欣 |
| 版權字級 | `16px` |
| 對齊方式 | 置中排列 |
| 社群圖示 1 | Line（連結 line.me） |
| 社群圖示 2 | 電話（連結 tel:） |
| 社群圖示 3 | 藝品藝廊（連結 331.today） |
| Footer padding | `40px 40px 24px` |

---

## 五、背景效果規格

### 5.1 背景底圖

| 參數 | 值 |
|------|-----|
| 圖片 | `assets/bg-main.webp` |
| 位置 | 固定（`fixed`），置中 |
| 尺寸 | 滿版覆蓋（`cover`） |
| 遮罩 | 暗色漸層：頂部 72% → 中部 82% → 底部 92% 透明度 |
| z-index | `0` |

### 5.2 光暈動畫（Orbs）

| 參數 | 值 |
|------|-----|
| 數量 | 3 個 |
| 模糊 | `blur(100px)` |
| 透明度 | `0.15` |
| 動畫 | `orb-float`，交替無限循環 |
| orb-1 | 500×500px，黃色，左上，25s |
| orb-2 | 400×400px，橘色，右上，30s |
| orb-3 | 350×350px，青色，底部，22s |

### 5.3 粒子紋理（Grain）

| 參數 | 值 |
|------|-----|
| 類型 | SVG 內嵌碎形雜訊 |
| 透明度 | `0.04` |
| 動畫 | `grain-shift`，0.5s，4 步驟 |
| z-index | `9998`（最上層，不可點擊） |

---

## 六、動畫與行為規格

| 參數 | 目前值 | 說明 |
|------|--------|------|
| 跑馬燈速度 | `22s` | 越短越快 |
| 黃點脈動 | `3s` | 縮放 1→1.4→1 |
| 卡片錯位顯示 | `80ms` | 滾動進入時逐張延遲 |
| 標題上升動畫 | `1s` | 從下方升起 |
| 標題動畫延遲 | `0.3s` / `0.45s` | 兩行依序 |
| 敘述淡入動畫 | `0.8s`，延遲 `0.7s` | — |
| 光暈漂浮 | `20s` 交替 | 三個 orb 各自 25/30/22s |
| 粒子紋理 | `0.5s` steps(4) | 細微位移 |
| Hover 過渡 | `0.3s` | 顏色/縮放 |
| 卡片 Hover 縮放 | `scale(1.03)` | — |
| 卡片頂部進度條 | `width: 0→100%`，0.45s | hover 時展開 |

---

## 七、響應式斷點

| 斷點 | 適用裝置 | 主要變化 |
|------|----------|----------|
| `≤1024px` | 平板 | 格子變 2 欄 |
| `≤768px` | 一般手機 | 格子變 1 欄，字級縮小，Nav 簡化 |
| `≤480px` | 小手機 | 進一步縮小，電話只留圖示 |

---

## 八、快速修改指南

### 8.1 更換顏色
修改 `:root` 中的 CSS 變數即可全站生效：
```css
:root {
  --accent: #你的黃色;    /* 黃色 */
  --accent-2: #你的橘色;  /* 橘色 */
}
```

### 8.2 更換卡片圖片
將新圖片放入 `assets/`，修改對應卡片的 `src`：
```html
<img class="card-img" src="assets/card-01-gallery.jpg" alt="...">
```

### 8.3 更換卡片文字
搜尋卡片名稱（如「三三藝」）直接替換即可，跑馬燈和 OG 描述中的對應文字也需一併更新。

### 8.4 調整卡片間距
修改 `.bento` 的 `gap` 值：
```css
.bento { gap: 48px; }  /* 加大或縮小 */
```

### 8.5 調整跑馬燈速度
修改 `.marquee-track` 的 `animation-duration`：
```css
.marquee-track { animation: marquee-scroll 22s linear infinite; }
/* 數字越小越快 */
```

---

## 九、版本紀錄

| 版本 | 日期 | 變更 |
|------|------|------|
| v1.0 | 2026-08-30 | 初始規格書建立，記錄所有變數與規格 |

---

*本文件由 欣媒體 MyMatrix 網站專案維護，設計規劃開發：張書欣*
