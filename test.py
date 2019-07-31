import requests

r = requests.post(url = "https://comakecategorizer.netlify.com/api/", data = {'text': "hello there"})
print(r)