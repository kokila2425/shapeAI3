import requests
# import os
from datetime import datetime

api_key = '922d282e6930061e50acf74775abc567'
location = input("Enter the city name: ")

complete_api_link = "https://api.openweathermap.org/data/2.5/weather?q="+location+"&appid="+api_key
api_link = requests.get(complete_api_link)
api_data = api_link.json()


# create variables to store and display data
temp_city = ((api_data['main']['temp']) - 273.15)
weather_desc = api_data['weather'][0]['description']
hmdt = api_data['main']['humidity']
wind_spd = api_data['wind']['speed']
date_time = datetime.now().strftime("%d %b %Y | %I:%M:%S %p")

print("--------------------------------------------------------------")
print("weather stats for - {} || {}".format(location.upper(), date_time))
print("-------------------------------------------------------------")

print("current temperature is: {:.2f} deg c".format(temp_city))
print("current weather desc :", weather_desc)
print("current Humidity     :", hmdt, '%')
print("current wind speed   :", wind_spd, 'kmph')
