import requests
import os

API_KEY = os.environ.get("owm_api_key")
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

parameters = {"q": "Madrid", "appid": API_KEY}

res = requests.get(BASE_URL, params=parameters)
res.raise_for_status()
print(API_KEY)
print(res.json())
