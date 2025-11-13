import unittest
from unittest.mock import Mock
import sys
sys.path.insert(1, './data')
sys.path.insert(1, './')
import weather

class TestWeather(unittest.TestCase):

    def test_get_weather(self):
        # Create a mock weather data provider
        mock_weather_data = {
            "DailyForecasts": [
                {
                    "Date": "2024-01-01T07:00:00+00:00",
                    "Temperature": {
                        "Minimum": {"Value": 10.0},
                        "Maximum": {"Value": 20.0}
                    },
                    "Day": {
                        "Icon": 1,
                        "IconPhrase": "Sunny"
                    },
                    "Night": {
                        "Icon": 33,
                        "IconPhrase": "Clear"
                    }
                }
            ]
        }

        mock_provider = Mock(return_value=mock_weather_data)

        # Call the get_weather function with the mock provider
        forecast = weather.get_weather(weather_data_provider=mock_provider)

        # Assert that the forecast is not empty
        self.assertIsNotNone(forecast)
        self.assertEqual(len(forecast), 1)

        # Assert that the Day object has the correct data
        day = forecast[0]
        self.assertEqual(day.tempMax, "20.0")
        self.assertEqual(day.tempMin, "10.0")
        self.assertEqual(day.summary, "Sunny")
        self.assertEqual(day.dayIcon, 1)
        self.assertEqual(day.nightIcon, 33)

if __name__ == '__main__':
    unittest.main()