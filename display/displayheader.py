"""This module is responsible for displaying the header section of the
display."""
import datetime
import draw
import settings


def get_day_suffix(b):
    """Get the suffix for a given day of the month.

    Args:
        b (str): The day of the month.

    Returns:
        str: The suffix for the day of the month.
    """
    if b.endswith("1"):
        return "st"
    elif b.endswith("2"):
        return "nd"
    elif b.endswith("3"):
        return "rd"
    else:
        return "th"


def get_displayable_date(timestamp):
    """Get a displayable date string from a timestamp.

    Args:
        timestamp (datetime): The timestamp to convert.

    Returns:
        str: A displayable date string.
    """
    date = timestamp.strftime("%d").lstrip("0")
    day_of_week = timestamp.strftime("%A")
    month = timestamp.strftime("%b")
    return f"{day_of_week} {date}{get_day_suffix(date)} {month}"


def get_displayable_time(timestamp):
    """Get a displayable time string from a timestamp.

    Args:
        timestamp (datetime): The timestamp to convert.

    Returns:
        str: A displayable time string.
    """
    time = timestamp.strftime("%I:%M").lstrip("0")
    p = timestamp.strftime("%p")
    return time + p.lower()


def get_display_text():
    """Get the full display text for the header.

    Returns:
        str: The full display text for the header.
    """
    timestamp = datetime.datetime.now()
    date_str = get_displayable_date(timestamp)
    time_str = get_displayable_time(timestamp)
    return f"{date_str} at {time_str}"


def display_header(image, origin, panel):
    """Display the header section.

    Args:
        image (Image): The image to draw on.
        origin (tuple): The origin coordinates of the header section.
        panel (tuple): The size of the header section.
    """
    draw.draw_centered_text(
        image, get_display_text(), origin, panel, settings.header_font_size
    )
    draw.draw_footer(image, origin, panel)


class Panel:
    """A class to represent the header panel."""

    def __init__(self, image):
        """Initialize the Panel object.

        Args:
            image (Image): The image to draw on.
        """
        self.image = image

    def display(self, origin, panel):
        """Display the header panel.

        Args:
            origin (tuple): The origin coordinates of the header panel.
            panel (tuple): The size of the header panel.
        """
        draw.draw_centered_text(
            self.image,
            get_display_text(),
            origin,
            panel,
            settings.header_font_size,
        )
        draw.draw_footer(self.image, origin, panel)
