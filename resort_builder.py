# -*- coding: utf-8 -*-
"""
Full generation script for 13 World-Class Luxury Resort Articles for huynhhoangthinh.com.
Each article contains:
- Rich markdown/HTML with drop-caps, quotes, key takeaways, feature breakdowns, architecture & interior review, fine dining & wellness analysis, and rating summary tables.
- Length: ~2,000 to 2,500 words per article.
- Author voice: Huỳnh Hoàng Thịnh - Luxury Curator.
"""

import json
import os

# Helper to build consistent rich article structure
def create_article(id_num, title, excerpt, img_url, country_tag, date_str, sections_html, takeaways, quote, verdict_table):
    takeaways_li = "".join([f"<li><strong>{k}:</strong> {v}</li>" for k, v in takeaways])
    
    table_rows = "".join([
        f"<tr><td style='padding: 10px 14px; border-bottom: 1px solid #eee; font-weight:600;'>{row[0]}</td>"
        f"<td style='padding: 10px 14px; border-bottom: 1px solid #eee;'>{row[1]}</td>"
        f"<td style='padding: 10px 14px; border-bottom: 1px solid #eee; color:#d4af37; font-weight:700;'>{row[2]}</td></tr>"
        for row in verdict_table
    ])
    
    full_content = f"""
<div class="article-lead-container">
    {sections_html['lead']}
</div>

<blockquote class="pull-quote">
    "{quote}"
</blockquote>

<div class="key-takeaways">
    <h3>Đặc Quyền & Dấu Ấn Nổi Bật</h3>
    <ul>
        {takeaways_li}
    </ul>
</div>

{sections_html['body_1']}

{sections_html['body_2']}

{sections_html['body_3']}

{sections_html['body_4']}

<h2>Bảng Đánh Giá & Thẩm Định Chi Tiết Từ Huỳnh Hoàng Thịnh</h2>
<div style="overflow-x: auto; margin: 30px 0;">
    <table style="width: 100%; border-collapse: collapse; text-align: left; font-size: 0.95rem; background: #fafafa; border-radius: 8px; overflow: hidden; border: 1px solid #eee;">
        <thead>
            <tr style="background: #111; color: #fff;">
                <th style="padding: 12px 14px; width: 25%;">Hạng Mục</th>
                <th style="padding: 12px 14px; width: 55%;">Đặc Điểm Trải Nghiệm</th>
                <th style="padding: 12px 14px; width: 20%;">Điểm Đánh Giá</th>
            </tr>
        </thead>
        <tbody>
            {table_rows}
        </tbody>
    </table>
</div>

{sections_html['conclusion']}
"""
    return {
        "id": id_num,
        "title": title,
        "date": date_str,
        "image": img_url,
        "excerpt": excerpt,
        "category": "resort",
        "category_label": f"RESORT XA XỈ • {country_tag.upper()}",
        "content": full_content
    }

print("Generator module loaded.")
