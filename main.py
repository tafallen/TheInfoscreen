import sys
sys.path.insert(1, './display')
import display
import epaper
import infologging as log
import time

epaper.initialise()

log.setup_logging()

try:
    while True:
        log.log_message('Creating image')
        image = display.createImage()
        epaper.display_on_e_paper(image)
        log.log_message('Sleeping')
        time.sleep(300)
except:
    log.logging.exception('Exception thrown')