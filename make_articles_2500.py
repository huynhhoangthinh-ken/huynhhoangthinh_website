import json, re

def count_words(html_str):
    text = re.sub(r'<[^>]+>', ' ', html_str)
    return len(text.split())

with open('data/posts.json', 'r', encoding='utf-8') as f:
    posts = json.load(f)

# Define expanded content templates for all 10 articles
articles_dict = {}

# We will read each post from 701 to 710 and write detailed 2500+ words content
