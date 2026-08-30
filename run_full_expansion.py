import json, re

def count_words(html_str):
    text = re.sub(r'<[^>]+>', ' ', html_str)
    return len(text.split())

with open('data/posts.json', 'r', encoding='utf-8') as f:
    posts = json.load(f)

# Post 701: Wealth Report Global & Vietnam (>2,500 words)
# Post 702: PIRI 100 Global Luxury Real Estate (>2,500 words)
# Post 703: Family Office Survey 2026 (>2,500 words)
# Post 704: Ultra-Mobility & Branded Residences (>2,500 words)
# Post 705: KFLII Luxury Investment Index (>2,500 words)
# Post 706: Classic Supercars & Halo Cars (>2,500 words)
# Post 707: Superyacht Market Rebounds 70% (>2,500 words)
# Post 708: Private Jets & Multi-Location Living (>2,500 words)
# Post 709: Global Vineyard Index (>2,500 words)
# Post 710: Commercial Real Estate & AI Data Centers (>2,500 words)

print("Starting generation...")
