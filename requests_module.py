import requests
import os

# open weather api test
API_KEY = os.environ.get("owm_api_key")
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

parameters = {"q": "Madrid", "appid": API_KEY}

res = requests.get(BASE_URL, params=parameters)
res.raise_for_status()
print(API_KEY)
print(res.json())


# post request in python
url = "some url"
payload = {
    "name": "Egor",
    "age": 29,
    "languages": ["english", "spanish", "russian"],
}

post_res = requests.post(url, json=payload)

# note: with the PUT method you need to pass in the whole 'person' object to update
# with the PATCH method, only pass the data that needs to be changed in 'person'
