filepath = r"D:\www\325-public\index.html"

with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

# 1. 加入 3x3 gallery CSS（在 .gallery-item.tall 之後）
three_by_three_css = '''
.gallery-3x3 {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 1rem;
  margin-top: 1rem;
}

.gallery-3x3 .gallery-item {
  aspect-ratio: 1/1;
}

@media (max-width: 768px) {
  .gallery-3x3 { grid-template-columns: repeat(2, 1fr); }
}

/* ===== 主要內容區 ===== */'''

# 找到第一個 "/* ===== 主要內容區 ===== */" 並替換
content = content.replace('/* ===== 主要內容區 ===== */', three_by_three_css, 1)

# 2. 加入 3x3 gallery HTML（在 Footer 之前）
three_by_three_html = '''
<!-- ===== 3x3 影像總覽 ===== -->
<section class="gallery-section reveal">
  <h2 class="gallery-title">空間細節</h2>
  <p class="gallery-subtitle">九個瞬間，看見 OKU 的 Art Deco 靈魂</p>
  <div class="gallery-3x3">
    <div class="gallery-item">
      <img src="assets/gallery-staircase.jpg" alt="Art Deco 樓梯">
      <div class="gallery-overlay"><span class="gallery-overlay-text">華麗樓梯</span></div>
    </div>
    <div class="gallery-item">
      <img src="assets/gallery-bar.jpg" alt="艾莉蕬酒吧">
      <div class="gallery-overlay"><span class="gallery-overlay-text">艾莉蕬酒吧</span></div>
    </div>
    <div class="gallery-item">
      <img src="assets/gallery-restaurant.jpg" alt="Lumen 餐廳">
      <div class="gallery-overlay"><span class="gallery-overlay-text">Lumen 全日餐廳</span></div>
    </div>
    <div class="gallery-item">
      <img src="assets/gallery-room-detail.jpg" alt="客房床頭細節">
      <div class="gallery-overlay"><span class="gallery-overlay-text">客房床頭細節</span></div>
    </div>
    <div class="gallery-item">
      <img src="assets/gallery-bathtub.jpg" alt="銅質浴缸">
      <div class="gallery-overlay"><span class="gallery-overlay-text">手工紅銅浴缸</span></div>
    </div>
    <div class="gallery-item">
      <img src="assets/gallery-entrance.jpg" alt="飯店夜景入口">
      <div class="gallery-overlay"><span class="gallery-overlay-text">夜晚飯店入口</span></div>
    </div>
    <div class="gallery-item">
      <img src="assets/gallery-alley.jpg" alt="舊城巷弄">
      <div class="gallery-overlay"><span class="gallery-overlay-text">台中舊城巷弄</span></div>
    </div>
    <div class="gallery-item">
      <img src="assets/gallery-deco-detail.jpg" alt="Art Deco 黃銅細節">
      <div class="gallery-overlay"><span class="gallery-overlay-text">Art Deco 黃銅細節</span></div>
    </div>
    <div class="gallery-item">
      <img src="assets/gallery-rooftop.jpg" alt="屋頂俯瞰舊城">
      <div class="gallery-overlay"><span class="gallery-overlay-text">屋頂俯瞰舊城</span></div>
    </div>
  </div>
</section>

<!-- Footer -->'''

content = content.replace('<!-- Footer -->', three_by_three_html, 1)

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(content)

print("Done! 3x3 gallery added.")
