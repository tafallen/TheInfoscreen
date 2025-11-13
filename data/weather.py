"""This module provides functions for fetching weather data from the
AccuWeather API."""
from __future__ import print_function
from datetime import date, datetime
import apis
import calendar
import json
import os
import requests


def get_cache_timestamp(filename):
    """Get the timestamp of the cache file.

    Args:
        filename (str): The path to the cache file.

    Returns:
        datetime: The timestamp of the cache file, or a very old timestamp if
                    the file does not exist.
    """
    if os.path.exists(filename):
        statbuf = os.stat(filename)
        timestamp = datetime.fromtimestamp(statbuf.st_mtime)
        print("weather: cache timestamp = " + str(timestamp))
        return timestamp
    else:
        print("weather: cache didn't exist")
        return datetime(2010, 1, 1)


def update_weather_cache(filename, requests_module=requests):
    """Update the weather cache file.

    Args:
        filename (str): The path to the cache file.
        requests_module (module): The requests module to use for making the API
                                    call.
    """
    print("weather: Updating cache")
    response = requests_module.get(apis.accuweather_api_url)
    if response.status_code == 200:
        document = json.loads(response.content.decode("utf-8"))
        with open(filename, "w") as outfile:
            json.dump(document, outfile)
        print("weather: cache update success")
        return
    print("weather: cache update fail = " + str(response.status_code))


def get_weather_data(requests_module=requests):
    """Get weather data from the cache file, updating it if necessary.

    Args:
        requests_module (module): The requests module to use for making the API
                                    call.

    Returns:
        dict: A dictionary containing the weather data.
    """
    filename = "./cache/weather.json"
    cache_time = get_cache_timestamp(filename)

    if cache_time < (datetime.now() - datetime.timedelta(hours=1)):
        update_weather_cache(filename, requests_module)

    print("weather: loading from file...")
    if os.path.exists(filename):
        with open(filename) as json_file:
            return json.load(json_file)

    print("weather: loading from file... FAILED")
    return None


def get_weather(weather_data_provider=get_weather_data):
    """Get a list of weather forecast Day objects.

    Args:
        weather_data_provider (function): The function to use for getting the
                                            weather data.

    Returns:
        list: A list of Day objects.
    """
    weather_json = weather_data_provider()
    if weather_json is None or weather_json == "503":
        print("weather: No forecast")
        return []

    daily_forcasts = weather_json["DailyForecasts"]
    day_index = date.today().weekday()
    result = []

    i = 0
    while i < len(daily_forcasts):
        result.append(Day(day_index + i, daily_forcasts[i]))
        i += 1

    print("weather: loaded forecast")
    return result


class Day:
    """A class to represent a day's weather forecast."""

    def __init__(self, day_index, weather_data):
        """Initialize the Day object.

        Args:
            day_index (int): The index of the day of the week (0-6).
            weather_data (dict): The JSON object representing the day's weather
                                    forecast.
        """
        self.day = calendar.day_name[(day_index % 7)]
        self.tempMax = str(weather_data["Temperature"]["Maximum"]["Value"])
        self.tempMin = str(weather_data["Temperature"]["Minimum"]["Value"])
        self.summary = weather_data["Day"]["IconPhrase"]
        self.dayIcon = weather_data["Day"]["Icon"]
        self.nightIcon = weather_data["Night"]["Icon"]

    def dump(self):
        """Print the day's weather forecast to the console."""
        print(self.day)
        print(self.tempMin + "°C/" + self.tempMax + "°C")
        print(self.summary)
