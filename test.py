import requests

r = requests.post(url = "https://comakecategorizer.herokuapp.com/api/", data = {'text': "hello there"})
print(r)