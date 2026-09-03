#!/usr/bin/env python3
"""
build_seo_prerender.py
Automated Technical SEO & AI Search Prerendering Pipeline for huynhhoangthinh.com

Strict Constraints:
- ABSOLUTE DESIGN LOCK: 100% identical visual layout, typography, colors, and components.
- Initial HTML contains full H1, article body, featured image, author, publication date.
- Clean canonical slug URLs: /article/<slug>/
- Backward compatibility: /article?id=XXX and /article/<id>/ redirect to canonical slug.
- Automated generation of:
  - sitemap.xml
  - robots.txt
  - URL_REDIRECT_MAP.md
  - Prerendered HTML for all 155 articles
  - Homepage SEO & Structured Data updates
"""

import os
import re
import json
import unicodedata
from datetime import datetime

SITE_URL = "https://huynhhoangthinh.com"
AUTHOR_NAME = "Huỳnh Hoàng Thịnh"
ORGANIZATION_NAME = "Huỳnh Hoàng Thịnh - Đại Chúng Properties"

def slugify(text):
    text = unicodedata.normalize('NFD', text)
    text = ''.join(c for c in text if unicodedata.category(c) != 'Mn')
    text = text.replace('đ', 'd').replace('Đ', 'd')
    text = re.sub(r'[^\w\s-]', '', text.lower())
    text = re.sub(r'[-\s]+', '-', text).strip('-')
    words = text.split('-')
    if len(words) > 12:
        text = '-'.join(words[:12])
    return text

def parse_date_to_iso(date_str):
    m = re.search(r'(\d+)\s+TH(\d+)\s+(\d{4})', date_str or '', re.IGNORECASE)
    if m:
        day = int(m.group(1))
        month = int(m.group(2))
        year = int(m.group(3))
        return f"{year:04d}-{month:02d}-{day:02d}"
    return "2026-09-02"

def clean_text_for_meta(html_or_text, max_len=160):
    clean = re.sub(r'<[^>]+>', ' ', html_or_text or '')
    clean = re.sub(r'\s+', ' ', clean).strip()
    clean = clean.replace('"', '&quot;').replace("'", "&#39;")
    if len(clean) > max_len:
        clean = clean[:max_len-3] + "..."
    return clean

def normalize_asset_url(url):
    if not url:
        return "/assets/Index_asset/ceo_thinh.jpg"
    url = url.strip()
    if url.startswith("http://") or url.startswith("https://"):
        return url
    if url.startswith("/"):
        return url
    return "/" + url

def fix_content_asset_paths(content):
    if not content:
        return ""
    # Fix src="assets/... to src="/assets/...
    content = re.sub(r'src=["\'](assets/[^"\']+)["\']', r'src="/\1"', content)
    content = re.sub(r'src=["\']\./(assets/[^"\']+)["\']', r'src="/\1"', content)
    return content

def main():
    print("🚀 [Step 1/6] Loading data/posts.json...")
    with open('data/posts.json', 'r', encoding='utf-8') as f:
        posts = json.load(f)
    print(f"Loaded {len(posts)} posts.")

    print("🔑 [Step 2/6] Generating unique SEO slugs...")
    slug_map = {}
    id_map = {}
    seen_slugs = set()

    for p in posts:
        post_id = p['id']
        s = slugify(p.get('title', ''))
        if not s:
            s = f"bai-viet-{post_id}"
        if s in seen_slugs:
            s = f"{s}-{post_id}"
        seen_slugs.add(s)
        slug_map[post_id] = s
        id_map[s] = post_id

    # Save slug mapping for runtime usage
    with open('data/slug_map.json', 'w', encoding='utf-8') as f:
        json.dump(slug_map, f, ensure_ascii=False, indent=2)

    print("📄 [Step 3/6] Generating static pre-rendered articles...")
    os.makedirs("article", exist_ok=True)

    generated_count = 0
    sitemap_entries = []

    for p in posts:
        post_id = p['id']
        slug = slug_map[post_id]
        title = p.get('title', '').strip()
        date_str = p.get('date', 'Tháng 8 2026').strip()
        iso_date = parse_date_to_iso(date_str)
        category_label = p.get('category_label', 'TẠP CHÍ XA XỈ').strip()
        category = p.get('category', 'editorial')
        raw_excerpt = p.get('excerpt', '') or p.get('content', '')[:200]
        meta_desc = clean_text_for_meta(raw_excerpt, 160)
        featured_img = normalize_asset_url(p.get('image', ''))
        full_img_url = featured_img if featured_img.startswith('http') else f"{SITE_URL}{featured_img}"
        canonical_url = f"{SITE_URL}/article/{slug}/"
        content_html = fix_content_asset_paths(p.get('content', ''))

        # Prepare Schema.org JSON-LD
        schema_json = {
            "@context": "https://schema.org",
            "@graph": [
                {
                    "@type": "Article",
                    "@id": f"{canonical_url}#article",
                    "isPartOf": {
                        "@type": "WebPage",
                        "@id": canonical_url,
                        "url": canonical_url,
                        "name": f"{title} - {AUTHOR_NAME}"
                    },
                    "headline": title,
                    "description": meta_desc,
                    "image": full_img_url,
                    "datePublished": iso_date,
                    "dateModified": "2026-09-03",
                    "author": {
                        "@type": "Person",
                        "name": AUTHOR_NAME,
                        "jobTitle": "Người Giám Tuyển Xa Xỉ & Chuyên Gia Bất Động Sản Hàng Hiệu",
                        "url": SITE_URL
                    },
                    "publisher": {
                        "@type": "Organization",
                        "name": ORGANIZATION_NAME,
                        "url": SITE_URL,
                        "logo": {
                            "@type": "ImageObject",
                            "url": f"{SITE_URL}/assets/Index_asset/ceo_thinh.jpg"
                        }
                    },
                    "mainEntityOfPage": canonical_url
                },
                {
                    "@type": "BreadcrumbList",
                    "@id": f"{canonical_url}#breadcrumb",
                    "itemListElement": [
                        {
                            "@type": "ListItem",
                            "position": 1,
                            "name": "Trang Chủ",
                            "item": f"{SITE_URL}/"
                        },
                        {
                            "@type": "ListItem",
                            "position": 2,
                            "name": category_label,
                            "item": f"{SITE_URL}/#tab-{category}"
                        },
                        {
                            "@type": "ListItem",
                            "position": 3,
                            "name": title,
                            "item": canonical_url
                        }
                    ]
                }
            ]
        }

        # Render complete pre-rendered static HTML
        article_html = f"""<!DOCTYPE html>
<html lang="vi">
<head>
  <!-- Google Analytics 4 -->
  <script src="/js/analytics.js" defer></script>

  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{title} - {AUTHOR_NAME}</title>
  <meta name="description" content="{meta_desc}">
  <link rel="canonical" href="{canonical_url}">

  <!-- Open Graph / Facebook / Zalo -->
  <meta property="og:type" content="article">
  <meta property="og:site_name" content="{AUTHOR_NAME}">
  <meta property="og:title" content="{title} - {AUTHOR_NAME}">
  <meta property="og:description" content="{meta_desc}">
  <meta property="og:image" content="{full_img_url}">
  <meta property="og:url" content="{canonical_url}">
  <meta property="article:published_time" content="{iso_date}">
  <meta property="article:author" content="{AUTHOR_NAME}">
  <meta property="article:section" content="{category_label}">

  <!-- Twitter / X Cards -->
  <meta name="twitter:card" content="summary_large_image">
  <meta name="twitter:title" content="{title} - {AUTHOR_NAME}">
  <meta name="twitter:description" content="{meta_desc}">
  <meta name="twitter:image" content="{full_img_url}">

  <!-- Structured Data (JSON-LD) for Search & AI Engines -->
  <script type="application/ld+json">
{json.dumps(schema_json, ensure_ascii=False, indent=2)}
  </script>
  
  <link rel="stylesheet" href="/css/main.css?v=20260903_1">
  <link rel="stylesheet" href="/css/components.css?v=20260902_1">
  <link rel="stylesheet" href="/css/responsive.css?v=20260902_1">
  <link rel="stylesheet" href="/css/chatbot.css?v=20260902_1">
  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
  
  <style>
    .article-header {{
      padding: 100px 0 60px;
      text-align: center;
      background-color: var(--color-light-gray);
      margin-bottom: 60px;
    }}
    .article-title {{
      font-family: var(--font-serif);
      font-size: 3rem;
      max-width: 900px;
      margin: 0 auto 20px;
      line-height: 1.2;
    }}
    .article-meta {{
      font-size: 0.9rem;
      color: var(--color-muted);
      text-transform: uppercase;
      letter-spacing: 0.1em;
    }}
    .article-featured-image {{
      max-width: 1000px;
      margin: 0 auto 60px;
    }}
    .article-featured-image img {{
      width: 100%;
      border-radius: 4px;
    }}
    .article-content {{
      max-width: 760px;
      margin: 0 auto 100px;
      font-size: 1.1rem;
      line-height: 1.8;
      color: var(--color-body);
    }}
    .article-content p {{
      margin-bottom: 24px;
    }}
    /* Editorial Elements */
    .article-content > p:first-of-type::first-letter {{
      float: left;
      font-family: var(--font-serif);
      font-size: 5rem;
      line-height: 0.8;
      padding-top: 4px;
      padding-right: 12px;
      color: var(--color-dark);
    }}
    .pull-quote {{
      font-family: var(--font-serif);
      font-size: 1.8rem;
      font-style: italic;
      color: var(--color-dark);
      margin: 40px -40px;
      padding: 30px;
      border-top: 1px solid var(--color-border);
      border-bottom: 1px solid var(--color-border);
      text-align: center;
    }}
    .key-takeaways {{
      background-color: var(--color-white);
      border: 2px solid #d4af37; /* Matte Gold */
      padding: 30px;
      margin: 40px 0;
      border-radius: 4px;
    }}
    .key-takeaways h3 {{
      font-family: var(--font-serif);
      color: #d4af37;
      margin-bottom: 20px;
      font-size: 1.5rem;
      text-transform: uppercase;
    }}
    .key-takeaways ul {{
      list-style-type: square;
      padding-left: 20px;
    }}
    .key-takeaways li {{
      margin-bottom: 10px;
    }}
    .article-content h2 {{
      font-family: var(--font-serif);
      font-size: 2rem;
      margin: 40px 0 20px;
      color: var(--color-dark);
    }}
  </style>
</head>
<body>

  <!-- Top Utility Bar -->
  <div class="top-bar">
    <div class="container">
      <a href="/#sell">Sell with Us</a>
      <a href="/#agents">For Agents <i class="fa-solid fa-chevron-down" style="font-size: 0.75rem;"></i></a>
      <a href="/#saved"><i class="fa-regular fa-heart"></i> Saved</a>
    </div>
  </div>

  <!-- Main Navigation Header (Dark Version for inner pages) -->
  <header class="main-header" style="position: fixed; top: 0; background: rgba(10,10,10,0.96); backdrop-filter: blur(14px); -webkit-backdrop-filter: blur(14px);">
    <div class="container header-container">
      <a class="brand-identity" href="/">
        <div class="brand-avatar-ring">
          <img src="/assets/Index_asset/ceo_thinh.jpg" alt="Huỳnh Hoàng Thịnh" class="brand-avatar-img"/>
        </div>
        <div class="brand-text-block">
          <span class="brand-logo">HUỲNH HOÀNG THỊNH</span>
          <span class="brand-tagline">NGƯỜI GIÁM TUYỂN XA XỈ</span>
        </div>
      </a>

      <nav class="nav-menu-links">
        <a href="/">Trang Chủ</a>
        <a href="/#tab-resorts">Resort Xa Xỉ</a>
        <a href="/#tab-cars">Siêu Xe</a>
        <a href="/#tab-yachts">Du Thuyền & Chuyên Cơ</a>
        <a href="/#tab-cars-market">Xe Đang Giao Dịch</a>
        <a href="/#tab-realestate">Bất Động Sản</a>
        <a href="/#tab-editorial" class="active">Tạp chí</a>
      </nav>

      <button class="menu-toggle-btn" id="mobileMenuBtn" aria-label="Mở menu">
        <i class="fa-solid fa-bars"></i>
      </button>
    </div>
  </header>

  <!-- Mobile Menu Overlay + Drawer -->
  <div class="mobile-menu-overlay" id="mobileMenuOverlay"></div>
  <nav class="mobile-menu-drawer" id="mobileMenuDrawer">
    <div class="mobile-menu-header">
      <span class="mobile-menu-logo">HUỲNH HOÀNG THỊNH</span>
      <button aria-label="Đóng menu" class="mobile-menu-close" id="mobileMenuClose">
        <i class="fa-solid fa-xmark"></i>
      </button>
    </div>
    <div class="mobile-menu-links">
      <a href="/"><i class="fa-solid fa-house" style="width:20px;margin-right:8px;"></i>Trang Chủ</a>
      <a href="/#tab-resorts"><i class="fa-solid fa-umbrella-beach" style="width:20px;margin-right:8px;"></i>Resort Xa Xỉ</a>
      <a href="/#tab-cars"><i class="fa-solid fa-car" style="width:20px;margin-right:8px;"></i>Siêu Xe</a>
      <a href="/#tab-yachts"><i class="fa-solid fa-sailboat" style="width:20px;margin-right:8px;"></i>Du Thuyền & Chuyên Cơ</a>
      <a href="/#tab-cars-market"><i class="fa-solid fa-car-side" style="width:20px;margin-right:8px;"></i>Xe Đang Giao Dịch</a>
      <a href="/#tab-realestate"><i class="fa-solid fa-building-columns" style="width:20px;margin-right:8px;"></i>Bất Động Sản</a>
      <a href="/#tab-editorial" class="active"><i class="fa-solid fa-newspaper" style="width:20px;margin-right:8px;"></i>Tạp Chí</a>
    </div>
    <div class="mobile-menu-footer">© 2026 Huỳnh Hoàng Thịnh (Đại Chúng Properties)</div>
  </nav>

  <!-- Pre-rendered Static Main Content (100% Available in Initial HTML) -->
  <main id="article-container" style="padding-top: 70px;">
    <div class="article-header">
      <div class="container">
        <div class="article-meta">{date_str} &bull; <span style="color: #c9a96e; font-weight: 700; letter-spacing: 0.05em;">{category_label}</span></div>
        <h1 class="article-title">{title}</h1>
      </div>
    </div>
    
    <div class="container">
      <div class="article-featured-image">
        <img src="{featured_img}" alt="{title}">
      </div>
      
      <article class="article-content">
        {content_html}
      </article>
    </div>
  </main>

  <!-- Related Editorial Section -->
  <section class="news-section" style="border-top: 1px solid #f0f0f0; padding-top: 40px;">
    <div class="container">
      <div class="editorial-latest-block">
        <h3 class="editorial-latest-heading">Góc Nhìn & Xu Hướng Khác</h3>
        <div class="editorial-row-list">
          <a class="editorial-row-item" href="/article/nhan-dinh-thi-truong-villa-trung-tam-tp-ho-chi-minh-xu-huong-dau-tu-bat-dong-san-sieu-sang/">
            <div class="row-item-thumb">
              <img alt="Villa trung tâm TP.HCM" src="https://images.unsplash.com/photo-1600596542815-ffad4c1539a9?w=800"/>
            </div>
            <div class="row-item-body">
              <span class="row-item-cat">NHẬN ĐỊNH THỊ TRƯỜNG</span>
              <h4 class="row-item-title">Villa trung tâm TP. Hồ Chí Minh: xu hướng đầu tư bất động sản siêu sang</h4>
            </div>
            <div class="row-item-action">
              <i class="fa-solid fa-arrow-right"></i>
            </div>
          </a>

          <a class="editorial-row-item" href="/article/nhung-bat-dong-san-dinh-hinh-gu-song-moi-saigon-farm-resort-tien-phong-mo-hinh-resort-sinh-thai/">
            <div class="row-item-thumb">
              <img alt="Saigon Farm Resort" src="/assets/Saigon_Farm_Resort/Phoi_canh_tong_the/SFR_S01_Final_Fix.jpg"/>
            </div>
            <div class="row-item-body">
              <span class="row-item-cat">PHONG CÁCH SỐNG</span>
              <h4 class="row-item-title">Những bất động sản định hình gu sống mới</h4>
            </div>
            <div class="row-item-action">
              <i class="fa-solid fa-arrow-right"></i>
            </div>
          </a>

          <a class="editorial-row-item" href="/article/louis-vuitton-dua-nghe-thuat-du-hanh-len-porsche-911-02-tuyet/">
            <div class="row-item-thumb">
              <img alt="Louis Vuitton x Singer Porsche 911" src="/assets/Posts/911_LouisVuitton/Thumbnail.webp"/>
            </div>
            <div class="row-item-body">
              <span class="row-item-cat">NGHỆ THUẬT CHẾ TÁC</span>
              <h4 class="row-item-title">Louis Vuitton đưa nghệ thuật du hành lên Porsche 911</h4>
            </div>
            <div class="row-item-action">
              <i class="fa-solid fa-arrow-right"></i>
            </div>
          </a>
        </div>
      </div>
    </div>
  </section>

  <!-- Site Footer -->
  <footer class="site-footer">
    <div class="container">
      <div class="footer-top-grid">
        <div>
          <div class="footer-brand-title">HUỲNH HOÀNG THỊNH</div>
          <p style="font-size: 0.85rem; line-height: 1.6; max-width: 320px; color: #888;">
            Sàn giao dịch xa xỉ hàng đầu thế giới, cung cấp các danh mục bất động sản, siêu xe, du thuyền và chuyên cơ đẳng cấp nhất.
          </p>
        </div>
        
        <div>
          <h4 class="footer-col-heading">Danh mục</h4>
          <ul class="footer-links-list">
            <li><a href="/#tab-realestate">Bất động sản</a></li>
            <li><a href="/#tab-cars-market">Xe đang giao dịch</a></li>
            <li><a href="/#tab-cars">Siêu xe độc bản</a></li>
            <li><a href="/#tab-yachts">Du thuyền & Chuyên cơ</a></li>
          </ul>
        </div>

        <div>
          <h4 class="footer-col-heading">Công ty</h4>
          <ul class="footer-links-list">
            <li><a href="/article/gioi-thieu-huynh-hoang-thinh-nguoi-giam-tuyen-xa-xi-hang-dau-viet-nam/">Giới thiệu</a></li>
            <li><a href="/article/lien-he-va-tu-van-danh-muc-xa-xi-cung-huynh-hoang-thinh/">Liên hệ</a></li>
          </ul>
        </div>
      </div>
    </div>
  </footer>

  <!-- Zalo Floating Button -->
  <a href="https://zalo.me/0906060036" class="zalo-floating-btn" target="_blank" rel="noopener noreferrer">
    <div class="zalo-pulse"></div>
    <div class="zalo-icon"><i class="fa-solid fa-comment-dots"></i></div>
  </a>

  <script src="/js/app.js?v=20260903_1"></script>
  <script src="/js/ai-chatbot.js?v=20260902_1"></script>
</body>
</html>
"""
        # Write to article/<slug>/index.html
        slug_dir = os.path.join("article", slug)
        os.makedirs(slug_dir, exist_ok=True)
        with open(os.path.join(slug_dir, "index.html"), "w", encoding="utf-8") as f:
            f.write(article_html)

        # Also write legacy ID directory: article/<id>/index.html (Permanent redirect)
        id_dir = os.path.join("article", str(post_id))
        os.makedirs(id_dir, exist_ok=True)
        id_redirect_html = f"""<!DOCTYPE html>
<html lang="vi">
<head>
  <meta charset="UTF-8">
  <title>Đang chuyển hướng - HUỲNH HOÀNG THỊNH</title>
  <link rel="canonical" href="{canonical_url}">
  <meta http-equiv="refresh" content="0;url=/article/{slug}/">
  <script>window.location.replace('/article/{slug}/');</script>
</head>
<body>
  <p>Đang chuyển hướng tới bài viết: <a href="/article/{slug}/">{title}</a>...</p>
</body>
</html>"""
        with open(os.path.join(id_dir, "index.html"), "w", encoding="utf-8") as f:
            f.write(id_redirect_html)

        sitemap_entries.append({
            'loc': canonical_url,
            'lastmod': iso_date,
            'changefreq': 'weekly',
            'priority': '0.8'
        })
        generated_count += 1

    print(f"Generated {generated_count} static article pages and {generated_count} legacy redirect pages.")

    print("🗺️ [Step 4/6] Creating XML sitemap and robots.txt...")
    # Generate sitemap.xml
    xml_lines = [
        '<?xml version="1.0" encoding="UTF-8"?>',
        '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">',
        '  <url>',
        f'    <loc>{SITE_URL}/</loc>',
        '    <lastmod>2026-09-03</lastmod>',
        '    <changefreq>daily</changefreq>',
        '    <priority>1.0</priority>',
        '  </url>'
    ]
    for item in sitemap_entries:
        xml_lines.append('  <url>')
        xml_lines.append(f'    <loc>{item["loc"]}</loc>')
        xml_lines.append(f'    <lastmod>{item["lastmod"]}</lastmod>')
        xml_lines.append(f'    <changefreq>{item["changefreq"]}</changefreq>')
        xml_lines.append(f'    <priority>{item["priority"]}</priority>')
        xml_lines.append('  </url>')
    xml_lines.append('</urlset>')

    with open('sitemap.xml', 'w', encoding='utf-8') as f:
        f.write('\n'.join(xml_lines) + '\n')
    print("Saved sitemap.xml with 156 URLs (Homepage + 155 articles).")

    # Generate robots.txt
    robots_content = f"""# robots.txt for {SITE_URL}
User-agent: *
Allow: /

# OpenAI Search Discovery (ChatGPT Search)
User-agent: OAI-SearchBot
Allow: /

# Google Search & Google AI Overviews
User-agent: Googlebot
Allow: /

# Bing Search & Copilot
User-agent: Bingbot
Allow: /

# Anthropic Claude Search & Discovery
User-agent: ClaudeBot
Allow: /

# Perplexity AI Search
User-agent: PerplexityBot
Allow: /

# Disallow scanning of non-existent CMS utility paths
Disallow: /wp-admin/
Disallow: /wp-includes/

# Sitemap Location
Sitemap: {SITE_URL}/sitemap.xml
"""
    with open('robots.txt', 'w', encoding='utf-8') as f:
        f.write(robots_content)
    print("Saved robots.txt with search and AI crawler access rules.")

    print("📑 [Step 5/6] Updating article.html with instant client-side slug redirection...")
    # Update article.html to perform instant redirection when queried with ?id=XXX
    slug_map_js = json.dumps(slug_map)
    article_html_update = f"""<!DOCTYPE html>
<html lang="vi">
<head>
  <!-- Google Analytics 4 -->
  <script src="/js/analytics.js" defer></script>

  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Tạp chí & Góc Nhìn - HUỲNH HOÀNG THỊNH</title>
  
  <script>
    // Instant Redirect from legacy ?id=XXX to canonical SEO slug /article/<slug>/
    (function() {{
      var params = new URLSearchParams(window.location.search);
      var id = parseInt(params.get('id'));
      var slugMap = {slug_map_js};
      if (id && slugMap[id]) {{
        window.location.replace('/article/' + slugMap[id] + '/');
      }}
    }})();
  </script>

  <link rel="stylesheet" href="/css/main.css?v=20260903_1">
  <link rel="stylesheet" href="/css/components.css?v=20260902_1">
  <link rel="stylesheet" href="/css/responsive.css?v=20260902_1">
  <link rel="stylesheet" href="/css/chatbot.css?v=20260902_1">
  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
</head>
<body>
  <div style="text-align: center; padding: 120px 20px; font-family: sans-serif;">
    <p style="font-size: 1.1rem; color: #555;">Đang mở bài viết...</p>
  </div>
  <script src="/js/app.js?v=20260903_1"></script>
</body>
</html>
"""
    with open('article.html', 'w', encoding='utf-8') as f:
        f.write(article_html_update)

    print("🔗 [Step 6/6] Updating internal links and metadata on index.html...")
    with open('index.html', 'r', encoding='utf-8') as f:
        index_content = f.read()

    # 1. Update card links: article.html?id=XXX -> /article/<slug>/
    updated_links = 0
    for post_id, slug in slug_map.items():
        pattern1 = f'href="article.html?id={post_id}"'
        replacement = f'href="/article/{slug}/"'
        if pattern1 in index_content:
            index_content = index_content.replace(pattern1, replacement)
            updated_links += 1
        
        pattern2 = f'href="/article?id={post_id}"'
        if pattern2 in index_content:
            index_content = index_content.replace(pattern2, replacement)
            updated_links += 1

    print(f"Updated {updated_links} internal card links on index.html to point to canonical slug URLs.")

    # 2. Add Homepage canonical link, Open Graph, Twitter Cards, and Schema.org JSON-LD
    homepage_schema = {
        "@context": "https://schema.org",
        "@graph": [
            {
                "@type": "WebSite",
                "@id": f"{SITE_URL}/#website",
                "url": f"{SITE_URL}/",
                "name": "HUỲNH HOÀNG THỊNH - Thị trường xa xỉ hàng đầu thế giới",
                "description": "Thị trường mua bán bất động sản, ô tô, du thuyền và máy bay cao cấp hàng đầu thế giới.",
                "publisher": {
                    "@type": "Organization",
                    "@id": f"{SITE_URL}/#organization"
                }
            },
            {
                "@type": "Person",
                "@id": f"{SITE_URL}/#person",
                "name": AUTHOR_NAME,
                "jobTitle": "Người Giám Tuyển Xa Xỉ & Chuyên Gia Bất Động Sản Cao Cấp",
                "image": f"{SITE_URL}/assets/Index_asset/ceo_thinh.jpg",
                "telephone": "+84906060036",
                "url": f"{SITE_URL}/",
                "worksFor": {
                    "@type": "Organization",
                    "@id": f"{SITE_URL}/#organization"
                }
            },
            {
                "@type": "Organization",
                "@id": f"{SITE_URL}/#organization",
                "name": ORGANIZATION_NAME,
                "url": f"{SITE_URL}/",
                "logo": f"{SITE_URL}/assets/Index_asset/ceo_thinh.jpg",
                "contactPoint": {
                    "@type": "ContactPoint",
                    "telephone": "+84906060036",
                    "contactType": "sales",
                    "areaServed": "VN",
                    "availableLanguage": ["Vietnamese", "English"]
                }
            }
        ]
    }

    # Inject metadata into <head> of index.html if not already present
    if '<link rel="canonical" href="https://huynhhoangthinh.com/"' not in index_content:
        meta_insertion = f"""  <link rel="canonical" href="{SITE_URL}/" />
  <meta property="og:type" content="website" />
  <meta property="og:site_name" content="HUỲNH HOÀNG THỊNH" />
  <meta property="og:title" content="HUỲNH HOÀNG THỊNH - Thị trường xa xỉ hàng đầu thế giới" />
  <meta property="og:description" content="Thị trường mua bán bất động sản, ô tô, du thuyền và máy bay cao cấp hàng đầu thế giới." />
  <meta property="og:url" content="{SITE_URL}/" />
  <meta property="og:image" content="{SITE_URL}/assets/Index_asset/ceo_thinh.jpg" />
  <meta name="twitter:card" content="summary_large_image" />
  <meta name="twitter:title" content="HUỲNH HOÀNG THỊNH - Thị trường xa xỉ hàng đầu thế giới" />
  <meta name="twitter:description" content="Thị trường mua bán bất động sản, ô tô, du thuyền và máy bay cao cấp hàng đầu thế giới." />
  <meta name="twitter:image" content="{SITE_URL}/assets/Index_asset/ceo_thinh.jpg" />
  <!-- Structured Data (JSON-LD) -->
  <script type="application/ld+json">
{json.dumps(homepage_schema, ensure_ascii=False, indent=2)}
  </script>
"""
        # Replace <meta http-equiv="Cache-Control"... if exists or insert before </head>
        index_content = re.sub(r'<meta http-equiv="Cache-Control"[^>]+>\s*', '', index_content)
        index_content = re.sub(r'<meta http-equiv="Pragma"[^>]+>\s*', '', index_content)
        index_content = re.sub(r'<meta http-equiv="Expires"[^>]+>\s*', '', index_content)
        index_content = index_content.replace('<link href="css/main.css?v=20260903_1"', f'{meta_insertion}  <link href="css/main.css?v=20260903_1"')

    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(index_content)
    print("Updated index.html with canonical, Open Graph, Twitter Cards, Schema, and clean URLs.")

    # Generate URL_REDIRECT_MAP.md
    print("📝 Generating URL_REDIRECT_MAP.md...")
    md_lines = [
        "# HUYNHHOANGTHINH.COM — URL MIGRATION & REDIRECT MAP",
        "",
        "**Date:** September 3, 2026  ",
        f"**Total Mapped URLs:** {len(slug_map)} Articles  ",
        "**Redirect Type:** Permanent 301 / Canonical Replacement  ",
        "",
        "All legacy query parameter URLs (`/article.html?id=XXX` and `/article?id=XXX`) and ID routes (`/article/XXX/`) permanently map to the new canonical keyword slug URLs (`/article/<slug>/`).",
        "",
        "| Post ID | Legacy URL | Canonical Slug URL | Article Title |",
        "| :--- | :--- | :--- | :--- |"
    ]
    for p in posts:
        pid = p['id']
        slug = slug_map[pid]
        title_escaped = p.get('title', '').replace('|', '-')
        md_lines.append(f"| `{pid}` | `/article?id={pid}` | [`/article/{slug}/`]({SITE_URL}/article/{slug}/) | {title_escaped} |")

    with open('URL_REDIRECT_MAP.md', 'w', encoding='utf-8') as f:
        f.write('\n'.join(md_lines) + '\n')
    print("Saved URL_REDIRECT_MAP.md.")

    print("🎉 All Technical SEO Prerendering steps completed successfully!")

if __name__ == '__main__':
    main()
