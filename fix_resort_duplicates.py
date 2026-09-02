# -*- coding: utf-8 -*-
"""
Remove duplicate resort cards from tab-resorts grid in index.html.
Top 3: 801 (SO/ Maldives), 804 (Amanoi Ninh Thuận), 810 (Amangiri Utah)
Grid 10: 802, 803, 805, 806, 807, 808, 809, 811, 812, 813.
"""

import json

with open('data/posts.json', 'r', encoding='utf-8') as f:
    posts = json.load(f)

# The 10 grid resorts (excluding 801, 804, 810 which are in top-listing)
grid_ids = [802, 803, 805, 806, 807, 808, 809, 811, 812, 813]
grid_resorts = [p for p in posts if p.get('id') in grid_ids]
grid_resorts.sort(key=lambda x: grid_ids.index(x['id']))

subtitles = {
    802: "Vịnh Đất Dốc • 50 Biệt thự gỗ Teak & Bảo tồn rùa biển",
    803: "Vịnh Ninh Vân • Biệt thự vách đá Rock Villa & Hầm rượu hang đá",
    805: "Peloponnese • Đền thờ Acropolis cẩm thạch trắng & Beach Club",
    806: "Paphos • Biệt thự đá vôi tự nhiên & Bãi biển riêng Địa Trung Hải",
    807: "Koh Kood • Phi cơ riêng Cessna, Treepod Dining & Cinema Paradiso",
    808: "Uluwatu • Vách đá 150m biển sâu, đá núi lửa đen & Thang máy nghiêng",
    809: "Talan Towers • Sảnh cẩm thạch hoàng gia & Club Lounge tầng 18",
    811: "Hồ Como • Cung điện Phục Hưng 1568 & Floating Pool trên mặt hồ",
    812: "Hồ Lucerne • Vách núi 500m & Hồ bơi vô cực nước ấm 35°C giữa mây",
    813: "French Riviera • Cung điện Palace 1908 & Hồ bơi nước biển Club Dauphin"
}

grid_html = ""
for r in grid_resorts:
    r_id = r['id']
    r_title = r['title']
    r_img = r.get('image', '')
    r_country = r.get('category_label', '').split('•')[-1].strip()
    sub = subtitles.get(r_id, r.get('excerpt', '')[:65] + '...')
    
    grid_html += f"""
          <!-- Resort Item {r_id}: {r_title.split(':')[0]} -->
          <a class="grid-card" href="article.html?id={r_id}" style="text-decoration: none; color: inherit; display: flex; flex-direction: column;">
            <div class="grid-img" style="position: relative; overflow: hidden; border-radius: 4px; aspect-ratio: 16/10;">
              <img alt="{r_title}" src="{r_img}" loading="lazy" style="width: 100%; height: 100%; object-fit: cover; transition: transform 0.4s ease;" />
              <span style="position: absolute; top: 10px; left: 10px; background: #1a1a1a; color: #c9a96e; font-size: 0.65rem; font-weight: 700; padding: 4px 8px; border-radius: 3px; letter-spacing: 0.05em; backdrop-filter: blur(4px); box-shadow: 0 2px 8px rgba(0,0,0,0.3);">
                5★ LUXURY
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

new_tab_resorts = f"""      <!-- Tab: Resort & Nghỉ Dưỡng Xa Xỉ Toàn Cầu (13 Điểm Đến Đã Tuyển Chọn & Trực Tiếp Trải Nghiệm) -->
      <div class="tab-content active" id="tab-resorts">
        <div class="top-listing">
          <!-- Top 1: SO/ Maldives (Review Trải nghiệm trực tiếp của Huỳnh Hoàng Thịnh) -->
          <a class="top-listing-card" href="article.html?id=801"
            style="text-decoration: none; color: inherit; display: block; position: relative;">
            <div class="top-listing-img"
              style="background-image: url('assets/Posts/SO_Madilves/thumbnail.webp');">
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
              style="background-image: url('assets/Posts/Amangiri_Utah/Thumbnail.jpg');">
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

        <!-- 10 World-Class Resorts Grid Listing (Không trùng lặp Top 3) -->
        <div class="grid-listing">
{grid_html}
        </div>
      </div>"""

# Read index.html and replace tab-resorts section
with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

import re
# Regex to find <div class="tab-content active" id="tab-resorts">...</div> before <div class="tab-content" id="tab-cars">
pattern = r'<div class="tab-content active" id="tab-resorts">.*?</div>\s*</div>\s*(?=<div class="tab-content" id="tab-cars">)'
match = re.search(pattern, html, re.DOTALL)
if match:
    html = html[:match.start()] + new_tab_resorts + '\n\n      ' + html[match.end():]
    print("Replaced tab-resorts successfully with Regex!")
else:
    # Alternative replacement
    start_tag = '<div class="tab-content active" id="tab-resorts">'
    end_tag = '<div class="tab-content" id="tab-cars">'
    start_idx = html.find(start_tag)
    end_idx = html.find(end_tag)
    if start_idx != -1 and end_idx != -1:
        html = html[:start_idx] + new_tab_resorts + '\n\n      ' + html[end_idx:]
        print("Replaced tab-resorts successfully with Slice!")

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("index.html is now free of any resort card duplicates!")
