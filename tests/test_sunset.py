import unittest
from unittest.mock import Mock
import sys
sys.path.insert(1, './data')
sys.path.insert(1, './')
import sunset
import datetime

class TestSunset(unittest.TestCase):

    def test_get_sunset(self):
        # Create a mock sunset data provider
        mock_sunset_data = {
            "results": {
                "sunrise": "6:00:00 AM",
                "sunset": "8:00:00 PM"
            }
        }

        mock_provider = Mock(return_value=mock_sunset_data)

        # Call the get_sunset function with the mock provider
        sunset_obj = sunset.get_sunset(sunset_data_provider=mock_provider)

        # Assert that the Sunset object has the correct data
        self.assertIsNotNone(sunset_obj)
        self.assertEqual(sunset_obj.sunrise, "6:00:00 AM")
        self.assertEqual(sunset_obj.sunset, "8:00:00 PM")

    def test_is_night(self):
        # Create a Sunset object with known sunrise and sunset times
        sunset_obj = sunset.Sunset({"results": {"sunrise": "6:00:00 AM", "sunset": "8:00:00 PM"}})

        # Test with a time during the day
        day_time = datetime.datetime(2024, 1, 1, 12, 0, 0)
        self.assertFalse(sunset_obj.isNight(now=day_time))

        # Test with a time at night
        night_time = datetime.datetime(2024, 1, 1, 22, 0, 0)
        self.assertTrue(sunset_obj.isNight(now=night_time))

if __name__ == '__main__':
    unittest.main()