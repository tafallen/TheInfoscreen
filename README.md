# infoscreen

A tailored home information screen using a Raspberry Pi Zero WH, a 7.5" WaveShare e-Paper screen and HAT.

It's a bit like a magic mirror, but it's low power, not a mirror and contains code rather than magic.

## I offer no warranty, support or help with this project. 
It's just some scrappy code I wrote to do a thing. It might help you do a thing too, or it might not. Play with it and have fun. 

I do assume you have some knowledge, such as how to setup a Raspberry Pi, how to clone git repos, get API keys and know some python.

I intend, one day, to make this easier to install, configure and use but this is not that day. I don't know Python all that well, so it's been a learning process too. I'm sure that there's plenty here that could be done better or in a more Pythonic way. If you'd like to suggest improvments then that would be nice.

## Hardware requirements

* WaveShare 7.5 in black & white e-paper display + HAT
* Raspberry Pi (I used a ZeroW)

## Installation requirements

Required:
* A newsapi.org account
* A National Rail API account
* An accuweather account

Optional:
* The Hive heating system

## Setup instructions

1. Get the Raspberry Pi + setup, powered, network connected, accessible by SSH and with the e-paper screen connected.
2. SSH to your Raspberry Pi
3. Clone the code to the Raspberry Pi
4. Install some of the pre-requisite libraries:
```
pip install newsapi-python
pip install nre-darwin-py
pip install --upgrade requests-cache
pip install Pillow
```
5. Edit the `apis.py` file entering keys, usernames etc. for the services you are using. I'm using Hive for heating control, sunrise-sunset.org for getting sunrise/sunset times, Accuweather for weather data and Darwin for UK Train information.
6. For any service that you're not using, e.g. hive, you can comment out a section in `display/display.py` to hide that section.
7. Run the `main.py` script using python3 and, eventually once all the data has been gathered from the web services, the rendered image will be pushed to the e-paper screen. The data and image willbe refreshed every 5 minutes.
8. Using `cron`, and the 'launcher.sh' file in the repo, you can run the code headless. I hate `cron`. Took ages and some googling to get it to work. I can't remember how I did it now. :-(

## Project structure

The project is split into the following areas:
* Root level folder containing the `main.py` file and some other important files, notably the `epaper.py` file which sends the image to the screen.
* data folder - Contains the code which talks to external webservices and gets data.
* display folder - Contains the folder which displays various viewable panels which are composed to form the image to be pushed to the e-paper screen. `display.py` co-ordinates the drawing process and `draw.py` does the actual drawing for each panel. `settings.py` contains lots of co-ordinates, font sizes and other things.
* fonts - a couple of Google fonts that the project uses.
* WeatherIcons - The weather icons, obviously.
* icons - Other icons!
* lib - The WaveShare e-paper drivers. 

### epaper.py

Commenting out the lines referencing `epd7in5` and `epd` will allow the code to run without an e-paper screen connected. Very useful when you're playing around with what's to be displayed on a different platform (in my case Win10. Don't judge.). 

### Logging

A logfile will be produced in the root code directory and, when things go wrong, it might help diagnose the issue.