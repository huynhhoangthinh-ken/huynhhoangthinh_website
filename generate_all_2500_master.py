import json, re

def count_words(html_str):
    text = re.sub(r'<[^>]+>', ' ', html_str)
    return len(text.split())

with open('data/posts.json', 'r', encoding='utf-8') as f:
    posts = json.load(f)

# Helper function to append comprehensive analytical chapters ensuring > 2500 words
def enrich_to_2500_words(article_id, title, category, category_label, price, image, excerpt, main_sections):
    full_content = f"""
<p class="magazine-dropcap">{main_sections['intro']}</p>

<figure class="magazine-figure">
  <img src="{image}" alt="{title}" loading="lazy">
  <figcaption class="magazine-figcaption">{main_sections['caption']}</figcaption>
</figure>

<div class="key-takeaways">
  <h3>Những Luận Điểm Cốt Lõi & Số Liệu Định Lượng Trọng Tâm (The Wealth Report 2026)</h3>
  <ul>
    {main_sections['takeaways']}
  </ul>
</div>

<h2>Chương I: Bối Cảnh Lịch Sử & Sự Chuyển Dịch Cấu Trúc Toàn Cầu 2007 – 2026</h2>
{main_sections['chapter1']}

<h2>Chương II: Phân Tích Chuyên Sâu Dữ Liệu Kinh Tế & Mô Hình Định Lượng</h2>
{main_sections['chapter2']}

<h2>Chương III: So Sánh Các Thị Trường Trọng Điểm & Dòng Chảy Vốn Quốc Tế</h2>
{main_sections['chapter3']}

<h2>Chương IV: Góc Nhìn Đại Chúng: Làn Sóng Phản Biện Xã Hội Học & Đạo Đức Học Của Sự Tích Sản</h2>
{main_sections['chapter4']}

<h2>Chương V: Chiến Lược Quản Trị Rủi Ro & Khuyến Nghị Tích Sản Dành Cho Giới Tinh Hoa</h2>
{main_sections['chapter5']}

<h2>Chương VI: Tầm Nhìn Chiến Lược 2026 – 2035 & Giá Trị Di Sản Bền Vững</h2>
{main_sections['chapter6']}

<div class="magazine-quote">"{main_sections['quote']}" — Huỳnh Hoàng Thịnh</div>
"""
    return {
        "id": article_id,
        "title": title,
        "category": category,
        "category_label": category_label,
        "price": price,
        "image": image,
        "hero_image": image,
        "excerpt": excerpt,
        "content": full_content
    }

# Let's craft the 10 articles with rich multi-page depth
print("Building comprehensive 2500+ words articles...")

