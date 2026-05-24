import os
import requests
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("API_KEY")
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"


def get_weather(city):
    params = {
        "q": city,
        "appid": API_KEY,
        "units": "metric",
        "lang": "es"
    }

    response = requests.get(BASE_URL, params=params)

    if response.status_code != 200:
        print("Status code:", response.status_code)
        print(response.json())
        return

    data = response.json()

    temperature = data["main"]["temp"]
    description = data["weather"][0]["description"]
    humidity = data["main"]["humidity"]

    print("\n=== WEATHER INFO ===")
    print(f"City: {city}")
    print(f"Temperature: {temperature}°C")  
    print(f"Weather: {description}")
    print(f"Humidity: {humidity}%")