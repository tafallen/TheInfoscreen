"""The main entry point for the info screen application.

This script initializes the e-paper display, sets up logging, and then enters
an infinite loop to continuously update the display with new information.
The display is refreshed every 5 minutes (300 seconds).
"""
import sys
import time
import display
import epaper
import infologging as log

sys.path.insert(1, "./display")


epaper.initialise()

log.setup_logging()

try:
    while True:
        log.log_message("Creating image")
        image = display.createImage()
        epaper.display_on_e_paper(image)
        log.log_message("Sleeping")
        time.sleep(300)
except Exception:
    log.logging.exception("Exception thrown")
