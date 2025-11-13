import unittest
from unittest.mock import Mock
import sys
sys.path.insert(1, './data')
sys.path.insert(1, './')
import trains

class TestTrains(unittest.TestCase):

    def test_get_train_times(self):
        # Create a mock session object
        mock_session = Mock()
        mock_session.get_station_board.return_value = "test_board"

        # Call the get_train_times function with the mock session
        result = trains.get_train_times("MAN", "LDS", session=mock_session)

        # Assert that the get_station_board method was called with the correct arguments
        mock_session.get_station_board.assert_called_with("MAN", destination_crs="LDS")

        # Assert that the result is the expected value
        self.assertEqual(result, "test_board")

if __name__ == '__main__':
    unittest.main()