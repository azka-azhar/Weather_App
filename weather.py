# ------------------------------------
# Weather API Module
# ------------------------------------
# This file is responsible for:
# 1. Sending requests to the Weather API
# 2. Receiving weather data
# 3. Returning the required information

import os
from dotenv import load_dotenv
import requests

load_dotenv()
API_KEY = os.getenv("API_KEY")

def get_weather(city):
    url = f"https://api.weatherapi.com/v1/current.json?key={API_KEY}&q={city}"
    response = requests.get(url)
    print(response.status_code)
    data= response.json()
   
    weather={
        "City:", data["location"]["name"],
        "Region:", data["location"]["region"],
        "Country:", data["location"]["country"],
        "Temperature (C):", data["current"]["temp_c"],
        "Temperature (F):", data["current"]["temp_f"],
        "Humidity:", data["current"]["humidity"],
        "Wind Speed (kph):", data["current"]["wind_kph"],
        "Condition:", data["current"]["condition"]["text"],
        "Wind Direction:", data["current"]["wind_dir"],
        "Wind Degree:", data["current"]["wind_degree"],
        "Pressure (mb):", data["current"]["pressure_mb"],
        "Chance of Rain:", data["current"]["chance_of_rain"],
        "Chance of Snow:", data["current"]["chance_of_snow"],
        "UV Index:", data["current"]["uv"],
        "Feels Like (C):", data["current"]["feelslike_c"],
        "Feels Like (F):", data["current"]["feelslike_f"],
        "Will It Rain?", data["current"]["will_it_rain"],
        "Will It Snow?", data["current"]["will_it_snow"],

    }
    return weather

weather=get_weather("lahore")
if weather:
    print(weather)
    print()
    print("CITY:", weather["City:"])
    print("REGION:", weather["Region:"])
    print("COUNTRY:", weather["Country:"])
    print("TEMPERATURE (C):", weather["Temperature (C):"])
    print("HUMIDITY:", weather["Humidity:"])
    print("WIND SPEED (KPH):", weather["Wind Speed (kph):"])
    print("CONDITION:", weather["Condition:"])
else:
 
    print("Weather data not available.")