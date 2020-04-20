import sys
sys.path.insert(1, './data')
import weather
import sunset
import draw
import datetime
import settings


def isNight():
    return sunset.get_sunset().isNight()

def draw_weather_day(image, day, i, origin, displaysize):
    draw_weather_day_title(i, image, origin, displaysize)
    draw_weather_day_icon(day, i, image, origin, displaysize)
    draw_weather_day_temp(day, i, image, origin, displaysize)
    draw_weather_day_summary(day, i, image, origin, displaysize)
    draw_weather_grid(image, origin, displaysize)

def get_day_horiontal_origin(i, origin, displaysize):
    column_width = int ((displaysize[0] - origin[0])/3)
    return origin[0] + settings.weather_content_indent + (i * column_width)

def draw_weather_data(image, forecast, origin, displaysize):
    i = 0
    have_forecast = False if len(forecast) == 0 else True

    while i < 3:
        day = forecast[i] if have_forecast else None
        draw_weather_day(image, day, i, origin, displaysize)
        i += 1

def draw_weather_day_title(i, image, origin, displaysize):
    day_text = (datetime.datetime.now() + datetime.timedelta(days=i)).strftime("%A")
    position = (get_day_horiontal_origin(i, origin, displaysize), settings.day_indent_y + origin[1])
    draw.draw_temp_line(image, day_text, position)

def draw_weather_day_summary(day, i, image, origin, displaysize):
    x = get_day_horiontal_origin(i, origin, displaysize)
    line1_position = (x + settings.summary_indent_x, settings.summary_indent_line1_y + origin[1])
    line2_position = (x + settings.summary_indent_x, settings.summary_indent_line2_y + origin[1])

    if day == None:
        draw.draw_summary_header(image, '?', line1_position)
        return

    #TODO: get the col width and use it to calculate the line break
    #Steal the code from elsewhere in the project and generalise
    if(len(day.summary) > 20):
        line_break = day.summary.rfind(' ', 0, 19)
        draw.draw_summary_header(image, day.summary[:line_break], line1_position)
        draw.draw_summary_header(image, day.summary[line_break+1:], line2_position)
    else:
        draw.draw_summary_header(image, day.summary, line1_position)

def get_temprature_text(day):
    return '?' if day == None else day.tempMax + settings.temp_units + settings.temp_separator + day.tempMin + settings.temp_units

def draw_weather_day_temp(day, i, image, origin, displaysize):
    position = (get_day_horiontal_origin(i, origin, displaysize), settings.temp_indent_y + origin[1])
    draw.draw_temp_line(image, get_temprature_text(day), position)

def get_weather_icon_type(day):
    return day.dayIcon if isNight() else day.nightIcon

def get_column_width(origin, displaysize):
    return int ((displaysize[0] - origin[0])/3)

def draw_weather_day_icon(day, i, image, origin, displaysize):
    if day == None:
        return

    icon_name = get_weather_icon_name(day)
    icon_size = int(get_column_width(origin, displaysize) * .82 )
    position = (get_day_horiontal_origin(i, origin, displaysize), settings.weather_icon_offset + settings.weather_icon_indent_y + origin[1])
    draw.draw_icon(image, icon_name, position, (icon_size, icon_size))

def display_weather(image, origin, displaysize):
    forecast = weather.get_weather()
    draw_weather_data(image, forecast, origin, displaysize)

def draw_weather_grid(image, origin, displaysize):
    column_width = get_column_width(origin, displaysize)
    column_2_x = origin[0] + column_width
    column_3_x = origin[0] + (2 * column_width)

    draw.draw_line(image, (origin[0] + 7,  displaysize[1], column_2_x - 6,     displaysize[1]))
    draw.draw_line(image, (column_2_x + 7, displaysize[1], column_3_x - 6,     displaysize[1]))
    draw.draw_line(image, (column_2_x,     origin[1] + 5,  column_2_x,         displaysize[1] - 6))
    draw.draw_line(image, (column_3_x + 7, displaysize[1], displaysize[0] - 6, displaysize[1]))
    draw.draw_line(image, (column_3_x,     origin[1] + 5,  column_3_x,         displaysize[1] - 6))

def get_weather_icon_name(day):
    return 'WeatherIcons/' + icon_to_image(get_weather_icon_type(day))

def icon_to_image(icon):
    if(icon==1): # sunny
        return "2.bmp"
    if(icon==2): # mostly sunny
        return "2.bmp"
    if(icon==3): # partly sunny
        return "8.bmp"
    if(icon==4): # intermittent cloud
        return "8.bmp"
    if(icon==5): # hazy sunshine
        return "1.bmp"
    if(icon==6): # mostly cloudy
        return "8.bmp"
    if(icon==7): # cloudy
        return "14.bmp"
    if(icon==8): # dreary
        return "25.bmp"
    if(icon==11): # Fog
        return "13.bmp"
    if(icon==12): # Showers
        return "17.bmp"
    if(icon==13): # Mostly cloudy w/Showers
        return "8.bmp"
    if(icon==14): # Partly sunny w/showers
        return "17.bmp"
    if(icon==15): # T-Storms
        return "15.bmp"
    if(icon==16): # Mostly sunny w/T-Storms
        return "16.bmp"
    if(icon==17): # Partly Sunny w/T-Storms
        return "16.bmp"
    if(icon==18): # Rain
        return "17.bmp"
    if(icon==19): # Flurries
        return "21.bmp"
    if(icon==20): # Mostly sunny w/flurries
        return "22.bmp"
    if(icon==21): # Partly sunny w/flurries
        return "22.bmp"
    if(icon==22): # Snow
        return "23.bmp"
    if(icon==23): # Mostly cloudy w/snow
        return "21.bmp"
    if(icon==24): # Ice
        return "7.bmp"
    if(icon==25): # Sleet
        return "24.bmp"
    if(icon==26): # Freezing Rain
        return "23.bmp"
    if(icon==29): # Rain and Snow
        return "24.bmp"
    if(icon==30): # Hot
        return "2.bmp"
    if(icon==31): # Cold
        return "7.bmp"
    if(icon==32): # Windy
        return "6.bmp"
    if(icon==33): # Clear, Night
        return "3.bmp"
    if(icon==34): #	Mostly Clear, Night
        return "3.bmp"
    if(icon==35): # Partly Cloudy, Night
        return "9.bmp"
    if(icon==36): # Intermittent Clouds, Night
        return "19.bmp"
    if(icon==37): # Hazy Moonlight, Night
        return "5.bmp"
    if(icon==38): #	Mostly Cloudy, Night
        return "25.bmp"
    if(icon==39): #	Partly Cloudy w/ Showers, Night
        return "17.bmp"
    if(icon==40): #	Mostly Cloudy w/ Showers, Night
        return "18.bmp"
    if(icon==41): # Partly Cloudy w/ T-Storms, Night
        return "15.bmp"
    if(icon==42): # Mostly Cloudy w/ T-Storms, Night
        return "16.bmp"
    if(icon==43): # Mostly Cloudy w/ Flurries, Night
        return "21.bmp"
    if(icon==44): # Mostly Cloudy w/ Snow, Night
        return "22.bmp"
    return "4.bmp"