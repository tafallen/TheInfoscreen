from __future__ import print_function
import datetime
import json
import requests
import apis

def get_sunset_data():
    response = requests.get( apis.sunset_api_url )
    if response.status_code == 200:
        return json.loads(response.content.decode('utf-8'))
    else:
        print( response.status_code )
        return str(response.status_code)

def get_sunset():
    sunset_json = get_sunset_data()
    return Sunset(sunset_json)

class Sunset:
    def __init__(self, sunset_json):
        self.sunrise = sunset_json['results']['sunrise']
        self.sunset = sunset_json['results']['sunset']

    def dump(self):
        print( self.sunrise + " - " + self.sunset)

    def isNight(self):
        time_now = datetime.datetime.now().time()

        sunrise_time = datetime.datetime.strptime(self.sunrise, '%I:%M:%S %p').time()
        sunset_time = datetime.datetime.strptime(self.sunset, '%I:%M:%S %p').time()

        if( sunrise_time < time_now and time_now < sunset_time):
            return False
        return True

