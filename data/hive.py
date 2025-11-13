"""This module provides functions for fetching heating data from the
Hive API."""
import apis
import json
import requests
import requests_cache
import settings


requests_cache.install_cache(
    cache_name="hive_api", backend="sqlite", expire_after=60
)


def get_hive_sessionId(requests_module=requests):
    """Get a session ID from the Hive API.

    Args:
        requests_module (module): The requests module to use for making the
                                    API call.

    Returns:
        str: The session ID.
    """
    payload = (
        '{\r\n    "sessions": [{\r\n        "username": "'
        + apis.username
        + '",\r\n        "password": "'
        + apis.password
        + '",\r\n        "caller": "WEB"\r\n    }]\r\n}'
    )
    headers = {
        "Content-Type": "application/json",
        "Accept": "application/vnd.alertme.zoo-6.1+json",
        "X-Omnia-Client": "Hive Web Dashboard",
        "User-Agent": "PostmanRuntime/7.18.0",
        "Cache-Control": "no-cache",
        "Host": "api.prod.bgchprod.info:443",
        "Accept-Encoding": "gzip, deflate",
        "Content-Length": "139",
        "Connection": "keep-alive",
        "cache-control": "no-cache",
    }

    response = requests_module.request(
        "POST", apis.hive_login_url, data=payload, headers=headers
    )

    login_data = json.loads(response.text)
    return login_data["sessions"][0]["sessionId"]


def get_hive_nodes(sessionId, requests_module=requests):
    """Get all nodes from the Hive API.

    Args:
        sessionId (str): The session ID to use for authentication.
        requests_module (module): The requests module to use for making the
                                    API call.

    Returns:
        dict: A dictionary containing the nodes.
    """

    url = "https://api.prod.bgchprod.info:443/omnia/nodes"

    headers = {
        "Content-Type": "application/vnd.alertme.zoo-6.1+json",
        "Accept": "application/vnd.alertme.zoo-6.1+json",
        "X-Omnia-Client": "Hive Web Dashboard",
        "X-Omnia-Access-Token": sessionId,
        "User-Agent": "PostmanRuntime/7.18.0",
        "Cache-Control": "no-cache",
        "Host": "api.prod.bgchprod.info:443",
        "Accept-Encoding": "gzip, deflate",
        "Connection": "keep-alive",
        "cache-control": "no-cache",
    }

    response = requests_module.request("GET", url, headers=headers)
    return json.loads(response.text)


def get_heating_state(
    session_id_provider=get_hive_sessionId, nodes_provider=get_hive_nodes
):
    """Get the current heating state.

    Args:
        session_id_provider (function): The function to use for getting the
                                        session ID.
        nodes_provider (function): The function to use for getting the nodes.

    Returns:
        Thermostat: A Thermostat object representing the current heating
                    state.
    """
    sessionId = session_id_provider()
    nodes = nodes_provider(sessionId)

    thermo = [
        x for x in nodes["nodes"] if x["name"] == settings.thermostat_name
    ][0]

    return Thermostat(thermo)


class Thermostat:
    """A class to represent the state of the thermostat."""

    def __init__(self, node):
        """Initialize the Thermostat object.

        Args:
            node (dict): The node representing the thermostat.
        """
        self.state = str(
            node["attributes"]["stateHeatingRelay"]["reportedValue"]
        )
        self.mode = str(
            node["attributes"]["activeHeatCoolMode"]["displayValue"]
        )
        self.temp_target = str(
            node["attributes"]["targetHeatTemperature"]["displayValue"]
        )
        self.temp_current = str(
            node["attributes"]["temperature"]["displayValue"]
        )

    def dump(self):
        """Print the thermostat state to the console."""
        print("Heat:       " + self.state)
        print("Mode:       " + self.mode)
        print("Target:     " + self.temp_target)
        print("Temprature: " + self.temp_current)
