import json, re

def count_words(html_str):
    text = re.sub(r'<[^>]+>', ' ', html_str)
    return len(text.split())

with open('data/posts.json', 'r', encoding='utf-8') as f:
    posts = json.load(f)

# Helper function to enrich content to guaranteed >= 2500 words
def build_massive_essay(p_id, title, category, category_label, price, image, excerpt, intro, takeaways_list, ch1_title, ch1_body, ch2_title, ch2_body, ch3_title, ch3_body, ch4_title, ch4_body, ch5_title, ch5_body, ch6_title, ch6_body, quote):
    takeaways_html = "".join(f"<li>{item}</li>" for item in takeaways_list)
    
    content = f"""
<p class="magazine-dropcap">{intro}</p>

<figure class="magazine-figure">
  <img src="{image}" alt="{title}" loading="lazy">
  <figcaption class="magazine-figcaption">{title} — Phân tích chuyên sâu từ The Wealth Report 2026 (Knight Frank 20th Edition).</figcaption>
</figure>

<div class="key-takeaways">
  <h3>Những Luận Điểm Cốt Lõi & Số Liệu Định Lượng Trọng Tâm (The Wealth Report 2026)</h3>
  <ul>
    {takeaways_html}
  </ul>
</div>

<h2>Chương I: {ch1_title}</h2>
{ch1_body}

<h2>Chương II: {ch2_title}</h2>
{ch2_body}

<h2>Chương III: {ch3_title}</h2>
{ch3_body}

<h2>Chương IV: {ch4_title}</h2>
{ch4_body}

<h2>Chương V: {ch5_title}</h2>
{ch5_body}

<h2>Chương VI: {ch6_title}</h2>
{ch6_body}

<div class="magazine-quote">"{quote}" — Huỳnh Hoàng Thịnh</div>
"""
    return {
        "id": p_id,
        "title": title,
        "category": category,
        "category_label": category_label,
        "price": price,
        "image": image,
        "hero_image": image,
        "excerpt": excerpt,
        "content": content
    }

print("Script framework ready.")
