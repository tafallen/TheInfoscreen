from __future__ import print_function
from datetime import date, time, datetime
import apis
import calendar
import datetime
import json
import os
import requests

def get_cache_timestamp(filename):
    if os.path.exists(filename):
        statbuf = os.stat(filename)
        timestamp = datetime.datetime.fromtimestamp(statbuf.st_mtime)
        print('weather: cache timestamp = ' + str(timestamp))
        return timestamp
    else:
        print('weather: cache didn\'t exist')
        return datetime.datetime(2010,1,1) 

def update_weather_cache(filename, requests_module=requests):
    print('weather: Updating cache')
    response = requests_module.get(apis.accuweather_api_url)
    if response.status_code == 200:
        document = json.loads(response.content.decode('utf-8'))
        with open(filename, 'w') as outfile:
            json.dump(document, outfile)
        print('weather: cache update success')
        return
    print('weather: cache update fail = ' + str(response.status_code))

def get_weather_data(requests_module=requests):
    filename = "./cache/weather.json"
    cache_time = get_cache_timestamp(filename)

    if cache_time < (datetime.datetime.now() - datetime.timedelta(hours=1)):
        update_weather_cache(filename, requests_module)

    print('weather: loading from file...')
    if os.path.exists(filename):
        with open(filename) as json_file:
            return json.load(json_file)

    print('weather: loading from file... FAILED')
    return None
    
def get_weather(weather_data_provider=get_weather_data):
    weather_json = weather_data_provider()
    if weather_json == None or weather_json == '503':
        print('weather: No forecast')
        return []

    daily_forcasts = weather_json['DailyForecasts']
    day_index = date.today().weekday()
    result = []

    i = 0
    while(i < len(daily_forcasts)):
        result.append(Day(day_index + i, daily_forcasts[i]))
        i += 1

    print('weather: loaded forecast')
    return result

class Day:
    def __init__(self, day_index, weather_data):
        self.day = calendar.day_name[(day_index%7)]
        self.tempMax = str(weather_data['Temperature']['Maximum']['Value'])
        self.tempMin = str(weather_data['Temperature']['Minimum']['Value'])
        self.summary = weather_data['Day']['IconPhrase']
        self.dayIcon = weather_data['Day']['Icon']
        self.nightIcon = weather_data['Night']['Icon']

    def dump(self):
        print(self.day)
        print(self.tempMin + "°C/" + self.tempMax + "°C")
        print(self.summary)
        