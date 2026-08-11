import json
import re
from bs4 import BeautifulSoup
import random

# Clean Unsplash URLs (using only ?w=800 to avoid & and &amp; issues entirely)
img_realestate = [
    "https://images.unsplash.com/photo-1600596542815-ffad4c1539a9?w=800",
    "https://images.unsplash.com/photo-1512917774080-9991f1c4c750?w=800",
    "https://images.unsplash.com/photo-1600607687920-4e2a09be1587?w=800",
    "https://images.unsplash.com/photo-1613490908653-cg7f39b1a7d6?w=800",
    "https://images.unsplash.com/photo-1512918728653-f72023cb5142?w=800",
    "https://images.unsplash.com/photo-1600585154340-be6161a56a0c?w=800",
    "https://images.unsplash.com/photo-1600607687644-aac4c3eac7f4?w=800",
    "https://images.unsplash.com/photo-1580587771525-78b9dba3b914?w=800",
    "https://images.unsplash.com/photo-1600566753190-17f0baa2a6c3?w=800",
    "https://images.unsplash.com/photo-1600047509807-ba8f99d2cdde?w=800",
    "https://images.unsplash.com/photo-1600585154526-990dced4ea0d?w=800",
    "https://images.unsplash.com/photo-1600573472591-ee6981ce35b4?w=800"
]

img_cars = [
    "https://images.unsplash.com/photo-1583121274602-3e2820c69888?w=800",
    "https://images.unsplash.com/photo-1614162692292-7ac56d7f7f1e?w=800",
    "https://images.unsplash.com/photo-1503376713217-1014abfb0c3d?w=800",
    "https://images.unsplash.com/photo-1511919884226-fd3cad34687c?w=800",
    "https://images.unsplash.com/photo-1633503251455-84728565cde9?w=800",
    "https://images.unsplash.com/photo-1605559424843-9e4c228bf1c2?w=800",
    "https://images.unsplash.com/photo-1603584173870-7f23fdae1b7a?w=800",
    "https://images.unsplash.com/photo-1568605114967-8130f3a36e56?w=800",
    "https://images.unsplash.com/photo-1555353540-64580b51c258?w=800",
    "https://images.unsplash.com/photo-1544829099-b9a0c62fad8d?w=800",
    "https://images.unsplash.com/photo-1549317661-bd32c8ce0e78?w=800",
    "https://images.unsplash.com/photo-1552519507-da3b142c6e3d?w=800",
    "https://images.unsplash.com/photo-1502877338535-766e1452684a?w=800",
    "https://images.unsplash.com/photo-1532581140115-3e355d1ed1fd?w=800",
    "https://images.unsplash.com/photo-1563720223185-11003d516935?w=800",
    "https://images.unsplash.com/photo-1614200179396-2bdb77ebf81b?w=800"
]

img_yachts = [
    "https://images.unsplash.com/photo-1569263979104-865ab7cd8d13?w=800",
    "https://images.unsplash.com/photo-1605281317010-fe5ffe798166?w=800",
    "https://images.unsplash.com/photo-1567899378494-47b22a2ae96a?w=800",
    "https://images.unsplash.com/photo-1580983218765-f663ca0e0be0?w=800",
    "https://images.unsplash.com/photo-1599839619722-39751411ea63?w=800",
    "https://images.unsplash.com/photo-1544551763-9b2f5cd9a779?w=800",
    "https://images.unsplash.com/photo-1520630718501-c30985208f6f?w=800",
    "https://images.unsplash.com/photo-1550993517-578f3d1354a9?w=800",
    "https://images.unsplash.com/photo-1588661642278-f60be24c74cb?w=800",
    "https://images.unsplash.com/photo-1515238152791-8216bfdf89a7?w=800"
]

img_jets = [
    "https://images.unsplash.com/photo-1540962351504-03099e0a754b?w=800",
    "https://images.unsplash.com/photo-1559087867-ce4c91325525?w=800",
    "https://images.unsplash.com/photo-1583416750470-965b2707b355?w=800",
    "https://images.unsplash.com/photo-1517999144091-3d9dca6d1e43?w=800",
    "https://images.unsplash.com/photo-1579899321307-e818820c7a5f?w=800",
    "https://images.unsplash.com/photo-1620612239462-23c8a5202867?w=800",
    "https://images.unsplash.com/photo-1541447271487-09edaf9b28ea?w=800",
    "https://images.unsplash.com/photo-1514315384763-ba4017794115?w=800",
    "https://images.unsplash.com/photo-1569154941061-e231b4732ef1?w=800",
    "https://images.unsplash.com/photo-1529074963764-98f45c47344b?w=800"
]

# Shuffle to ensure randomness but no repeats within short loops
random.shuffle(img_realestate)
random.shuffle(img_cars)
random.shuffle(img_yachts)
random.shuffle(img_jets)

posts_file = "/Users/kenhuynh/.gemini/antigravity-ide/scratch/huynh-hoang-thinh-website/data/posts.json"
html_file = "/Users/kenhuynh/.gemini/antigravity-ide/scratch/huynh-hoang-thinh-website/index.html"

with open(posts_file, "r", encoding="utf-8") as f:
    posts = json.load(f)

# Update images in posts based on title keywords
for i, post in enumerate(posts):
    title = post['title'].lower()
    
    if "xe" in title or "hypercar" in title or "garage" in title or "chiron" in title or "porsche" in title or "lamborghini" in title or "rolls" in title or "mclaren" in title or "aston" in title or "koenigsegg" in title or "bugatti" in title or "ferrari" in title:
        img = img_cars[i % len(img_cars)]
    elif "du thuyền" in title or "yacht" in title or "biển" in title or "đại dương" in title or "lürssen" in title or "oceanco" in title or "feadship" in title or "azimut" in title or "sunseeker" in title or "riva" in title:
        img = img_yachts[i % len(img_yachts)]
    elif "máy bay" in title or "chuyên cơ" in title or "jet" in title or "gulfstream" in title or "bombardier" in title or "falcon" in title or "cessna" in title or "embraer" in title or "pilatus" in title:
        img = img_jets[i % len(img_jets)]
    else:
        # Default to Real Estate
        img = img_realestate[i % len(img_realestate)]
        
    post['image'] = img

# Save posts
with open(posts_file, "w", encoding="utf-8") as f:
    json.dump(posts, f, ensure_ascii=False, indent=2)

# Now update index.html to match
with open(html_file, "r", encoding="utf-8") as f:
    html = f.read()

soup = BeautifulSoup(html, "html.parser")

# Helper to find post by title substring
def get_post_image_by_title(title_text):
    title_text = title_text.lower().strip()
    for p in posts:
        if p['title'].lower().strip() == title_text:
            return p['image']
    return None

def get_post_image_by_id(post_id):
    for p in posts:
        if str(p['id']) == str(post_id):
            return p['image']
    return None

# Update all anchor tags that point to article.html
for a_tag in soup.find_all("a", href=re.compile(r"article\.html\?id=\d+")):
    post_id = a_tag['href'].split("=")[-1]
    correct_img = get_post_image_by_id(post_id)
    if correct_img:
        # Check if it has background-image (top-listing)
        if a_tag.find(class_="top-listing-img"):
            img_div = a_tag.find(class_="top-listing-img")
            img_div['style'] = f"background-image: url('{correct_img}');"
        # Check if it has img tag (grid-card or news)
        img_tag = a_tag.find("img")
        if img_tag:
            img_tag['src'] = correct_img

# Write back HTML
with open(html_file, "w", encoding="utf-8") as f:
    # Beautifulsoup sometimes converts & to &amp;, but since we don't have & in URLs anymore, it's safe!
    html_str = str(soup)
    html_str = html_str.replace("&amp;", "&") # just to be safe
    f.write(html_str)

print("All images updated successfully and synced between JSON and HTML.")
