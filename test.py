import requests

res = requests.get("http://www.official-joke-api.appspot.com/random_joke")
print(res.json()["punchline"])
