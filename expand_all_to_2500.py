import json, re

def count_words(html_str):
    text = re.sub(r'<[^>]+>', ' ', html_str)
    return len(text.split())

with open('data/posts.json', 'r', encoding='utf-8') as f:
    posts = json.load(f)

# Common helper function to generate massive, deep, intellectual chapters
def generate_deep_essay(base_data, specific_chapters):
    content = f"""
<p class="magazine-dropcap">{base_data['intro']}</p>

<figure class="magazine-figure">
  <img src="{base_data['image']}" alt="{base_data['title']}" loading="lazy">
  <figcaption class="magazine-figcaption">{base_data['caption']}</figcaption>
</figure>

<div class="key-takeaways">
  <h3>Những Luận Điểm Cốt Lõi & Số Liệu Định Lượng Trọng Tâm (The Wealth Report 2026)</h3>
  <ul>
    {base_data['takeaways']}
  </ul>
</div>

<h2>Chương I: Bối Cảnh Lịch Sử & Sự Chuyển Dịch Cấu Trúc Toàn Cầu (2007 – 2026)</h2>
{specific_chapters['ch1']}

<h2>Chương II: Phân Tích Chuyên Sâu Dữ Liệu Kinh Tế & Mô Hình Định Lượng</h2>
{specific_chapters['ch2']}

<h2>Chương III: So Sánh Các Thị Trường Trọng Điểm & Dòng Chảy Vốn Quốc Tế</h2>
{specific_chapters['ch3']}

<h2>Chương IV: Góc Nhìn Đại Chúng: Làn Sóng Phản Biện Xã Hội Học & Đạo Đức Học Của Sự Tích Sản</h2>
{specific_chapters['ch4']}

<h2>Chương V: Chiến Lược Quản Trị Rủi Ro & Khuyến Nghị Tích Sản Dành Cho Giới Tinh Hoa</h2>
{specific_chapters['ch5']}

<h2>Chương VI: Tầm Nhìn Chiến Lược 2026 – 2035 & Giá Trị Di Sản Bền Vững</h2>
{specific_chapters['ch6']}

<div class="magazine-quote">"{base_data['quote']}" — Huỳnh Hoàng Thịnh</div>
"""
    return content

# We will define rich content for each of the 10 articles
# Let's craft them with massive length to exceed 2500 words per article.

print("Crafting comprehensive essays for all 10 posts...")
