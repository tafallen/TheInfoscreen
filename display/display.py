import sys
sys.path.insert(1, './display')
import displayheader
import displaynews
import displayweather
import displaytrains
import displayheating
import displaycountdown
import displayagenda
import draw
import infologging as log
import settings

def createImage():
    image = draw.create_display(settings.displaysize)

    try: 
        log.log_message('Header')
        displayheader.display_header(image, settings.header_location, settings.header_size)
    except:
        log.log_message('Header failed?')

    try: 
        log.log_message('Weather')
        displayweather.display_weather(image, settings.weather_location, settings.weather_size)
    except:
        log.log_message('Weather failed?')

    try: 
        log.log_message('News')
        displaynews.display_news(image, settings.news_location, settings.news_size)
    except:
        log.log_message('News failed?')

    try: 
        log.log_message('Trains')
        displaytrains.display_trains(image, settings.trains_location, settings.trains_size)
    except:
        log.log_message('Trains failed?')

    try: 
        log.log_message('Heating')
        displayheating.display_heating(image, settings.heating_location, settings.heating_size)
    except:
        log.log_message('Heating failed?')

    print("display: returning image")
    return image
