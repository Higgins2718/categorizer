import requests

r = requests.post(url = "https://comakecategorizer.herokuapp.com/api/", data = "hello there")
print(r)