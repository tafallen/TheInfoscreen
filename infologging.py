import logging
import logging.handlers
import os

def setup_logging():
    handler = logging.handlers.WatchedFileHandler(
        os.environ.get("LOGFILE", "./infoscreen.log"))
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    handler.setFormatter(formatter)

    root = logging.getLogger()
    root.setLevel(os.environ.get("LOGLEVEL", "INFO"))
    root.addHandler(handler)

def log_message(message):
    log = logging.getLogger("infoscreen")
    log.info(message)
