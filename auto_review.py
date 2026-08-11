import json
from bs4 import BeautifulSoup
import urllib.request
import urllib.error
import re
from collections import Counter

html_file = "/Users/kenhuynh/.gemini/antigravity-ide/scratch/huynh-hoang-thinh-website/index.html"

with open(html_file, "r", encoding="utf-8") as f:
    html = f.read()

soup = BeautifulSoup(html, "html.parser")

img_urls = []
for img in soup.find_all("img"):
    src = img.get("src")
    if src: img_urls.append(("img_src", src))

for tag in soup.find_all(style=True):
    style = tag.get("style")
    m = re.search(r"url\(['\"]?(.*?)['\"]?\)", style)
    if m:
        img_urls.append(("bg_image", m.group(1)))

errors = []
unique_urls = set()

for typ, url in img_urls:
    unique_urls.add(url)
    
    # check for obvious html entities issue
    if "&amp;" in url:
        errors.append(f"Contains &amp; -> {url}")
        
    if not url.startswith("http") and not url.startswith("assets/"):
        errors.append(f"Invalid URL format -> {url}")

print(f"Total image references found: {len(img_urls)}")
print(f"Total unique images: {len(unique_urls)}")
if errors:
    print("Errors found:")
    for e in errors: print(e)
else:
    print("No obvious format errors in URLs.")
    
# Let's count duplicates to see if Tạp Chí / Tin Tức are still using same images
url_counts = Counter([u for t, u in img_urls if u.startswith("http")])
duplicates = {u: c for u, c in url_counts.items() if c > 1}
if duplicates:
    print(f"Found {len(duplicates)} URLs used more than once. (Could be normal if same posts are shown twice, e.g. top-listing vs grid, or editorial vs news).")
    for u, c in duplicates.items():
        pass # print(f"{u}: {c} times")

print("Validating a sample of 5 Unsplash URLs...")
sample = [u for t, u in img_urls if "unsplash.com" in u][:5]
for u in sample:
    try:
        req = urllib.request.Request(u, headers={'User-Agent': 'Mozilla/5.0'})
        res = urllib.request.urlopen(req)
        print(f"[OK] {u} - {res.status} {res.headers.get('Content-Type')}")
    except Exception as e:
        print(f"[FAIL] {u} - {e}")
