# -*- coding: utf-8 -*-
"""
Update SO/ Maldives images across posts.json and index.html
using authentic assets from assets/Posts/SO_Madilves/.
"""

import json
import re

# 1. Update data/posts.json
with open('data/posts.json', 'r', encoding='utf-8') as f:
    posts = json.load(f)

for post in posts:
    if post.get('id') == 801:
        # Update main thumbnail
        post['image'] = 'assets/Posts/SO_Madilves/thumbnail.webp'
        
        content = post.get('content', '')
        
        # Insert authentic images into chapters if not already present
        if 'assets/Posts/SO_Madilves/' not in content:
            img_block_1 = """
<div style="margin: 30px 0; text-align: center;">
    <img src="assets/Posts/SO_Madilves/maldives-fb-1440x560-watervillas-1-1.webp" alt="Quần thể biệt thự nổi trên mặt biển SO/ Maldives" style="width: 100%; border-radius: 6px; box-shadow: 0 4px 20px rgba(0,0,0,0.15);" />
    <p style="font-size: 0.85rem; color: #777; font-style: italic; margin-top: 8px;">Toàn cảnh quần thể biệt thự nổi Water Villa và cầu cảng The Runway tại Emboodhoo Lagoon</p>
</div>
"""
            img_block_2 = """
<div style="margin: 30px 0; display: grid; grid-template-columns: 1fr 1fr; gap: 16px;">
    <div>
        <img src="assets/Posts/SO_Madilves/SO_maldives_villas_Lagoon-water-pool-villa_1_overview.webp" alt="Lagoon Water Pool Villa SO Maldives" style="width: 100%; height: 260px; object-fit: cover; border-radius: 6px;" />
        <p style="font-size: 0.8rem; color: #777; font-style: italic; margin-top: 6px; text-align: center;">Không gian Lagoon Water Pool Villa nhìn từ ban công riêng</p>
    </div>
    <div>
        <img src="assets/Posts/SO_Madilves/SO_maldives_villas_Lagoon-water-pool-villa_2_overview.webp" alt="Nội thất sang trọng Lagoon Water Pool Villa" style="width: 100%; height: 260px; object-fit: cover; border-radius: 6px;" />
        <p style="font-size: 0.8rem; color: #777; font-style: italic; margin-top: 6px; text-align: center;">Chi tiết nội thất đương đại và hồ bơi vô cực riêng hướng biển</p>
    </div>
</div>
"""
            img_block_3 = """
<div style="margin: 30px 0; text-align: center;">
    <img src="assets/Posts/SO_Madilves/maldives-fb-1440x560-beachvillas-1_1dffbd.webp" alt="Beach Villa và bờ cát trắng mịn SO Maldives" style="width: 100%; border-radius: 6px; box-shadow: 0 4px 20px rgba(0,0,0,0.15);" />
    <p style="font-size: 0.85rem; color: #777; font-style: italic; margin-top: 8px;">Khu biệt thự hướng biển Beach Villa ẩn mình giữa rặng dừa nhiệt đới</p>
</div>
"""
            img_block_4 = """
<div style="margin: 30px 0; display: grid; grid-template-columns: 1fr 1fr 1fr; gap: 12px;">
    <div>
        <img src="assets/Posts/SO_Madilves/maldives-roomcards-water-lagoon-800x800-1.webp" alt="Phòng ngủ hướng biển SO Maldives" style="width: 100%; height: 200px; object-fit: cover; border-radius: 6px;" />
        <p style="font-size: 0.75rem; color: #777; text-align: center; margin-top: 4px;">Giường ngủ Master King view biển</p>
    </div>
    <div>
        <img src="assets/Posts/SO_Madilves/maldives-details-650x800-sunlounge-1.webp" alt="Ghế tắm nắng ban công" style="width: 100%; height: 200px; object-fit: cover; border-radius: 6px;" />
        <p style="font-size: 0.75rem; color: #777; text-align: center; margin-top: 4px;">Khu vực tắm nắng riêng tư</p>
    </div>
    <div>
        <img src="assets/Posts/SO_Madilves/maldives-roomcards-water-ocean-800x800-1.webp" alt="Bồn tắm đá cẩm thạch" style="width: 100%; height: 200px; object-fit: cover; border-radius: 6px;" />
        <p style="font-size: 0.75rem; color: #777; text-align: center; margin-top: 4px;">Bồn tắm cẩm thạch chạm sàn</p>
    </div>
</div>
"""
            # Insert images after chapter headers
            if "<h2>Chương 1:" in content:
                content = content.replace("<h2>Chương 1:", img_block_1 + "<h2>Chương 1:")
            if "<h2>Chương 2:" in content:
                content = content.replace("<h2>Chương 2:", img_block_2 + "<h2>Chương 2:")
            if "<h2>Chương 3:" in content:
                content = content.replace("<h2>Chương 3:", img_block_3 + "<h2>Chương 3:")
            if "<h2>Chương 4:" in content:
                content = content.replace("<h2>Chương 4:", img_block_4 + "<h2>Chương 4:")
                
            post['content'] = content

with open('data/posts.json', 'w', encoding='utf-8') as f:
    json.dump(posts, f, ensure_ascii=False, indent=2)

print("Updated data/posts.json with SO/ Maldives local images.")

# 2. Update index.html
with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Replace any external unsplash photo for SO Maldives with local thumbnail
html = html.replace(
    "style=\"background-image: url('https://images.unsplash.com/photo-1514282401047-d79a71a590e8?auto=format&fit=crop&w=1600&q=85');\"",
    "style=\"background-image: url('assets/Posts/SO_Madilves/thumbnail.webp');\""
)
html = html.replace(
    "src=\"https://images.unsplash.com/photo-1514282401047-d79a71a590e8?auto=format&fit=crop&w=1600&q=85\"",
    "src=\"assets/Posts/SO_Madilves/thumbnail.webp\""
)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("Updated index.html with SO/ Maldives local images.")
