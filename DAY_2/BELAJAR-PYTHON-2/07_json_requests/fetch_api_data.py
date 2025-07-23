import requests
import json

r = requests.get('https://jsonplaceholder.typicode.com/posts')
data = r.json()

with open("posts.json", "w") as file:
    json.dump(data[:5], f, indent=2)