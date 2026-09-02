# -*- coding: utf-8 -*-
"""
Full Generator for 13 World-Class Luxury Resort Articles.
Ensures ~2,000 words per article (approx 9,000 - 14,000 characters).
"""

import json
import re

def render_article_html(lead_p, quote, takeaways, chapters, verdict_table, author_concl):
    takeaways_html = "".join([f"<li><strong>{k}:</strong> {v}</li>" for k, v in takeaways])
    
    table_rows = "".join([
        f"<tr><td style='padding: 12px 14px; border-bottom: 1px solid #eee; font-weight:600;'>{row[0]}</td>"
        f"<td style='padding: 12px 14px; border-bottom: 1px solid #eee;'>{row[1]}</td>"
        f"<td style='padding: 12px 14px; border-bottom: 1px solid #eee; color:#d4af37; font-weight:700;'>{row[2]}</td></tr>"
        for row in verdict_table
    ])
    
    chapters_html = ""
    for title, content in chapters:
        chapters_html += f"<h2>{title}</h2>\n{content}\n"
        
    return f"""
<div class="article-lead-container">
    {lead_p}
</div>

<blockquote class="pull-quote">
    "{quote}"
</blockquote>

<div class="key-takeaways">
    <h3>Đặc Quyền & Dấu Ấn Nổi Bật</h3>
    <ul>
        {takeaways_html}
    </ul>
</div>

{chapters_html}

<h2>Bảng Đánh Giá & Thẩm Định Chi Tiết Từ Huỳnh Hoàng Thịnh</h2>
<div style="overflow-x: auto; margin: 30px 0;">
    <table style="width: 100%; border-collapse: collapse; text-align: left; font-size: 0.95rem; background: #fafafa; border-radius: 8px; overflow: hidden; border: 1px solid #eee;">
        <thead>
            <tr style="background: #111; color: #fff;">
                <th style="padding: 12px 14px; width: 25%;">Hạng Mục Thẩm Định</th>
                <th style="padding: 12px 14px; width: 55%;">Đặc Điểm Trải Nghiệm & Tiêu Chuẩn</th>
                <th style="padding: 12px 14px; width: 20%;">Điểm Số</th>
            </tr>
        </thead>
        <tbody>
            {table_rows}
        </tbody>
    </table>
</div>

<div class="author-conclusion" style="background: #fdfbf7; border-left: 4px solid #c9a96e; padding: 20px 24px; margin: 40px 0; border-radius: 0 8px 8px 0;">
    <h3 style="font-family: var(--font-serif); margin-bottom: 10px; color: #111;">Lời Kết Từ Người Giám Tuyển Xa Xỉ Huỳnh Hoàng Thịnh</h3>
    {author_concl}
</div>
"""

# Let's import part1 and part2
print("Engine ready.")
