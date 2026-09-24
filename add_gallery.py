import re

filepath = r"D:\www\325-public\index.html"

with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

# 1. 修正 title 重複
content = content.replace('OKUOKU舊城風華', 'OKU舊城風華')

# 2. 加入畫廊 CSS（在 .main-container CSS 之前）
gallery_css = '''
/* ===== 照片畫廊 ===== */
.gallery-section {
  padding: 4rem 2rem;
  max-width: 1400px;
  margin: 0 auto;
}

.gallery-title {
  text-align: center;
  font-size: 2rem;
  margin-bottom: 0.5rem;
  color: var(--text-primary);
}

.gallery-subtitle {
  text-align: center;
  color: var(--text-muted);
  font-size: 0.95rem;
  margin-bottom: 2.5rem;
  font-weight: 300;
}

.gallery-grid {
  display: grid;
  grid-template-columns: repeat(4, 1fr);
  gap: 1rem;
}

.gallery-item {
  position: relative;
  border-radius: 12px;
  overflow: hidden;
  cursor: pointer;
  aspect-ratio: 4/3;
  box-shadow: var(--shadow);
  transition: all 0.4s cubic-bezier(0.16, 1, 0.3, 1);
}

.gallery-item:hover {
  transform: translateY(-6px);
  box-shadow: var(--shadow-hover);
}

.gallery-item img {
  width: 100%;
  height: 100%;
  object-fit: cover;
  transition: transform 0.6s ease;
}

.gallery-item:hover img {
  transform: scale(1.08);
}

.gallery-overlay {
  position: absolute;
  inset: 0;
  background: linear-gradient(transparent 50%, rgba(0,0,0,0.75));
  opacity: 0;
  transition: opacity 0.3s;
  display: flex;
  align-items: flex-end;
  padding: 1rem;
}

.gallery-item:hover .gallery-overlay {
  opacity: 1;
}

.gallery-overlay-text {
  color: #fff;
  font-size: 0.9rem;
  font-weight: 500;
}

.gallery-item.tall {
  grid-row: span 2;
  aspect-ratio: auto;
}

@media (max-width: 1024px) {
  .gallery-grid { grid-template-columns: repeat(3, 1fr); }
}

@media (max-width: 768px) {
  .gallery-grid { grid-template-columns: repeat(2, 1fr); gap: 0.75rem; }
  .gallery-item.tall { grid-row: span 1; }
  .gallery-title { font-size: 1.5rem; }
}

/* ===== 主要內容區 ===== */'''

content = content.replace('/* ===== 主要內容區 ===== */', gallery_css, 1)

# 3. 加入畫廊 HTML（在 Hero section 結束後、main container 之前）
gallery_html = '''
<!-- ===== 照片畫廊 ===== -->
<section class="gallery-section reveal">
  <h2 class="gallery-title">影像廊</h2>
  <p class="gallery-subtitle">走進 OKU 的 Art Deco 世界</p>
  <div class="gallery-grid">
    <div class="gallery-item tall">
      <img src="assets/hero-lobby.jpg" alt="三層樓高酒塔大廳">
      <div class="gallery-overlay"><span class="gallery-overlay-text">三層樓高酒塔大廳</span></div>
    </div>
    <div class="gallery-item">
      <img src="assets/ch2-building.jpg" alt="Art Deco 建築外觀">
      <div class="gallery-overlay"><span class="gallery-overlay-text">Art Deco 建築外觀</span></div>
    </div>
    <div class="gallery-item">
      <img src="assets/ch3-room.jpg" alt="銅質浴缸客房">
      <div class="gallery-overlay"><span class="gallery-overlay-text">銅質浴缸客房</span></div>
    </div>
    <div class="gallery-item">
      <img src="assets/ch1-invitation.jpg" alt="復古邀請函設計">
      <div class="gallery-overlay"><span class="gallery-overlay-text">復古邀請函設計</span></div>
    </div>
    <div class="gallery-item">
      <img src="assets/ch4-oldcity.jpg" alt="台中舊城街道">
      <div class="gallery-overlay"><span class="gallery-overlay-text">台中舊城街道</span></div>
    </div>
    <div class="gallery-item">
      <img src="assets/ch5-salon.jpg" alt="沙龍共學場景">
      <div class="gallery-overlay"><span class="gallery-overlay-text">沙龍共學場景</span></div>
    </div>
    <div class="gallery-item">
      <img src="assets/ch6-sunset.jpg" alt="城市黃昏天際線">
      <div class="gallery-overlay"><span class="gallery-overlay-text">城市黃昏天際線</span></div>
    </div>
    <div class="gallery-item">
      <img src="assets/appendix-blueprint.jpg" alt="建築設計藍圖">
      <div class="gallery-overlay"><span class="gallery-overlay-text">建築設計藍圖</span></div>
    </div>
  </div>
</section>

<!-- 主要內容 -->'''

content = content.replace('<!-- 主要內容 -->', gallery_html, 1)

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(content)

print("Done! Gallery added and title fixed.")
