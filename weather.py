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
    if (response.status_code != 200):
        print("NOT FOUND")
        return None
  
    data= response.json()
   
    weather={
        "City": data["location"]["name"],
        "Region": data["location"]["region"],
        "Country": data["location"]["country"],
        "Temperature (C)": data["current"]["temp_c"],
        "Temperature (F)": data["current"]["temp_f"],
        "Humidity": data["current"]["humidity"],
        "Wind Speed (kph)": data["current"]["wind_kph"],
        "Condition":data["current"]["condition"]["text"],
        "Wind Direction": data["current"]["wind_dir"],
        "Wind Degree": data["current"]["wind_degree"],
        "Pressure (mb)": data["current"]["pressure_mb"],
        "Chance of Rain": data["current"]["chance_of_rain"],
        "Chance of Snow": data["current"]["chance_of_snow"],
        "UV Index": data["current"]["uv"],
        "Feels Like (C)": data["current"]["feelslike_c"],
        "Feels Like (F)": data["current"]["feelslike_f"],
        "Will It Rain?": data["current"]["will_it_rain"],
        "Will It Snow?": data["current"]["will_it_snow"],

    }
    return weather

# weather=get_weather("toronto")
# if weather:
#     # print(weather)
#     print()
#     print("CITY:", weather["City"])
#     print("REGION:", weather["Region"])
#     print("COUNTRY:", weather["Country"])
#     print("TEMPERATURE (C):", weather["Temperature (C)"])
#     print("TEMPERATURE (F):", weather["Temperature (F)"])
#     print("HUMIDITY:", weather["Humidity"])
#     print("WIND SPEED (KPH):", weather["Wind Speed (kph)"])
#     print("WIND DIRECTION :",weather["Wind Direction"])
#     print("CONDITION:", weather["Condition"])
#     print("WIND DEGREE : ",weather["Wind Degree"])
#     print("FEELS LIKE (C) :",weather["Feels Like (C)"])
#     print("FEELS LIKE (F):" ,weather["Feels Like (F)"])
#     print("WILL IT RAIN ? :",weather["Will It Rain?"])
#     print("WILL IT SNOW? :",weather["Will It Snow?"])
#     print("UI INDEX : ",weather["UV Index"])
#     print("CHANCE OF RAIN :",weather["Chance of Rain"])
#     print("CHANCE OF SNOW :",weather["Chance of Snow"])
# else:
 
#     print("Weather data not available.")