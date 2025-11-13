"""This module is responsible for displaying the weather section of the
display."""
import sys
import weather
import sunset
import draw
import datetime
import settings

sys.path.insert(1, "./data")


def isNight():
    """Check if it is currently night.

    Returns:
        bool: True if it is night, False otherwise.
    """
    return sunset.get_sunset().isNight()


def draw_weather_day(image, day, i, origin, displaysize):
    """Draw a single day's weather forecast.

    Args:
        image (Image): The image to draw on.
        day (Day): The day's weather forecast to draw.
        i (int): The index of the day.
        origin (tuple): The origin coordinates of the weather section.
        displaysize (tuple): The size of the weather section.
    """
    draw_weather_day_title(i, image, origin, displaysize)
    draw_weather_day_icon(day, i, image, origin, displaysize)
    draw_weather_day_temp(day, i, image, origin, displaysize)
    draw_weather_day_summary(day, i, image, origin, displaysize)
    draw_weather_grid(image, origin, displaysize)


def get_day_horiontal_origin(i, origin, displaysize):
    """Get the horizontal origin for a a given day.

    Args:
        i (int): The index of the day.
        origin (tuple): The origin coordinates of the weather section.
        displaysize (tuple): The size of the weather section.

    Returns:
        int: The horizontal origin for the day.
    """
    column_width = int((displaysize[0] - origin[0]) / 3)
    return origin[0] + settings.weather_content_indent + (i * column_width)


def draw_weather_data(image, forecast, origin, displaysize):
    """Draw the weather data for all days.

    Args:
        image (Image): The image to draw on.
        forecast (list): A list of Day objects.
        origin (tuple): The origin coordinates of the weather section.
        displaysize (tuple): The size of the weather section.
    """
    i = 0
    have_forecast = False if len(forecast) == 0 else True

    while i < 3:
        day = forecast[i] if have_forecast else None
        draw_weather_day(image, day, i, origin, displaysize)
        i += 1


def draw_weather_day_title(i, image, origin, displaysize):
    """Draw the title for a given day.

    Args:
        i (int): The index of the day.
        image (Image): The image to draw on.
        origin (tuple): The origin coordinates of the weather section.
        displaysize (tuple): The size of the weather section.
    """
    day_text = (datetime.datetime.now() + datetime.timedelta(days=i)).strftime(
        "%A"
    )
    position = (
        get_day_horiontal_origin(i, origin, displaysize),
        settings.day_indent_y + origin[1],
    )
    draw.draw_temp_line(image, day_text, position)


def draw_weather_day_summary(day, i, image, origin, displaysize):
    """Draw the summary for a given day.

    Args:
        day (Day): The day's weather forecast to draw.
        i (int): The index of the day.
        image (Image): The image to draw on.
        origin (tuple): The origin coordinates of the weather section.
        displaysize (tuple): The size of the weather section.
    """
    x = get_day_horiontal_origin(i, origin, displaysize)
    line1_position = (
        x + settings.summary_indent_x,
        settings.summary_indent_line1_y + origin[1],
    )
    line2_position = (
        x + settings.summary_indent_x,
        settings.summary_indent_line2_y + origin[1],
    )

    if day is None:
        draw.draw_summary_header(image, "?", line1_position)
        return

    # TODO: get the col width and use it to calculate the line break
    # Steal the code from elsewhere in the project and generalise
    if len(day.summary) > 20:
        line_break = day.summary.rfind(" ", 0, 19)
        draw.draw_summary_header(
            image, day.summary[:line_break], line1_position
        )
        draw.draw_summary_header(
            image, day.summary[line_break + 1:], line2_position
        )
    else:
        draw.draw_summary_header(image, day.summary, line1_position)


def get_temprature_text(day):
    """Get the temperature text for a given day.

    Args:
        day (Day): The day's weather forecast to get the temperature text
                    for.

    Returns:
        str: The temperature text.
    """
    return (
        "?"
        if day is None
        else day.tempMax
        + settings.temp_units
        + settings.temp_separator
        + day.tempMin
        + settings.temp_units
    )


def draw_weather_day_temp(day, i, image, origin, displaysize):
    """Draw the temperature for a given day.

    Args:
        day (Day): The day's weather forecast to draw.
        i (int): The index of the day.
        image (Image): The image to draw on.
        origin (tuple): The origin coordinates of the weather section.
        displaysize (tuple): The size of the weather section.
    """
    position = (
        get_day_horiontal_origin(i, origin, displaysize),
        settings.temp_indent_y + origin[1],
    )
    draw.draw_temp_line(image, get_temprature_text(day), position)


def get_weather_icon_type(day):
    """Get the weather icon type for a given day.

    Args:
        day (Day): The day's weather forecast to get the icon type for.

    Returns:
        int: The weather icon type.
    """
    return day.dayIcon if isNight() else day.nightIcon


def get_column_width(origin, displaysize):
    """Get the width of a column.

    Args:
        origin (tuple): The origin coordinates of the weather section.
        displaysize (tuple): The size of the weather section.

    Returns:
        int: The width of a column.
    """
    return int((displaysize[0] - origin[0]) / 3)


def draw_weather_day_icon(day, i, image, origin, displaysize):
    """Draw the icon for a given day.

    Args:
        day (Day): The day's weather forecast to draw.
        i (int): The index of the day.
        image (Image): The image to draw on.
        origin (tuple): The origin coordinates of the weather section.
        displaysize (tuple): The size of the weather section.
    """
    if day is None:
        return

    icon_name = get_weather_icon_name(day)
    icon_size = int(get_column_width(origin, displaysize) * 0.82)
    position = (
        get_day_horiontal_origin(i, origin, displaysize),
        settings.weather_icon_offset
        + settings.weather_icon_indent_y
        + origin[1],
    )
    draw.draw_icon(image, icon_name, position, (icon_size, icon_size))


def display_weather(image, origin, displaysize):
    """Display the weather section.

    Args:
        image (Image): The image to draw on.
        origin (tuple): The origin coordinates of the weather section.
        displaysize (tuple): The size of the weather section.
    """
    forecast = weather.get_weather()
    draw_weather_data(image, forecast, origin, displaysize)


def draw_weather_grid(image, origin, displaysize):
    """Draw the grid for the weather section.

    Args:
        image (Image): The image to draw on.
        origin (tuple): The origin coordinates of the weather section.
        displaysize (tuple): The size of the weather section.
    """
    column_width = get_column_width(origin, displaysize)
    column_2_x = origin[0] + column_width
    column_3_x = origin[0] + (2 * column_width)

    draw.draw_line(
        image,
        (origin[0] + 7, displaysize[1], column_2_x - 6, displaysize[1]),
    )
    draw.draw_line(
        image,
        (column_2_x + 7, displaysize[1], column_3_x - 6, displaysize[1]),
    )
    draw.draw_line(
        image, (column_2_x, origin[1] + 5, column_2_x, displaysize[1] - 6)
    )
    draw.draw_line(
        image,
        (
            column_3_x + 7,
            displaysize[1],
            displaysize[0] - 6,
            displaysize[1],
        ),
    )
    draw.draw_line(
        image, (column_3_x, origin[1] + 5, column_3_x, displaysize[1] - 6)
    )


def get_weather_icon_name(day):
    """Get the name of the weather icon for a given day.

    Args:
        day (Day): The day's weather forecast to get the icon name for.

    Returns:
        str: The name of the weather icon.
    """
    return "WeatherIcons/" + icon_to_image(get_weather_icon_type(day))


def icon_to_image(icon):
    """Convert a weather icon type to an image filename.

    Args:
        icon (int): The weather icon type.

    Returns:
        str: The filename of the weather icon image.
    """
    # sunny
    if icon == 1:
        return "2.bmp"
    # mostly sunny
    if icon == 2:
        return "2.bmp"
    # partly sunny
    if icon == 3:
        return "8.bmp"
    # intermittent cloud
    if icon == 4:
        return "8.bmp"
    # hazy sunshine
    if icon == 5:
        return "1.bmp"
    # mostly cloudy
    if icon == 6:
        return "8.bmp"
    # cloudy
    if icon == 7:
        return "14.bmp"
    # dreary
    if icon == 8:
        return "25.bmp"
    # Fog
    if icon == 11:
        return "13.bmp"
    # Showers
    if icon == 12:
        return "17.bmp"
    # Mostly cloudy w/Showers
    if icon == 13:
        return "8.bmp"
    # Partly sunny w/showers
    if icon == 14:
        return "17.bmp"
    # T-Storms
    if icon == 15:
        return "15.bmp"
    # Mostly sunny w/T-Storms
    if icon == 16:
        return "16.bmp"
    # Partly Sunny w/T-Storms
    if icon == 17:
        return "16.bmp"
    # Rain
    if icon == 18:
        return "17.bmp"
    # Flurries
    if icon == 19:
        return "21.bmp"
    # Mostly sunny w/flurries
    if icon == 20:
        return "22.bmp"
    # Partly sunny w/flurries
    if icon == 21:
        return "22.bmp"
    # Snow
    if icon == 22:
        return "23.bmp"
    # Mostly cloudy w/snow
    if icon == 23:
        return "21.bmp"
    # Ice
    if icon == 24:
        return "7.bmp"
    # Sleet
    if icon == 25:
        return "24.bmp"
    # Freezing Rain
    if icon == 26:
        return "23.bmp"
    # Rain and Snow
    if icon == 29:
        return "24.bmp"
    # Hot
    if icon == 30:
        return "2.bmp"
    # Cold
    if icon == 31:
        return "7.bmp"
    # Windy
    if icon == 32:
        return "6.bmp"
    # Clear, Night
    if icon == 33:
        return "3.bmp"
    # 	Mostly Clear, Night
    if icon == 34:
        return "3.bmp"
    # Partly Cloudy, Night
    if icon == 35:
        return "9.bmp"
    # Intermittent Clouds, Night
    if icon == 36:
        return "19.bmp"
    # Hazy Moonlight, Night
    if icon == 37:
        return "5.bmp"
    # 	Mostly Cloudy, Night
    if icon == 38:
        return "25.bmp"
    # 	Partly Cloudy w/ Showers, Night
    if icon == 39:
        return "17.bmp"
    # 	Mostly Cloudy w/ Showers, Night
    if icon == 40:
        return "18.bmp"
    # Partly Cloudy w/ T-Storms, Night
    if icon == 41:
        return "15.bmp"
    # Mostly Cloudy w/ T-Storms, Night
    if icon == 42:
        return "16.bmp"
    # Mostly Cloudy w/ Flurries, Night
    if icon == 43:
        return "21.bmp"
    # Mostly Cloudy w/ Snow, Night
    if icon == 44:
        return "22.bmp"
    return "4.bmp"
