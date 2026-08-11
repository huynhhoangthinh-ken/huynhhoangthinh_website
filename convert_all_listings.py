import json
import re
from bs4 import BeautifulSoup

html_file = "/Users/kenhuynh/.gemini/antigravity-ide/scratch/huynh-hoang-thinh-website/index.html"
posts_file = "/Users/kenhuynh/.gemini/antigravity-ide/scratch/huynh-hoang-thinh-website/data/posts.json"

with open(html_file, "r", encoding="utf-8") as f:
    html_content = f.read()

soup = BeautifulSoup(html_content, "html.parser")

with open(posts_file, "r", encoding="utf-8") as f:
    posts = json.load(f)

# Keep track of existing max ID
max_id = max([p["id"] for p in posts]) if posts else 200
current_id = max_id + 1

new_posts = []

# Templates for detailed articles
article_template = """
<p>{description}. Sự ra đời của kiệt tác này đánh dấu một bước ngoặt mới trong ngành công nghiệp xa xỉ, nơi mọi giới hạn về kỹ thuật và thiết kế đều bị phá vỡ.</p>
<h2>Thiết Kế Vượt Thời Gian</h2>
<p>Mang trong mình DNA đặc trưng, sản phẩm này không chỉ thu hút mọi ánh nhìn mà còn thể hiện gu thẩm mỹ đỉnh cao của chủ nhân. Mọi đường nét đều được tính toán kỹ lưỡng, tối ưu hóa cả về công năng lẫn tính khí động học (hoặc không gian sống). Nội thất bên trong là sự xa hoa không giới hạn với vật liệu thủ công quý hiếm nhất.</p>
<img src="{img_src}" alt="Hình ảnh thực tế" style="width:100%; border-radius:12px; margin: 30px 0;">
<h2>Trải Nghiệm Cảm Xúc Tuyệt Đối</h2>
<p>Sở hữu siêu phẩm này đồng nghĩa với việc bạn đang nắm trong tay tấm vé bước vào một thế giới đặc quyền. Không chỉ là cảm giác phấn khích tột độ khi vận hành, hay sự yên bình thư thái trong không gian riêng tư, mà còn là sự tự hào khi sở hữu một tài sản vô giá mang tính biểu tượng.</p>
<div class="key-takeaways">
  <h3>Chi Tiết & Thông Số Kỹ Thuật</h3>
  <ul>
    <li>Thương hiệu / Nhà phát triển danh tiếng hàng đầu thế giới.</li>
    <li>Mức độ cá nhân hóa (Bespoke) lên tới 100% theo yêu cầu của khách hàng.</li>
    <li>Vật liệu: Sợi carbon, hợp kim nhẹ hàng không, gỗ quý và da thật cao cấp.</li>
    <li>Dịch vụ hậu mãi và bảo hành toàn cầu chuẩn VVIP 24/7.</li>
  </ul>
</div>
"""

# Process Tab 2 (Cars) and Tab 3 (Yachts & Jets)
# We only want to convert the ones that are still divs, not anchor tags.
# Wait, some real estate ones might already be 'a' tags from my previous script.

def process_listings(tab_id):
    global current_id
    tab = soup.find(id=tab_id)
    if not tab: return

    # Process top-listing-card
    for card in tab.find_all(["div", "a"], class_="top-listing-card"):
        # If it's already an 'a' tag, maybe skip or rewrite href
        title_tag = card.find("h4")
        if not title_tag: continue
        title = title_tag.get_text(strip=True)
        
        desc_tag = card.find("p")
        desc = desc_tag.get_text(strip=True) if desc_tag else ""
        
        img_tag = card.find(class_="top-listing-img")
        img_src = ""
        if img_tag and 'style' in img_tag.attrs:
            style = img_tag['style']
            m = re.search(r"url\(['\"]?(.*?)['\"]?\)", style)
            if m: img_src = m.group(1)

        # Check if already has href with id
        if card.name == 'a' and 'href' in card.attrs and 'article.html?id=' in card['href']:
            card_id = int(card['href'].split('=')[-1])
        else:
            card_id = current_id
            current_id += 1
            
            # Convert to anchor
            card.name = 'a'
            card['href'] = f"article.html?id={card_id}"
            card['style'] = card.get('style', '') + " text-decoration: none; color: inherit; display: block;"

        # Append to posts
        new_posts.append({
            "id": card_id,
            "title": title,
            "date": "29 TH8 2026",
            "image": img_src,
            "excerpt": f"{desc}. Siêu phẩm mang tính biểu tượng này là minh chứng rõ ràng nhất cho sự hoàn hảo...",
            "content": article_template.format(description=desc, img_src=img_src)
        })

    # Process grid-card
    for card in tab.find_all(["div", "a"], class_="grid-card"):
        # Note: Editorial grid cards don't matter because this is restricted to tab_id
        title_tag = card.find("h5")
        if not title_tag: continue
        title = title_tag.get_text(strip=True)
        
        img_tag = card.find("img")
        img_src = img_tag['src'] if img_tag else ""
        
        # Get details
        price_tag = card.find(class_="car-price") or card.find("p")
        desc = price_tag.get_text(strip=True) if price_tag else "Siêu phẩm đẳng cấp"

        if card.name == 'a' and 'href' in card.attrs and 'article.html?id=' in card['href']:
            card_id = int(card['href'].split('=')[-1])
        else:
            card_id = current_id
            current_id += 1
            card.name = 'a'
            card['href'] = f"article.html?id={card_id}"
            card['style'] = card.get('style', '') + " text-decoration: none; color: inherit; display: block;"

        new_posts.append({
            "id": card_id,
            "title": title,
            "date": "30 TH8 2026",
            "image": img_src,
            "excerpt": f"Khám phá siêu phẩm {title} với mức giá {desc}. Sự lựa chọn hoàn hảo cho phong cách sống đỉnh cao...",
            "content": article_template.format(description=f"Phiên bản giới hạn với mức giá {desc}", img_src=img_src)
        })

# Process all 3 tabs
process_listings("tab-cars")
process_listings("tab-yachts")

# Write updated HTML
with open(html_file, "w", encoding="utf-8") as f:
    f.write(str(soup))

# Write updated JSON
# Only append new_posts that aren't already in posts
existing_ids = {p["id"] for p in posts}
added = 0
for np in new_posts:
    if np["id"] not in existing_ids:
        posts.append(np)
        added += 1

with open(posts_file, "w", encoding="utf-8") as f:
    json.dump(posts, f, ensure_ascii=False, indent=2)

print(f"Updated index.html to make listings clickable.")
print(f"Appended {added} new product articles to posts.json.")
