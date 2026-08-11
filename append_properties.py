import json
import os

filepath = "/Users/kenhuynh/.gemini/antigravity-ide/scratch/huynh-hoang-thinh-website/data/posts.json"

with open(filepath, "r", encoding="utf-8") as f:
    posts = json.load(f)

real_estate_html = """
<p>Nằm tại những vị trí đắc địa bậc nhất, đây là những tuyệt tác kiến trúc dành riêng cho giới thượng lưu. Dự án nổi bật với không gian sống được thiết kế tỉ mỉ, kết hợp giữa nghệ thuật đương đại và vật liệu thiên nhiên cao cấp nhất.</p>
<h2>Thiết Kế Độc Bản và Tiện Ích Đỉnh Cao</h2>
<p>Không chỉ sở hữu diện tích rộng rãi, mỗi chi tiết từ nội thất, cảnh quan sân vườn đến hệ thống an ninh 24/7 đều được cá nhân hóa hoàn toàn. Tầm nhìn panorama đắt giá mang lại trải nghiệm sống thư thái, tách biệt khỏi sự ồn ào của phố thị nhưng vẫn nằm ngay tại trái tim của sự tiện nghi.</p>
<img src="{img_src}" alt="Hình ảnh thực tế" style="width:100%; border-radius:12px; margin: 30px 0;">
<h2>Cơ Hội Đầu Tư Không Thể Bỏ Lỡ</h2>
<p>Sở hữu bất động sản siêu sang không chỉ là một biểu tượng của sự thành đạt, mà còn là một kênh đầu tư trú ẩn an toàn và có khả năng sinh lời vượt trội trong tương lai. Sự khan hiếm của những dự án có vị trí "vàng" thế này khiến giá trị của chúng luôn tăng trưởng bất chấp những biến động của thị trường chung.</p>
<div class="key-takeaways">
  <h3>Chi Tiết Bất Động Sản</h3>
  <ul>
    <li>Diện tích sử dụng: Lên đến hơn 1000m2.</li>
    <li>Thiết kế bespoke, vật liệu nhập khẩu 100% từ châu Âu.</li>
    <li>Hệ thống tiện ích nội khu: Rạp chiếu phim riêng, hầm rượu vang, hồ bơi vô cực.</li>
    <li>Hệ sinh thái thông minh (Smart Home) thế hệ mới nhất.</li>
  </ul>
</div>
"""

new_posts = [
    {
        "id": 101,
        "title": "Dinh Thự Đảo Ngọc - Ven Sông Sài Gòn",
        "date": "10 TH8 2026",
        "image": "assets/cat_realestate.png",
        "excerpt": "Ven sông Sài Gòn, Không gian sống tinh hoa. Dinh thự tuyệt đẹp này mang lại sự kết hợp hoàn hảo giữa thiên nhiên và sự hiện đại...",
        "content": real_estate_html.format(img_src="assets/cat_realestate.png")
    },
    {
        "id": 102,
        "title": "Biệt Thự Đỉnh Đồi - Tầm nhìn Panorama",
        "date": "15 TH8 2026",
        "image": "assets/trend_patio.png",
        "excerpt": "Tầm nhìn Panorama, Hồ bơi vô cực. Chiêm ngưỡng kiệt tác kiến trúc hiện đại hòa quyện cùng mảng xanh thiên nhiên rộng lớn...",
        "content": real_estate_html.format(img_src="assets/trend_patio.png")
    },
    {
        "id": 103,
        "title": "Penthouse Độc Bản - Trung Tâm Quận 1",
        "date": "20 TH8 2026",
        "image": "assets/news_resort.png",
        "excerpt": "Trung tâm Q1, Thiết kế Bespoke. Đây không chỉ là nơi an cư, mà còn là sự khẳng định vị thế độc tôn của chủ nhân...",
        "content": real_estate_html.format(img_src="assets/news_resort.png")
    },
    {
        "id": 104,
        "title": "Penthouse The View - Mức Giá $3,200,000",
        "date": "22 TH8 2026",
        "image": "assets/cat_realestate.png",
        "excerpt": "Chỉ với 3.2 triệu USD, bạn sẽ sở hữu một tầm nhìn không giới hạn toàn thành phố từ một căn hộ đẳng cấp...",
        "content": real_estate_html.format(img_src="assets/cat_realestate.png")
    },
    {
        "id": 105,
        "title": "Villa Ngoại Ô - Sự Tĩnh Lặng Trị Giá $2,100,000",
        "date": "25 TH8 2026",
        "image": "assets/trend_patio.png",
        "excerpt": "Nơi để trở về sau những ngày làm việc căng thẳng, một căn Villa sinh thái trị giá 2.1 triệu USD nằm ở ngoại ô thanh bình...",
        "content": real_estate_html.format(img_src="assets/trend_patio.png")
    },
    {
        "id": 106,
        "title": "Resort Ven Biển - Siêu Phẩm Đầu Tư $5,500,000",
        "date": "28 TH8 2026",
        "image": "assets/news_resort.png",
        "excerpt": "Khu nghỉ dưỡng sang trọng ven biển, mang lại lợi suất cao và trải nghiệm nghỉ dưỡng xa xỉ cho những nhà đầu tư tầm cỡ...",
        "content": real_estate_html.format(img_src="assets/news_resort.png")
    }
]

# Check if they exist to avoid duplication if run multiple times
existing_ids = {p["id"] for p in posts}
for np in new_posts:
    if np["id"] not in existing_ids:
        posts.append(np)

with open(filepath, "w", encoding="utf-8") as f:
    json.dump(posts, f, ensure_ascii=False, indent=2)

print("Appended real estate property articles to data/posts.json")
