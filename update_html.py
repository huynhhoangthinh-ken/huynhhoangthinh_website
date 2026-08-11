import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Update News Section Links and Titles
news_replacements = [
    (r'<a href="#article" class="featured-news-card">', r'<a href="article.html?id=1" class="featured-news-card">'),
    (r'<h3 class="featured-news-title">Khám Phá Vẻ Đẹp Thiên Nhiên – Nguồn Cảm Hứng Bất Tận Cho Cuộc Sống \(Bản sao\)</h3>', r'<h3 class="featured-news-title">Bất động sản siêu sang: Khi giới tinh hoa chọn phong cách sống cá nhân hoá</h3>'),
    
    (r'<a href="#article-1" class="side-news-item">', r'<a href="article.html?id=2" class="side-news-item">'),
    (r'<h4 class="side-news-title">Khám Phá Vẻ Đẹp Thiên Nhiên – Nguồn Cảm Hứng Bất Tận Cho Cuộc Sống \(Bản sao\)</h4>', r'<h4 class="side-news-title">Du thuyền 2026: Hành trình kiến tạo những trải nghiệm vượt đại dương</h4>', 1),
    
    (r'<a href="#article-2" class="side-news-item">', r'<a href="article.html?id=3" class="side-news-item">'),
    (r'<h4 class="side-news-title">Khám Phá Vẻ Đẹp Thiên Nhiên – Nguồn Cảm Hứng Bất Tận Cho Cuộc Sống \(Bản sao\)</h4>', r'<h4 class="side-news-title">Hypercar Thế Hệ Mới: Tốc Độ Và Nghệ Thuật Thiết Kế Đỉnh Cao</h4>', 1),
    
    (r'<a href="#article-3" class="side-news-item">', r'<a href="article.html?id=4" class="side-news-item">'),
    (r'<h4 class="side-news-title">Khám Phá Vẻ Đẹp Thiên Nhiên – Nguồn Cảm Hứng Bất Tận Cho Cuộc Sống \(Bản sao\)</h4>', r'<h4 class="side-news-title">Private Jet: Kỷ Nguyên Mới Của Hàng Không Cá Nhân Hóa</h4>', 1)
]

for old, new, *args in news_replacements:
    count = args[0] if args else 0
    content = re.sub(old, new, content, count=count)


# Jet images
jet_imgs = {
    "Gulfstream G700": "https://images.unsplash.com/photo-1540962351504-03099e0a754b?auto=format&fit=crop&w=800&q=80",
    "Bombardier Global 8000": "https://images.unsplash.com/photo-1559087867-ce4c91325525?auto=format&fit=crop&w=800&q=80",
    "Dassault Falcon 10X": "https://images.unsplash.com/photo-1583416750470-965b2707b355?auto=format&fit=crop&w=800&q=80",
    "Cessna Citation Longitude": "https://images.unsplash.com/photo-1517999144091-3d9dca6d1e43?auto=format&fit=crop&w=800&q=80",
    "Embraer Praetor 600": "https://images.unsplash.com/photo-1579899321307-e818820c7a5f?auto=format&fit=crop&w=800&q=80",
    "Pilatus PC-24": "https://images.unsplash.com/photo-1620612239462-23c8a5202867?auto=format&fit=crop&w=800&q=80"
}

# Yacht images
yacht_imgs = {
    "Oceanco Project": "https://images.unsplash.com/photo-1569263979104-865ab7cd8d13?auto=format&fit=crop&w=800&q=80",
    "Lurssen Ahpo": "https://images.unsplash.com/photo-1605281317010-fe5ffe798166?auto=format&fit=crop&w=800&q=80",
    "Feadship 821": "https://images.unsplash.com/photo-1567899378494-47b22a2ae96a?auto=format&fit=crop&w=800&q=80",
    "Azimut Grande 36M": "https://images.unsplash.com/photo-1580983218765-f663ca0e0be0?auto=format&fit=crop&w=800&q=80",
    "Sunseeker Ocean 182": "https://images.unsplash.com/photo-1569263979104-865ab7cd8d13?auto=format&fit=crop&w=800&q=80",
    "Riva 130 Bellissima": "https://images.unsplash.com/photo-1605281317010-fe5ffe798166?auto=format&fit=crop&w=800&q=80"
}

# Car images
car_imgs = {
    "Koenigsegg Jesko": "https://images.unsplash.com/photo-1614162692292-7ac56d7f7f1e?auto=format&fit=crop&w=800&q=80",
    "Bugatti Chiron": "https://images.unsplash.com/photo-1603584173870-7f23fdae1b7a?auto=format&fit=crop&w=800&q=80",
    "Ferrari LaFerrari": "https://images.unsplash.com/photo-1583121274602-3e2820c69888?auto=format&fit=crop&w=800&q=80",
    "Lamborghini Revuelto": "https://images.unsplash.com/photo-1511919884226-fd3cad34687c?auto=format&fit=crop&w=800&q=80",
    "Rolls-Royce Spectre": "https://images.unsplash.com/photo-1633503251455-84728565cde9?auto=format&fit=crop&w=800&q=80",
    "Porsche 911 GT3 RS": "https://images.unsplash.com/photo-1503376713217-1014abfb0c3d?auto=format&fit=crop&w=800&q=80",
    "McLaren 750S": "https://images.unsplash.com/photo-1605559424843-9e4c228bf1c2?auto=format&fit=crop&w=800&q=80",
    "Aston Martin Valkyrie": "https://images.unsplash.com/photo-1603584173870-7f23fdae1b7a?auto=format&fit=crop&w=800&q=80",
    "Pagani Utopia": "https://images.unsplash.com/photo-1614162692292-7ac56d7f7f1e?auto=format&fit=crop&w=800&q=80",
    "Maserati MC20": "https://images.unsplash.com/photo-1583121274602-3e2820c69888?auto=format&fit=crop&w=800&q=80",
    "Bentley Continental GT": "https://images.unsplash.com/photo-1633503251455-84728565cde9?auto=format&fit=crop&w=800&q=80",
    "Mercedes-AMG One": "https://images.unsplash.com/photo-1503376713217-1014abfb0c3d?auto=format&fit=crop&w=800&q=80",
    "Koenigsegg Gemera": "https://images.unsplash.com/photo-1614162692292-7ac56d7f7f1e?auto=format&fit=crop&w=800&q=80"
}

import re

# We will regex replace the image tags or background urls based on the preceding/succeeding text

# Helper to find and replace top listing cards background
def replace_top_listing_bg(name, img_url, content_str):
    # Looking for:
    # <div class="top-listing-img" style="background-image: url('assets/cat_cars.png');"></div>
    # <div class="top-listing-info">
    #   <h4>Koenigsegg Jesko</h4>
    
    # We regex find the block
    pattern = r'(<div class="top-listing-img" style="background-image: url\()[^>]*(\);"></div>\s*<div class="top-listing-info">\s*<h4>' + re.escape(name) + r'</h4>)'
    return re.sub(pattern, r"\1'" + img_url + r"'\2", content_str)

def replace_grid_listing_img(name, img_url, content_str):
    # Looking for:
    # <div class="grid-img"><img src="assets/cat_cars.png" alt="Car"></div>
    # <h5>Lamborghini Revuelto</h5>
    
    pattern = r'(<div class="grid-img"><img src=")[^"]*(" alt="[^"]*"></div>\s*<h5>' + re.escape(name) + r'</h5>)'
    return re.sub(pattern, r'\1' + img_url + r'\2', content_str)


for name, url in car_imgs.items():
    content = replace_top_listing_bg(name, url, content)
    content = replace_grid_listing_img(name, url, content)

for name, url in yacht_imgs.items():
    content = replace_top_listing_bg(name, url, content)
    content = replace_grid_listing_img(name, url, content)
    
for name, url in jet_imgs.items():
    content = replace_top_listing_bg(name, url, content)
    content = replace_grid_listing_img(name, url, content)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Images replaced in HTML successfully")
