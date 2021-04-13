# -*- coding: utf-8 -*-
"""
Created on Mon Apr 12 21:10:48 2021

@author: Роман
"""

import requests
import json
#from pprint import pprint
#import os

api_key='b9b7b09d12a9aa4a8129461caed3f127'
#api_key = os.getenv('api_key', 'b9b7b09d12a9aa4a8129461caed3f127')

city_name=input('Enter name of a city: ')

request_url='https://api.openweathermap.org/data/2.5/weather'

params={
    'q':city_name,
    'appid':api_key
}

res = json.loads(requests.get(request_url,params=params).text)

'''
'coord': {'lon': -0.1257, 'lat': 51.5085}, 
'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}], 
'base': 'stations', 
'main': {'temp': 281.34, 'feels_like': 280.18, 'temp_min': 280.37, 'temp_max': 282.15, 'pressure': 1030, 'humidity': 31}, 
'visibility': 10000, 'wind': {'speed': 2.06, 'deg': 360}, 
'clouds': {'all': 90}, 'dt': 1618252183, 
'sys': {'type': 1, 'id': 1414, 'country': 'GB', 'sunrise': 1618204250, 'sunset': 1618253474},
 'timezone': 3600, 'id': 2643743, 'name': 'London', 'cod': 200}
'''
print()
print(f'Country: {res["sys"]["country"]}')
print(f'City name: {res["name"]}')
print(f'Cordinates: {res["coord"]}')
print(f'Weather: {res["weather"]}')
print(f'Main info: {res["main"]}')
print(f'Wind info: {res["wind"]}')
print(f'Clouds info: {res["clouds"]}')

