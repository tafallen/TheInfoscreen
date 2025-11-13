"""This module provides logging setup and helper functions."""
import logging
import logging.handlers
import os


def setup_logging():
    """Configure the root logger for the application.

    Sets up a watched file handler that writes logs to './infoscreen.log'
    by default, or to the path specified in the LOGFILE environment variable.
    The log level is set to INFO by default, or to the level specified in
    the LOGLEVEL environment variable.
    """
    handler = logging.handlers.WatchedFileHandler(
        os.environ.get("LOGFILE", "./infoscreen.log")
    )
    formatter = logging.Formatter(
        "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
    )
    handler.setFormatter(formatter)

    root = logging.getLogger()
    root.setLevel(os.environ.get("LOGLEVEL", "INFO"))
    root.addHandler(handler)


def log_message(message):
    """Log an informational message to the infoscreen logger.

    Args:
        message (str): The message to log.
    """
    log = logging.getLogger("infoscreen")
    log.info(message)
