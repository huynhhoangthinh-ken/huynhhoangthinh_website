# -*- coding: utf-8 -*-
"""
Master Image Updater for huynhhoangthinh.com
Scans all local folders in assets/ for thumbnails and applies them
across data/posts.json and index.html.
"""

import json
import os
import re

# 1. Update data/posts.json
with open('data/posts.json', 'r', encoding='utf-8') as f:
    posts = json.load(f)

# Mapping ID to local thumbnail path
thumbnail_map = {
    # Resorts
    801: 'assets/Posts/SO_Madilves/thumbnail.webp',
    802: 'assets/Posts/Six_senses_Con_Dao/Thumbnail.jpg',
    803: 'assets/Posts/Six_senses_ninh_van_bay/Thumbnail.jpg',
    804: 'assets/Posts/amanoi/thumbnail_amanoi.avif',
    805: 'assets/Posts/Amanzoe_Greece/Thumbnail.jpg',
    806: 'assets/Posts/Cap_St_Georges_Resort/Thumbnail.jpg',
    809: 'assets/Posts/Ritz_carlton_Astana/Thumbnail.jpeg',
    810: 'assets/Posts/Amangiri_Utah/Thumbnail.jpg',
    
    # Supercars
    107: 'assets/Posts/Koenigsegg_Jesko_2026/Koenigsegg_Jesko_20261_thumbnail.webp',
    108: 'assets/Posts/Bugatti_tourbillon_2026/Bugatti Tourbillon (2026)1.jpg',
    109: 'assets/Posts/ferrari-laferrari/tbumbnail_ferrari-laferrari-3ab0b-c693322032026005415_1.jpg',
    110: 'assets/Posts/lamborghini-revuelto/thumbnail_lamborghini-revuelto_3.jpeg',
    111: 'assets/Posts/Rolls_Royce_spectre/Thumbnail.webp',
    112: 'assets/Posts/Porsche 911 GT3 RS 2026/thumnail_Porsche 911 GT3 RS 20266.webp',
    115: 'assets/Posts/Pagani_Utopia_2026/thumbnail.avif',
    116: 'assets/Posts/Maserati_MC20/thumbnail_2023-maserati-mc20-cielo-spyder-28-1666275747.avif',
    119: 'assets/Posts/Koenigsegg-Gemera-GT-supercar/Koenigsegg_Gemera_6_thumbnail.webp',
    200: 'assets/Posts/bugatti-chiron/bugatti-chiron_3_thumbnail.jpg',
    202: 'assets/Posts/911_LouisVuitton/Thumbnail.webp',
    135: 'assets/Posts/Range_Rover_GT_Concept/712335-le-prochain-range-rover-sera-une-grande-routiere-electrique.jpg',
    
    # Yachts & Jets
    120: 'assets/Posts/Oceanco_Project_2026/Oceanco_Project_2026_thumbnail.jpg',
    121: 'assets/Posts/Lurssen_Ahpo/Lurssen_AhpoThumbnail.avif',
    122: 'assets/Posts/Feadship_821_(Viva)_2026/Feadship_821_(Viva)_20263_thumbnail.webp',
    123: 'assets/Posts/Gulfstream_G700/Gulfstream_G700_22_thumbnail.jpg',
    124: 'assets/Posts/Bombardier_8000_2026/Bombardier_8000_20266_thumbnail.jpg',
    125: 'assets/Posts/falcon-10x/falcon-10x15_thumbnail.jpg',
    126: 'assets/Posts/Azimut_Grande_36M_2026/Azimut_Grande_36M_2026_thumbnail.webp',
    128: 'assets/Posts/Riva_130_Bellissima_2026/Riva_130_Bellissima_2026_00015_thumbnail.webp',
    131: 'assets/Posts/Pilatus PC-24_2026/Thumbnail.webp',
    716: 'assets/Posts/Airbus_ACH145_ACH160/Airbus_ACH145_thumbnail.jpg',
    617: 'assets/Posts/Helicopter/thumbnail_Helicopter_3.jpg.webp',
    18: 'assets/Posts/Helicopter/thumbnail_Helicopter_3.jpg.webp',
    
    # Watches
    618: 'assets/Posts/Patek Philippe Grandmaster Chime & Nautilus/Patek Philippe Grandmaster Chime & Nautilus:6_thumbnail.avif',
    
    # Real Estate & Cars Market
    606: 'assets/projects/03_RIVUS/Thumbnail.jpg',
    609: 'assets/projects/12_GLADIA/Gladia Web Dai Chung1_NoiThat_NhaBep.jpg',
    704: 'assets/projects/03_RIVUS/Thumbnail.jpg',
    117: 'assets/Posts/Bentley_Flying_Spur_V8/Bentley Flying Spur V8-2.webp',
    405: 'assets/Posts/Bentley_Flying_Spur_V8/thumbnail.webp',
    406: 'assets/Posts/Range_rover_LWB_2024/Thumnbail_Rang_river_LWB.jpeg',
    407: 'assets/Xe_dang_giao_dich/BMW/BMW_735_MSP/Thumbnail.jpg',
    408: 'assets/Xe_dang_giao_dich/Land_rover/DefenderX/Thumbnail.jpg',
    409: 'assets/Xe_dang_giao_dich/Mercedes/Mercedes_ Maybach S450_2019/thumbnail.jpg',
    410: 'assets/Xe_dang_giao_dich/Porsche/Macan_GTS_2021/thumbnail.jpeg',
    411: 'assets/Xe_dang_giao_dich/Porsche/Porsche_911_4S/thumbnail.jpg',
    412: 'assets/Xe_dang_giao_dich/Porsche/Posche_911_GT3TouringTuning/thumbnail.jpg',
    413: 'assets/Xe_dang_giao_dich/Porsche/718_boxter_S/thumbnail.jpg',
    414: 'assets/Xe_dang_giao_dich/Porsche/Porsche_911S/thumbnail.jpg',
    415: 'assets/Xe_dang_giao_dich/Bentley/Bentley_pink/thumbnail.jpg',
    400: 'assets/Xe_dang_giao_dich/Maserarti/Grecale/Thumbnail.jpg',
    401: 'assets/Xe_dang_giao_dich/Maserarti/Grecale/Thumbnail.jpg'
}

# Rich galleries for newly provided resort folders
resort_galleries = {
    802: """
<div style="margin: 30px 0; text-align: center;">
    <img src="assets/Posts/Six_senses_Con_Dao/Six_senses_Con_Dao_8.jpg" alt="Toàn cảnh Six Senses Côn Đảo" style="width: 100%; border-radius: 6px; box-shadow: 0 4px 20px rgba(0,0,0,0.15);" />
    <p style="font-size: 0.85rem; color: #777; font-style: italic; margin-top: 8px;">Toàn cảnh quần thể biệt thự gỗ Teak bên bờ vịnh Đất Dốc nguyên sơ</p>
</div>
<div style="margin: 30px 0; display: grid; grid-template-columns: 1fr 1fr; gap: 16px;">
    <div>
        <img src="assets/Posts/Six_senses_Con_Dao/Six_senses_Con_Dao_2.jpg" alt="Biệt thự hướng biển Six Senses Côn Đảo" style="width: 100%; height: 260px; object-fit: cover; border-radius: 6px;" />
        <p style="font-size: 0.8rem; color: #777; font-style: italic; margin-top: 6px; text-align: center;">Hồ bơi vô cực và bãi cát trắng mịn</p>
    </div>
    <div>
        <img src="assets/Posts/Six_senses_Con_Dao/Six_senses_Con_Dao_5.jpg" alt="Nội thất gỗ mộc mạc Six Senses Côn Đảo" style="width: 100%; height: 260px; object-fit: cover; border-radius: 6px;" />
        <p style="font-size: 0.8rem; color: #777; font-style: italic; margin-top: 6px; text-align: center;">Không gian phòng ngủ mở ngắm bình minh</p>
    </div>
</div>
""",
    803: """
<div style="margin: 30px 0; text-align: center;">
    <img src="assets/Posts/Six_senses_ninh_van_bay/Six_senses_ninh_van_bay_8.jpg" alt="Toàn cảnh Six Senses Ninh Vân Bay" style="width: 100%; border-radius: 6px; box-shadow: 0 4px 20px rgba(0,0,0,0.15);" />
    <p style="font-size: 0.85rem; color: #777; font-style: italic; margin-top: 8px;">Vịnh biển biệt lập và những khối đá granite kỳ vĩ tại Six Senses Ninh Vân Bay</p>
</div>
<div style="margin: 30px 0; display: grid; grid-template-columns: 1fr 1fr; gap: 16px;">
    <div>
        <img src="assets/Posts/Six_senses_ninh_van_bay/Six_senses_ninh_van_bay_1.jpg" alt="Rock Pool Villa Six Senses Ninh Vân Bay" style="width: 100%; height: 260px; object-fit: cover; border-radius: 6px;" />
        <p style="font-size: 0.8rem; color: #777; font-style: italic; margin-top: 6px; text-align: center;">Biệt thự dựng trên vách đá sát mép biển</p>
    </div>
    <div>
        <img src="assets/Posts/Six_senses_ninh_van_bay/Six_senses_ninh_van_bay_4.jpg" alt="Water Pool Villa Six Senses Ninh Vân Bay" style="width: 100%; height: 260px; object-fit: cover; border-radius: 6px;" />
        <p style="font-size: 0.8rem; color: #777; font-style: italic; margin-top: 6px; text-align: center;">Lối đi bằng gỗ và hồ bơi tạc vào đá tự nhiên</p>
    </div>
</div>
""",
    805: """
<div style="margin: 30px 0; text-align: center;">
    <img src="assets/Posts/Amanzoe_Greece/Amanzoe_Greece_1.jpg" alt="Toàn cảnh Amanzoe Peloponnese Hy Lạp" style="width: 100%; border-radius: 6px; box-shadow: 0 4px 20px rgba(0,0,0,0.15);" />
    <p style="font-size: 0.85rem; color: #777; font-style: italic; margin-top: 8px;">Kiến trúc đá cẩm thạch trắng Acropolis đương đại vươn mình trên đồi Peloponnese</p>
</div>
<div style="margin: 30px 0; display: grid; grid-template-columns: 1fr 1fr; gap: 16px;">
    <div>
        <img src="assets/Posts/Amanzoe_Greece/Amanzoe_Greece_2.jpg" alt="Hồ bơi phản chiếu Amanzoe" style="width: 100%; height: 260px; object-fit: cover; border-radius: 6px;" />
        <p style="font-size: 0.8rem; color: #777; font-style: italic; margin-top: 6px; text-align: center;">Hồ bơi vô cực riêng bằng đá cẩm thạch</p>
    </div>
    <div>
        <img src="assets/Posts/Amanzoe_Greece/Amanzoe_Greece_8.jpg" alt="Amanzoe Beach Club" style="width: 100%; height: 260px; object-fit: cover; border-radius: 6px;" />
        <p style="font-size: 0.8rem; color: #777; font-style: italic; margin-top: 6px; text-align: center;">Không gian Beach Club riêng tư bên bờ biển Aegean</p>
    </div>
</div>
""",
    806: """
<div style="margin: 30px 0; text-align: center;">
    <img src="assets/Posts/Cap_St_Georges_Resort/cap-st-georges-hotel_1.jpg" alt="Toàn cảnh Cap St Georges Hotel & Resort" style="width: 100%; border-radius: 6px; box-shadow: 0 4px 20px rgba(0,0,0,0.15);" />
    <p style="font-size: 0.85rem; color: #777; font-style: italic; margin-top: 8px;">Biệt thự đá vôi tự nhiên bên bờ biển Paphos ngập tràn nắng Địa Trung Hải</p>
</div>
<div style="margin: 30px 0; display: grid; grid-template-columns: 1fr 1fr; gap: 16px;">
    <div>
        <img src="assets/Posts/Cap_St_Georges_Resort/cap-st-georges-hotel_3.jpg" alt="Hồ bơi và cảnh quan Cap St Georges" style="width: 100%; height: 260px; object-fit: cover; border-radius: 6px;" />
        <p style="font-size: 0.8rem; color: #777; font-style: italic; margin-top: 6px; text-align: center;">Hồ bơi trung tâm hướng thẳng ra biển Địa Trung Hải</p>
    </div>
    <div>
        <img src="assets/Posts/Cap_St_Georges_Resort/cap-st-georges-hotel_4.jpg" alt="Nội thất sang trọng Cap St Georges" style="width: 100%; height: 260px; object-fit: cover; border-radius: 6px;" />
        <p style="font-size: 0.8rem; color: #777; font-style: italic; margin-top: 6px; text-align: center;">Thiết kế nội thất hiện đại sang trọng bậc nhất đảo Síp</p>
    </div>
</div>
""",
    809: """
<div style="margin: 30px 0; text-align: center;">
    <img src="assets/Posts/Ritz_carlton_Astana/Ritz_carlton_Astana_2.jpeg" alt="The Ritz-Carlton Astana Talan Towers" style="width: 100%; border-radius: 6px; box-shadow: 0 4px 20px rgba(0,0,0,0.15);" />
    <p style="font-size: 0.85rem; color: #777; font-style: italic; margin-top: 8px;">Kiến trúc Talan Towers và sảnh đón tiếp vương giả của The Ritz-Carlton Astana</p>
</div>
<div style="margin: 30px 0; display: grid; grid-template-columns: 1fr 1fr; gap: 16px;">
    <div>
        <img src="assets/Posts/Ritz_carlton_Astana/Ritz_carlton_Astana_3.jpeg" alt="Phòng Suite hoàng gia The Ritz-Carlton Astana" style="width: 100%; height: 260px; object-fit: cover; border-radius: 6px;" />
        <p style="font-size: 0.8rem; color: #777; font-style: italic; margin-top: 6px; text-align: center;">Phòng Suite thượng hạng với tầm nhìn ngắm tháp Bayterek</p>
    </div>
    <div>
        <img src="assets/Posts/Ritz_carlton_Astana/Ritz_carlton_Astana_6.jpeg" alt="Nhà hàng & Club Lounge" style="width: 100%; height: 260px; object-fit: cover; border-radius: 6px;" />
        <p style="font-size: 0.8rem; color: #777; font-style: italic; margin-top: 6px; text-align: center;">Không gian ẩm thực và The Club Lounge đặc quyền</p>
    </div>
</div>
""",
    810: """
<div style="margin: 30px 0; text-align: center;">
    <img src="assets/Posts/Amangiri_Utah/Amangiri_Utah_1.jpg" alt="Hồ bơi đá sa thạch Amangiri Utah" style="width: 100%; border-radius: 6px; box-shadow: 0 4px 20px rgba(0,0,0,0.15);" />
    <p style="font-size: 0.85rem; color: #777; font-style: italic; margin-top: 8px;">Hồ bơi trung tâm uốn lượn ôm trọn khối đá sa thạch 200 triệu năm tại Amangiri</p>
</div>
<div style="margin: 30px 0; display: grid; grid-template-columns: 1fr 1fr; gap: 16px;">
    <div>
        <img src="assets/Posts/Amangiri_Utah/Amangiri_Utah_2.jpg" alt="Kiến trúc bê tông tối giản Amangiri" style="width: 100%; height: 260px; object-fit: cover; border-radius: 6px;" />
        <p style="font-size: 0.8rem; color: #777; font-style: italic; margin-top: 6px; text-align: center;">Kiến trúc bê tông màu cát hòa quyện hẻm núi đá đỏ</p>
    </div>
    <div>
        <img src="assets/Posts/Amangiri_Utah/Amangiri_Utah_3.jpg" alt="Phòng Suite hướng sa mạc Amangiri" style="width: 100%; height: 260px; object-fit: cover; border-radius: 6px;" />
        <p style="font-size: 0.8rem; color: #777; font-style: italic; margin-top: 6px; text-align: center;">Không gian nghỉ dưỡng riêng tư mở ra cao nguyên Colorado Plateau</p>
    </div>
</div>
"""
}

# Apply thumbnail and galleries to data/posts.json
for post in posts:
    p_id = post.get('id')
    if p_id in thumbnail_map:
        post['image'] = thumbnail_map[p_id]
        
    if p_id in resort_galleries:
        content = post.get('content', '')
        if 'assets/Posts/' not in content:
            # Insert gallery after lead
            if "<h2>Chương 1:" in content:
                content = content.replace("<h2>Chương 1:", resort_galleries[p_id] + "\n<h2>Chương 1:")
                post['content'] = content

with open('data/posts.json', 'w', encoding='utf-8') as f:
    json.dump(posts, f, ensure_ascii=False, indent=2)

print("Updated data/posts.json with all local thumbnails and galleries!")

# 2. Update index.html
with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Update Supercars tab cards
html = html.replace('src="assets/vehicles/porsche_gt3_rs.jpg"', 'src="assets/Posts/Porsche 911 GT3 RS 2026/thumnail_Porsche 911 GT3 RS 20266.webp"')
html = html.replace("style=\"background-image: url('assets/Posts/ferrari-laferrari/ferrari-laferrari-0f31e-c414325082026194653_1.jpg');\"", "style=\"background-image: url('assets/Posts/ferrari-laferrari/tbumbnail_ferrari-laferrari-3ab0b-c693322032026005415_1.jpg');\"")
html = html.replace('src="assets/Posts/lamborghini-revuelto/404252-2026-lamborghini-revuelto.jpg"', 'src="assets/Posts/lamborghini-revuelto/thumbnail_lamborghini-revuelto_3.jpeg"')
html = html.replace('src="assets/vehicles/maserati_mc20.jpg"', 'src="assets/Posts/Maserati_MC20/thumbnail_2023-maserati-mc20-cielo-spyder-28-1666275747.avif"')
html = html.replace('src="assets/Posts/Pagani_Utopia_2026/Pagani_Utopia_2026_1.avif"', 'src="assets/Posts/Pagani_Utopia_2026/thumbnail.avif"')
html = html.replace('src="assets/Posts/bugatti-chiron/bugatti-chiron_1.jpg"', 'src="assets/Posts/bugatti-chiron/bugatti-chiron_3_thumbnail.jpg"')
html = html.replace('src="assets/vehicles/bentley_continental_gt.jpg"', 'src="assets/Posts/Bentley_Flying_Spur_V8/Bentley Flying Spur V8-2.webp"')
html = html.replace('src="assets/Posts/Bentley_Flying_Spur_V8/Bentley Flying Spur V8-8.webp"', 'src="assets/Posts/Bentley_Flying_Spur_V8/Bentley Flying Spur V8-2.webp"')

# Update Yachts & Jets
html = html.replace("style=\"background-image: url('assets/Posts/Feadship_821_(Viva)_2026/Feadship_821_(Viva)_20261.webp');\"", "style=\"background-image: url('assets/Posts/Feadship_821_(Viva)_2026/Feadship_821_(Viva)_20263_thumbnail.webp');\"")
html = html.replace('src="assets/Posts/Pilatus PC-24_2026/world_wide_lux_fleet_pilatus_pc-24_1-1536x1024.jpg"', 'src="assets/Posts/Pilatus PC-24_2026/Thumbnail.webp"')

# Update Market Cars
html = html.replace('src="assets/Posts/Range_rover_LWB_2024/Range_rover_LWB1.jpeg"', 'src="assets/Posts/Range_rover_LWB_2024/Thumnbail_Rang_river_LWB.jpeg"')

# Update Resorts tab images
html = html.replace(
    'src="https://images.unsplash.com/photo-1540555700478-4be289fbecef?auto=format&fit=crop&w=1600&q=85"',
    'src="assets/Posts/Six_senses_Con_Dao/Thumbnail.jpg"'
)
html = html.replace(
    'src="https://images.unsplash.com/photo-1571896349842-33c89424de2d?auto=format&fit=crop&w=1600&q=85"',
    'src="assets/Posts/Six_senses_ninh_van_bay/Thumbnail.jpg"'
)
html = html.replace(
    'src="https://images.unsplash.com/photo-1533105079780-92b9be482077?auto=format&fit=crop&w=1600&q=85"',
    'src="assets/Posts/Amanzoe_Greece/Thumbnail.jpg"'
)
html = html.replace(
    'src="https://images.unsplash.com/photo-1566073771259-6a8506099945?auto=format&fit=crop&w=1600&q=85"',
    'src="assets/Posts/Cap_St_Georges_Resort/Thumbnail.jpg"'
)
html = html.replace(
    'src="https://images.unsplash.com/photo-1578683010236-d716f9a3f461?auto=format&fit=crop&w=1600&q=85"',
    'src="assets/Posts/Ritz_carlton_Astana/Thumbnail.jpeg"'
)
html = html.replace(
    'src="https://images.unsplash.com/photo-1518780664697-55e3ad937233?auto=format&fit=crop&w=1600&q=85"',
    'src="assets/Posts/Amangiri_Utah/Thumbnail.jpg"'
)
html = html.replace(
    "style=\"background-image: url('https://images.unsplash.com/photo-1518780664697-55e3ad937233?auto=format&fit=crop&w=1600&q=85');\"",
    "style=\"background-image: url('assets/Posts/Amangiri_Utah/Thumbnail.jpg');\""
)

# Update Real Estate The Rivus
html = html.replace(
    "style=\"background-image: url('assets/projects/03_RIVUS/Rivus_Photo_TongHop_001_NgoaiThat_Flycam_TongThe.jpg');\"",
    "style=\"background-image: url('assets/projects/03_RIVUS/Thumbnail.jpg');\""
)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("Updated index.html with all local thumbnails!")
