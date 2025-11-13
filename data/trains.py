"""This module provides functions for fetching train times from the National
Rail Darwin API."""
import sys
from nredarwin.webservice import DarwinLdbSession
import apis
import infologging as log

sys.path.insert(1, "../")


# TODO: Can we preserve the session and save some processing time?
def get_train_times(source, dest, session=None):
    """Get train times from the National Rail Darwin API.

    Args:
        source (str): The source station CRS code.
        dest (str): The destination station CRS code.
        session (DarwinLdbSession, optional): The DarwinLdbSession object to
                                                use. Defaults to None.

    Returns:
        StationBoard: A StationBoard object.
    """
    if session is None:
        log.log_message("trains: Getting session")
        session = DarwinLdbSession(
            wsdl=apis.darwin_api_url, api_key=apis.darwin_api_key
        )

    log.log_message("trains: Getting train times: " + source + " -> " + dest)
    result = session.get_station_board(source, destination_crs=dest)

    log.log_message("trains: Got times: " + source + " -> " + dest)
    return result
