"""This module provides functions for fetching sunrise and sunset times."""
from __future__ import print_function
import datetime
import json
import requests
import apis


def get_sunset_data(requests_module=requests):
    """Get sunrise and sunset data from the API.

    Args:
        requests_module (module): The requests module to use for making the API
                                  call.

    Returns:
        dict: A dictionary containing the sunrise and sunset data.
    """
    response = requests_module.get(apis.sunset_api_url)
    if response.status_code == 200:
        return json.loads(response.content.decode("utf-8"))
    else:
        print(response.status_code)
        return str(response.status_code)


def get_sunset(sunset_data_provider=get_sunset_data):
    """Get a Sunset object.

    Args:
        sunset_data_provider (function): The function to use for getting the
                                        sunset data.

    Returns:
        Sunset: A Sunset object.
    """
    sunset_json = sunset_data_provider()
    return Sunset(sunset_json)


class Sunset:
    """A class to represent the sunrise and sunset times."""

    def __init__(self, sunset_json):
        """Initialize the Sunset object.

        Args:
            sunset_json (dict): The JSON object representing the sunrise and
                                sunset times.
        """
        self.sunrise = sunset_json["results"]["sunrise"]
        self.sunset = sunset_json["results"]["sunset"]

    def dump(self):
        """Print the sunrise and sunset times to the console."""
        print(self.sunrise + " - " + self.sunset)

    def isNight(self, now=None):
        """Check if it is currently night.

        Args:
            now (datetime, optional): The current time. Defaults to None.

        Returns:
            bool: True if it is night, False otherwise.
        """
        if now is None:
            now = datetime.datetime.now()
        time_now = now
        today = time_now.date()

        sunrise_time = datetime.datetime.strptime(
            self.sunrise, "%I:%M:%S %p"
        ).time()
        sunset_time = datetime.datetime.strptime(
            self.sunset, "%I:%M:%S %p"
        ).time()

        sunrise = datetime.datetime.combine(today, sunrise_time)
        sunset = datetime.datetime.combine(today, sunset_time)

        if sunrise < time_now and time_now < sunset:
            return False
        return True
