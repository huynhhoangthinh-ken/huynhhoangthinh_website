import urllib.request
import json
import urllib.parse

def get_wiki_img(title):
    url = f"https://en.wikipedia.org/w/api.php?action=query&titles={urllib.parse.quote(title)}&prop=pageimages&format=json&pithumbsize=800"
    req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    try:
        res = urllib.request.urlopen(req)
        data = json.loads(res.read())
        pages = data['query']['pages']
        for page_id in pages:
            if 'thumbnail' in pages[page_id]:
                return pages[page_id]['thumbnail']['source']
    except Exception as e:
        print(f"Error for {title}: {e}")
    return None

for c in ["Koenigsegg Jesko", "Bugatti Chiron", "Ferrari LaFerrari", "Lamborghini Revuelto", "Rolls-Royce Spectre", "Gulfstream G700", "Lürssen", "Azimut Yachts"]:
    print(c, "->", get_wiki_img(c))
