import requests

API_KEY = "bc02ae346739ccbf63347d4934ae8885"
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

parameters = {"q": "Madrid", "appid": API_KEY}

res = requests.get(BASE_URL, params=parameters)
res.raise_for_status()
print(res.json())
