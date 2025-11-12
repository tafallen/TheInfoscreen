import unittest
from unittest.mock import Mock, MagicMock
import sys
sys.path.insert(1, './data')
sys.path.insert(1, './')
import hive

class TestHive(unittest.TestCase):

    def test_get_heating_state(self):
        # Create mock providers
        mock_session_id_provider = Mock(return_value="test_session_id")

        mock_nodes_data = {
            "nodes": [
                {
                    "name": "Hall",
                    "attributes": {
                        "stateHeatingRelay": {"reportedValue": "ON"},
                        "activeHeatCoolMode": {"displayValue": "BOOST"},
                        "targetHeatTemperature": {"displayValue": "21.0"},
                        "temperature": {"displayValue": "20.0"}
                    }
                }
            ]
        }
        mock_nodes_provider = Mock(return_value=mock_nodes_data)

        # Call the get_heating_state function with the mock providers
        thermostat = hive.get_heating_state(
            session_id_provider=mock_session_id_provider,
            nodes_provider=mock_nodes_provider
        )

        # Assert that the Thermostat object has the correct data
        self.assertIsNotNone(thermostat)
        self.assertEqual(thermostat.state, "ON")
        self.assertEqual(thermostat.mode, "BOOST")
        self.assertEqual(thermostat.temp_target, "21.0")
        self.assertEqual(thermostat.temp_current, "20.0")

if __name__ == '__main__':
    unittest.main()