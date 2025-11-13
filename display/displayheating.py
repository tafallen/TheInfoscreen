"""This module is responsible for displaying the heating section of the
display."""
import draw
import settings
import sys
import hive

sys.path.insert(1, "./data")


def draw_icon(image, origin, state):
    """Draw the heating icon.

    Args:
        image (Image): The image to draw on.
        origin (tuple): The origin coordinates of the heating icon.
        state (Thermostat): The current state of the thermostat.
    """
    icon_file = "icons/heat off.bmp"
    if state.mode == "BOOST" or state.state == "ON":
        icon_file = "icons/heat on.bmp"

    draw.draw_icon(
        image,
        icon_file,
        (origin[0] + settings.heating_icon_indent, origin[1] + 10),
        (settings.heating_icon_size, settings.heating_icon_size),
    )


def get_temprature_text(state):
    """Get the temperature text.

    Args:
        state (Thermostat): The current state of the thermostat.

    Returns:
        str: The temperature text.
    """
    return (
        state.temp_current
        + settings.temp_units
        + " >> "
        + state.temp_target
        + settings.temp_units
    )


def draw_temperatures(image, origin, state):
    """Draw the temperatures.

    Args:
        image (Image): The image to draw on.
        origin (tuple): The origin coordinates of the temperatures.
        state (Thermostat): The current state of the thermostat.
    """
    text = get_temprature_text(state)
    draw.draw_text(
        image,
        text,
        (origin[0] + settings.x_offset + 20, origin[1] + settings.y1),
        28,
    )


def draw_temperatures_experimental(image, state):
    """Draw the temperatures (experimental).

    Args:
        image (Image): The image to draw on.
        state (Thermostat): The current state of the thermostat.
    """
    draw_icon(image, (220, 145), state)
    draw.draw_text_line(image, get_temprature_text(state), (280, 180))


def display_heating(image, origin, panel):
    """Display the heating section.

    Args:
        image (Image): The image to draw on.
        origin (tuple): The origin coordinates of the heating section.
        panel (tuple): The size of the heating section.
    """
    state = hive.get_heating_state()
    if settings.experimental:
        draw_temperatures_experimental(image, state)
    else:
        draw_temperatures(image, origin, state)
        draw_icon(image, origin, state)
