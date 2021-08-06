import requests
import os
import json
from datetime import datetime
#542ffd081e67f4512b705f89d2a611b2
#ba24c6018ddd72041749018d0c1b1ef8
user_api = os.environ['weather_key']
location = input("Enter the city name: ")

complete_api_link = "https://api.openweathermap.org/data/2.5/weather?q="+location+"&appid="+user_api
api_link = requests.get(complete_api_link)
api_data = api_link.json()
path = os.path.dirname(os.path.abspath(__file__))
path = os.path.join(path, "data", "data.json")
path = os.path.normpath(path)
with open(path, 'w') as outfile:
    json.dump(api_data, outfile, indent = 4)
#create variables to store and display data
temp_city = ((api_data['main']['temp']) - 273.15)
weather_desc = api_data['weather'][0]['description']
hmdt = api_data['main']['humidity']
wind_spd = api_data['wind']['speed']
date_time = datetime.now().strftime("%d %b %Y | %I:%M:%S %p")

print ("-------------------------------------------------------------")
print ("Weather Stats for - {}  || {}".format(location.upper(), date_time))
print ("-------------------------------------------------------------")

print ("Current temperature is: {:.2f} deg C".format(temp_city))
print ("Current weather desc  :",weather_desc)
print ("Current Humidity      :",hmdt, '%')
print ("Current wind speed    :",wind_spd ,'kmph')