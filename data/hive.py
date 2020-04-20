import apis
import json
import requests
import requests_cache
import settings


requests_cache.install_cache(cache_name='hive_api', backend='sqlite', expire_after=60)

def get_hive_sessionId():
    payload = "{\r\n    \"sessions\": [{\r\n        \"username\": \"" + apis.username + "\",\r\n        \"password\": \"" + apis.password + "\",\r\n        \"caller\": \"WEB\"\r\n    }]\r\n}"
    headers = {
        'Content-Type': "application/json",
        'Accept': "application/vnd.alertme.zoo-6.1+json",
        'X-Omnia-Client': "Hive Web Dashboard",
        'User-Agent': "PostmanRuntime/7.18.0",
        'Cache-Control': "no-cache",
        'Host': "api.prod.bgchprod.info:443",
        'Accept-Encoding': "gzip, deflate",
        'Content-Length': "139",
        'Connection': "keep-alive",
        'cache-control': "no-cache"
        }

    response = requests.request("POST", apis.hive_login_url, data=payload, headers=headers)

    login_data = json.loads(response.text)
    return login_data['sessions'][0]['sessionId'] 

def get_hive_nodes(sessionId):

    url = "https://api.prod.bgchprod.info:443/omnia/nodes"

    headers = {
        'Content-Type': "application/vnd.alertme.zoo-6.1+json",
        'Accept': "application/vnd.alertme.zoo-6.1+json",
        'X-Omnia-Client': "Hive Web Dashboard",
        'X-Omnia-Access-Token': sessionId,
        'User-Agent': "PostmanRuntime/7.18.0",
        'Cache-Control': "no-cache",
        'Host': "api.prod.bgchprod.info:443",
        'Accept-Encoding': "gzip, deflate",
        'Connection': "keep-alive",
        'cache-control': "no-cache"
        }

    response = requests.request("GET", url, headers=headers)
    return json.loads(response.text)

def get_heating_state():
    sessionId = get_hive_sessionId()
    nodes = get_hive_nodes(sessionId)
    
    thermo = [x for x in nodes['nodes'] if x['name'] == settings.thermostat_name][0]

    return Thermostat(thermo)

class Thermostat:
    def __init__(self, node):
        self.state = str(node['attributes']['stateHeatingRelay']['reportedValue'])
        self.mode = str(node['attributes']['activeHeatCoolMode']['displayValue'])
        self.temp_target = str(node['attributes']['targetHeatTemperature']['displayValue'])
        self.temp_current = str(node['attributes']['temperature']['displayValue'])
    def dump(self):
        print('Heat:       ' + self.state)
        print('Mode:       ' + self.mode)
        print('Target:     ' + self.temp_target)
        print('Temprature: ' + self.temp_current)
