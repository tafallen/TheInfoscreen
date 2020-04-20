import sys
sys.path.insert(1, '../')
from nredarwin.webservice import DarwinLdbSession
import apis
import infologging as log

# TODO: Can we preserve the session and save some processing time?
def get_train_times(source, dest):
    log.log_message('trains: Getting session')
    session = DarwinLdbSession(wsdl=apis.darwin_api_url, api_key=apis.darwin_api_key)

    log.log_message('trains: Getting train times: ' + source + ' -> ' + dest)
    result = session.get_station_board(source, destination_crs=dest)

    log.log_message('trains: Got times: ' + source + ' -> ' + dest)
    return result