import json

file_path = "/Users/kenhuynh/.gemini/antigravity-ide/scratch/huynh-hoang-thinh-website/index.html"
with open(file_path, "r", encoding="utf-8") as f:
    content = f.read()

content = content.replace("&amp;", "&")

with open(file_path, "w", encoding="utf-8") as f:
    f.write(content)

print("Fixed amp in index.html")
