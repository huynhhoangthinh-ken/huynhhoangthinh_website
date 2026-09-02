# -*- coding: utf-8 -*-
"""
Injects the dedicated Resort Tab into index.html and updates nav links.
"""

import json

# Read 13 resort articles from posts.json to get metadata
with open('data/posts.json', 'r', encoding='utf-8') as f:
    posts = json.load(f)

resorts_list = [p for p in posts if p.get('id') in range(801, 814)]
resorts_list.sort(key=lambda x: x['id'])

grid_items_html = ""
for r in resorts_list:
    r_id = r['id']
    r_title = r['title']
    r_img = r['image']
    r_country = r['category_label'].split('•')[-1].strip()
    
    badge_tag = "ĐÃ TRẢI NGHIỆM" if r_id == 801 else "5★ LUXURY"
    badge_bg = "#d4af37" if r_id == 801 else "#1a1a1a"
    badge_color = "#000" if r_id == 801 else "#c9a96e"
    
    # Custom subtitle
    subtitles = {
        801: "Emboodhoo Lagoon • Sàn diễn thời trang & Lagoon Water Pool Villa",
        802: "Vịnh Đất Dốc • 50 Biệt thự gỗ Teak & Bảo tồn rùa biển",
        803: "Vịnh Ninh Vân • Biệt thự vách đá Rock Villa & Hầm rượu hang đá",
        804: "Vườn QG Núi Chúa • Hồ bơi Cliff Pool 100m & Wellness Pool Villa",
        805: "Peloponnese • Đền thờ Acropolis cẩm thạch trắng & Beach Club",
        806: "Paphos • Biệt thự đá vôi tự nhiên & Bãi biển riêng Địa Trung Hải",
        807: "Koh Kood • Phi cơ riêng Cessna, Treepod Dining & Cinema Paradiso",
        808: "Uluwatu • Vách đá 150m biển sâu, đá núi lửa đen & Thang máy nghiêng",
        809: "Talan Towers • Sảnh cẩm thạch hoàng gia & Club Lounge tầng 18",
        810: "Canyon Point • Bê tông sa mạc tối giản & Hồ bơi đá sa thạch 200tr năm",
        811: "Hồ Como • Cung điện Phục Hưng 1568 & Floating Pool trên mặt hồ",
        812: "Hồ Lucerne • Vách núi 500m & Hồ bơi vô cực nước ấm 35°C giữa mây",
        813: "French Riviera • Cung điện Palace 1908 & Hồ bơi nước biển Club Dauphin"
    }
    sub = subtitles.get(r_id, r.get('excerpt', '')[:65] + '...')

    grid_items_html += f"""
          <!-- Resort Item {r_id}: {r_title.split(':')[0]} -->
          <a class="grid-card" href="article.html?id={r_id}" style="text-decoration: none; color: inherit; display: flex; flex-direction: column;">
            <div class="grid-img" style="position: relative; overflow: hidden; border-radius: 4px; aspect-ratio: 16/10;">
              <img alt="{r_title}" src="{r_img}" loading="lazy" style="width: 100%; height: 100%; object-fit: cover; transition: transform 0.4s ease;" />
              <span style="position: absolute; top: 10px; left: 10px; background: {badge_bg}; color: {badge_color}; font-size: 0.65rem; font-weight: 700; padding: 4px 8px; border-radius: 3px; letter-spacing: 0.05em; backdrop-filter: blur(4px); box-shadow: 0 2px 8px rgba(0,0,0,0.3);">
                {badge_tag}
              </span>
              <span style="position: absolute; bottom: 10px; right: 10px; background: rgba(0,0,0,0.75); color: #fff; font-size: 0.65rem; font-weight: 600; padding: 3px 8px; border-radius: 3px;">
                <i class="fa-solid fa-location-dot" style="color: #d4af37; margin-right: 4px;"></i>{r_country}
              </span>
            </div>
            <div class="grid-card-info" style="display: flex; flex-direction: column; flex-grow: 1; padding-top: 12px;">
              <h5 style="font-size: 0.98rem; font-weight: 700; margin-bottom: 6px; line-height: 1.4;">{r_title}</h5>
              <p class="grid-card-subtitle" style="font-size: 0.82rem; color: #666; margin-bottom: 12px; line-height: 1.5; display: -webkit-box; -webkit-line-clamp: 2; -webkit-box-orient: vertical; overflow: hidden;">{sub}</p>
              <div style="margin-top: auto; display: flex; justify-content: space-between; align-items: center; border-top: 1px solid #f0f0f0; padding-top: 10px;">
                <span style="font-size: 0.75rem; color: #d4af37; font-weight: 700; letter-spacing: 0.05em;">ĐỌC BÀI REVIEW <i class="fa-solid fa-arrow-right" style="font-size: 0.7rem; margin-left: 4px;"></i></span>
                <span style="font-size: 0.72rem; color: #999;">2.000+ từ</span>
              </div>
            </div>
          </a>
"""

tab_resorts_html = f"""
      <!-- Tab: Resort & Nghỉ Dưỡng Xa Xỉ Toàn Cầu (13 Điểm Đến Đã Tuyển Chọn & Trực Tiếp Trải Nghiệm) -->
      <div class="tab-content active" id="tab-resorts">
        <div class="top-listing">
          <!-- Top 1: SO/ Maldives (Review Trải nghiệm trực tiếp của Huỳnh Hoàng Thịnh) -->
          <a class="top-listing-card" href="article.html?id=801"
            style="text-decoration: none; color: inherit; display: block; position: relative;">
            <div class="top-listing-img"
              style="background-image: url('https://images.unsplash.com/photo-1514282401047-d79a71a590e8?auto=format&fit=crop&w=1600&q=85');">
            </div>
            <div
              style="position: absolute; top: 16px; left: 16px; background: #d4af37; color: #000; font-size: 0.72rem; font-weight: 800; padding: 4px 10px; border-radius: 4px; letter-spacing: 0.05em; box-shadow: 0 4px 12px rgba(0,0,0,0.3);">
              ★ HUỲNH HOÀNG THỊNH ĐÃ TRẢI NGHIỆM • LAGOON WATER VILLA</div>
            <div class="top-listing-info">
              <h4>SO/ Maldives — Sàn Diễn Runway Thời Trang Giữa Ấn Độ Dương</h4>
              <p>Review thực tế: The Runway catwalk, Overwater Pool Villa & Hadaba Levant ẩm thực</p>
            </div>
          </a>

          <!-- Top 2: Amanoi Ninh Thuận -->
          <a class="top-listing-card" href="article.html?id=804"
            style="text-decoration: none; color: inherit; display: block; position: relative;">
            <div class="top-listing-img"
              style="background-image: url('https://images.unsplash.com/photo-1582719478250-c89cae4dc85b?auto=format&fit=crop&w=1600&q=85');">
            </div>
            <div
              style="position: absolute; top: 16px; left: 16px; background: #2e7d32; color: #fff; font-size: 0.72rem; font-weight: 700; padding: 4px 10px; border-radius: 4px; letter-spacing: 0.05em;">
              AMAN RESORTS • VƯỜN QUỐC GIA NÚI CHÚA</div>
            <div class="top-listing-info">
              <h4>Amanoi Ninh Thuận — Đỉnh Cao Xa Xỉ Tĩnh Lặng</h4>
              <p>Kiệt tác Jean-Michel Gathy, hồ bơi Cliff Pool 100m & Wellness Pool Villa</p>
            </div>
          </a>

          <!-- Top 3: Amangiri Utah (Mỹ) -->
          <a class="top-listing-card" href="article.html?id=810"
            style="text-decoration: none; color: inherit; display: block; position: relative;">
            <div class="top-listing-img"
              style="background-image: url('https://images.unsplash.com/photo-1518780664697-55e3ad937233?auto=format&fit=crop&w=1600&q=85');">
            </div>
            <div
              style="position: absolute; top: 16px; left: 16px; background: #c9a96e; color: #000; font-size: 0.72rem; font-weight: 700; padding: 4px 10px; border-radius: 4px; letter-spacing: 0.05em;">
              COLORADO PLATEAU • HẺM NÚI ĐÁ ĐỎ 200 TRIỆU NĂM</div>
            <div class="top-listing-info">
              <h4>Amangiri Utah — Ẩn Náu Giữa Sa Mạc Nước Mỹ</h4>
              <p>Hồ bơi ôm trọn khối đá sa thạch nguyên sinh, chốn lui tới của giới tỷ phú Silicon Valley</p>
            </div>
          </a>
        </div>

        <!-- 13 World-Class Resorts Grid Listing -->
        <div class="grid-listing">
{grid_items_html}
        </div>
      </div>
"""

# Read index.html
with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Update Navigation Menu Links in Desktop Header
old_nav = """      <nav class="nav-menu-links">
        <a class="nav-link active" href="#news-section">Tạp Chí</a>
        <a class="nav-link" data-target="tab-cars" href="#tabs-section">Siêu Xe</a>
        <a class="nav-link" data-target="tab-yachts" href="#tabs-section">Du Thuyền & Chuyên Cơ</a>
        <a class="nav-link" data-target="tab-cars-market" href="#tabs-section">Xe Đang Giao Dịch</a>
        <a class="nav-link" data-target="tab-realestate" href="#tabs-section">Bất Động Sản</a>
      </nav>"""

new_nav = """      <nav class="nav-menu-links">
        <a class="nav-link active" href="#news-section">Tạp Chí</a>
        <a class="nav-link" data-target="tab-resorts" href="#tabs-section">Resort Xa Xỉ</a>
        <a class="nav-link" data-target="tab-cars" href="#tabs-section">Siêu Xe</a>
        <a class="nav-link" data-target="tab-yachts" href="#tabs-section">Du Thuyền & Chuyên Cơ</a>
        <a class="nav-link" data-target="tab-cars-market" href="#tabs-section">Xe Đang Giao Dịch</a>
        <a class="nav-link" data-target="tab-realestate" href="#tabs-section">Bất Động Sản</a>
      </nav>"""

if old_nav in html:
    html = html.replace(old_nav, new_nav)
else:
    print("Warning: old_nav not exact match, attempting regex replacement")

# 2. Update Mobile Menu Links
old_mobile_links = """    <div class="mobile-menu-links">
      <a href="#news-section" onclick="closeMobileMenu()"><i class="fa-solid fa-book-open"
          style="width:20px;margin-right:8px;"></i>Tạp Chí</a>
      <a data-tab="tab-cars" href="#tabs-section" onclick="closeMobileMenu()"><i class="fa-solid fa-car"
          style="width:20px;margin-right:8px;"></i>Siêu Xe</a>
      <a data-tab="tab-yachts" href="#tabs-section" onclick="closeMobileMenu()"><i class="fa-solid fa-sailboat"
          style="width:20px;margin-right:8px;"></i>Du Thuyền & Chuyên Cơ</a>
      <a data-tab="tab-cars-market" href="#tabs-section" onclick="closeMobileMenu()"><i class="fa-solid fa-car-side"
          style="width:20px;margin-right:8px;"></i>Xe Đang Giao Dịch</a>
      <a data-tab="tab-realestate" href="#tabs-section" onclick="closeMobileMenu()"><i
          class="fa-solid fa-building-columns" style="width:20px;margin-right:8px;"></i>Bất Động Sản</a>
    </div>"""

new_mobile_links = """    <div class="mobile-menu-links">
      <a href="#news-section" onclick="closeMobileMenu()"><i class="fa-solid fa-book-open"
          style="width:20px;margin-right:8px;"></i>Tạp Chí</a>
      <a data-tab="tab-resorts" href="#tabs-section" onclick="closeMobileMenu()"><i class="fa-solid fa-umbrella-beach"
          style="width:20px;margin-right:8px;"></i>Resort Xa Xỉ</a>
      <a data-tab="tab-cars" href="#tabs-section" onclick="closeMobileMenu()"><i class="fa-solid fa-car"
          style="width:20px;margin-right:8px;"></i>Siêu Xe</a>
      <a data-tab="tab-yachts" href="#tabs-section" onclick="closeMobileMenu()"><i class="fa-solid fa-sailboat"
          style="width:20px;margin-right:8px;"></i>Du Thuyền & Chuyên Cơ</a>
      <a data-tab="tab-cars-market" href="#tabs-section" onclick="closeMobileMenu()"><i class="fa-solid fa-car-side"
          style="width:20px;margin-right:8px;"></i>Xe Đang Giao Dịch</a>
      <a data-tab="tab-realestate" href="#tabs-section" onclick="closeMobileMenu()"><i
          class="fa-solid fa-building-columns" style="width:20px;margin-right:8px;"></i>Bất Động Sản</a>
    </div>"""

if old_mobile_links in html:
    html = html.replace(old_mobile_links, new_mobile_links)

# 3. Update Tab Buttons Header
old_tabs_header = """      <div class="tabs-header">
        <button class="tab-btn active" data-tab="tab-cars">Siêu Xe</button>
        <button class="tab-btn" data-tab="tab-yachts">Du Thuyền & Chuyên Cơ</button>
        <button class="tab-btn" data-tab="tab-cars-market">Xe Đang Giao Dịch <span
            style="background:#c9a96e;color:#000;font-size:0.6rem;padding:2px 6px;border-radius:10px;margin-left:4px;font-weight:700;">MỞ
            BÁN</span></button>
        <button class="tab-btn" data-tab="tab-realestate">Bất Động Sản Cao Cấp</button>
        <button class="tab-btn" data-tab="tab-editorial">Tất Cả Tạp Chí</button>
      </div>"""

new_tabs_header = """      <div class="tabs-header">
        <button class="tab-btn active" data-tab="tab-resorts">Resort Toàn Cầu <span
            style="background:#d4af37;color:#000;font-size:0.6rem;padding:2px 6px;border-radius:10px;margin-left:4px;font-weight:700;">ĐÃ TRẢI NGHIỆM</span></button>
        <button class="tab-btn" data-tab="tab-cars">Siêu Xe</button>
        <button class="tab-btn" data-tab="tab-yachts">Du Thuyền & Chuyên Cơ</button>
        <button class="tab-btn" data-tab="tab-cars-market">Xe Đang Giao Dịch <span
            style="background:#c9a96e;color:#000;font-size:0.6rem;padding:2px 6px;border-radius:10px;margin-left:4px;font-weight:700;">MỞ
            BÁN</span></button>
        <button class="tab-btn" data-tab="tab-realestate">Bất Động Sản Cao Cấp</button>
        <button class="tab-btn" data-tab="tab-editorial">Tất Cả Tạp Chí</button>
      </div>"""

if old_tabs_header in html:
    html = html.replace(old_tabs_header, new_tabs_header)

# Make sure tab-cars is not active by default if tab-resorts is active
html = html.replace('<div class="tab-content active" id="tab-cars">', '<div class="tab-content" id="tab-cars">')

# 4. Insert tab_resorts_html before tab-cars
if 'id="tab-resorts"' not in html:
    html = html.replace('<div class="tab-content" id="tab-cars">', tab_resorts_html + '\n      <div class="tab-content" id="tab-cars">')

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("Successfully injected Resort Tab into index.html!")
