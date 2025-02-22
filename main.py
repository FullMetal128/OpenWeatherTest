import requests
import json

API_key = '32d1b56c6598eb16fe689ebff1ff6d97'

def get_weather_data(city,  API_key):
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_key}&units=metric"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        return data
    else:
        return response.status_code

print(get_weather_data('Moscow', API_key))


