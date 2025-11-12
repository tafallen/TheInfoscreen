from __future__ import print_function
import datetime
import json
import requests
import apis

def get_sunset_data(requests_module=requests):
    response = requests_module.get( apis.sunset_api_url )
    if response.status_code == 200:
        return json.loads(response.content.decode('utf-8'))
    else:
        print( response.status_code )
        return str(response.status_code)

def get_sunset(sunset_data_provider=get_sunset_data):
    sunset_json = sunset_data_provider()
    return Sunset(sunset_json)

class Sunset:
    def __init__(self, sunset_json):
        self.sunrise = sunset_json['results']['sunrise']
        self.sunset = sunset_json['results']['sunset']

    def dump(self):
        print( self.sunrise + " - " + self.sunset)

    def isNight(self, now=None):
        if now is None:
            now = datetime.datetime.now()
        time_now = now
        today = time_now.date()

        sunrise_time = datetime.datetime.strptime(self.sunrise, '%I:%M:%S %p').time()
        sunset_time = datetime.datetime.strptime(self.sunset, '%I:%M:%S %p').time()

        sunrise = datetime.datetime.combine(today, sunrise_time)
        sunset = datetime.datetime.combine(today, sunset_time)

        if( sunrise < time_now and time_now < sunset):
            return False
        return True

