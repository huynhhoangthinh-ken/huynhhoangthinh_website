import urllib.request
import json
import urllib.parse
import ssl
import time

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

def get_wiki_img(title):
    url = f"https://en.wikipedia.org/w/api.php?action=query&titles={urllib.parse.quote(title)}&prop=pageimages&format=json&pithumbsize=800"
    req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    try:
        res = urllib.request.urlopen(req, context=ctx)
        data = json.loads(res.read())
        pages = data['query']['pages']
        for page_id in pages:
            if 'thumbnail' in pages[page_id]:
                return pages[page_id]['thumbnail']['source']
    except Exception as e:
        print(f"Error for {title}: {e}")
    return None

items = [
    "Koenigsegg Jesko", "Bugatti Chiron", "LaFerrari", "Lamborghini Revuelto", 
    "Rolls-Royce Spectre", "Porsche 911 GT3", "McLaren 750S", "Aston Martin Valkyrie", 
    "Pagani Utopia", "Maserati MC20", "Bentley Continental GT", "Mercedes-AMG One", 
    "Koenigsegg Gemera", "Oceanco", "Lürssen", "Feadship", "Azimut Yachts", 
    "Sunseeker", "Riva (yacht)", "Gulfstream G700", "Bombardier Global Express", 
    "Dassault Falcon 10X", "Cessna Citation Longitude", "Embraer Praetor 600", "Pilatus PC-24"
]

results = {}
for c in items:
    url = get_wiki_img(c)
    print(c, "->", url)
    if url:
        results[c] = url
    time.sleep(0.5)

with open('wiki_images.json', 'w') as f:
    json.dump(results, f, indent=2)

