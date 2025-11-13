"""This module provides low-level drawing functions for the display."""
from PIL import Image, ImageDraw, ImageFont
import settings

font_name = "./fonts/Oxygen-Regular.ttf"
mono_font_name = "./fonts/OxygenMono-Regular.ttf"
font_colour = 255


# Helper Methods
def get_background(screen_size):
    """Get a new blank image.

    Args:
        screen_size (tuple): The size of the image to create.

    Returns:
        Image: A new blank image.
    """
    return Image.new("L", screen_size, font_colour)


def get_font(size, font=font_name):
    """Get a font object.

    Args:
        size (int): The size of the font.
        font (str, optional): The name of the font. Defaults to font_name.

    Returns:
        FreeTypeFont: A font object.
    """
    return ImageFont.truetype(font, size)


def get_text_size(image, text, size):
    """Get the size of a string of text.

    Args:
        image (Image): The image to draw on.
        text (str): The text to measure.
        size (int): The size of the font.

    Returns:
        tuple: The width and height of the text.
    """
    d = ImageDraw.Draw(image)
    return d.textbbox(xy=(0, 0), text=text, font=get_font(size))[2:]


def create_display(displaysize):
    """Create a new blank display image.

    Args:
        displaysize (tuple): The size of the display.

    Returns:
        Image: A new blank display image.
    """
    return get_background(displaysize)


def get_resized_icon(icon_file, icon_dimensions):
    """Get a resized icon image.

    Args:
        icon_file (str): The path to the icon file.
        icon_dimensions (tuple): The desired dimensions of the icon.

    Returns:
        Image: A resized icon image.
    """
    original_icon = Image.open(icon_file)
    return original_icon.resize(icon_dimensions)


def get_center_positon(image, text, font_size, origin, panel):
    """Get the x-coordinate for centered text.

    Args:
        image (Image): The image to draw on.
        text (str): The text to center.
        font_size (int): The size of the font.
        origin (tuple): The origin coordinates of the panel.
        panel (tuple): The size of the panel.

    Returns:
        int: The x-coordinate for the centered text.
    """
    size = get_text_size(image, text, font_size)
    width = size[0]
    avail = panel[0] - origin[0]
    return int((avail - width) / 2)


def get_right_align_positon(image, text, font_size, origin, panel):
    """Get the x-coordinate for right-aligned text.

    Args:
        image (Image): The image to draw on.
        text (str): The text to right-align.
        font_size (int): The size of the font.
        origin (tuple): The origin coordinates of the panel.
        panel (tuple): The size of the panel.

    Returns:
        int: The x-coordinate for the right-aligned text.
    """
    size = get_text_size(image, text, font_size)
    avail = panel[0] - origin[0]
    return avail - size[0]


# Primitive Drawing Methods
def draw_line(image, line):
    """Draw a line on the image.

    Args:
        image (Image): The image to draw on.
        line (tuple): The coordinates of the line.
    """
    d = ImageDraw.Draw(image)
    d.line(line, fill=settings.line_fill, width=settings.line_width)


def draw_text(image, text, origin, size, font=font_name):
    """Draw text on the image.

    Args:
        image (Image): The image to draw on.
        text (str): The text to draw.
        origin (tuple): The coordinates to draw the text at.
        size (int): The size of the font.
        font (str, optional): The name of the font. Defaults to font_name.
    """
    d = ImageDraw.Draw(image)
    d.text(origin, text, font=get_font(size, font), fill=0)


# Applied Drawing Methods
def draw_icon(image, icon_file, origin, icon_dimensions):
    """Draw an icon on the image.

    Args:
        image (Image): The image to draw on.
        icon_file (str): The path to the icon file.
        origin (tuple): The coordinates to draw the icon at.
        icon_dimensions (tuple): The dimensions of the icon.
    """
    box = (
        origin[0],
        origin[1],
        origin[0] + icon_dimensions[0],
        origin[1] + icon_dimensions[1],
    )
    image.paste(get_resized_icon(icon_file, icon_dimensions), box)


def draw_footer(image, origin, panel):
    """Draw a footer line.

    Args:
        image (Image): The image to draw on.
        origin (tuple): The origin coordinates of the panel.
        panel (tuple): The size of the panel.
    """
    y = origin[1] + panel[1]
    line = (
        origin[0] + settings.divider_indent_x,
        y,
        panel[0] - settings.divider_indent_x,
        y,
    )
    draw_line(image, line)


def draw_section_header(image, text, origin):
    """Draw a section header.

    Args:
        image (Image): The image to draw on.
        text (str): The text to draw.
        origin (tuple): The coordinates to draw the text at.
    """
    draw_text(image, text, origin, settings.title_font_size)


def draw_summary_header(image, text, origin):
    """Draw a summary header.

    Args:
        image (Image): The image to draw on.
        text (str): The text to draw.
        origin (tuple): The coordinates to draw the text at.
    """
    draw_text(image, text, origin, settings.summary_font_size)


def draw_text_line(image, text, origin):
    """Draw a line of text.

    Args:
        image (Image): The image to draw on.
        text (str): The text to draw.
        origin (tuple): The coordinates to draw the text at.
    """
    draw_text(image, text, origin, settings.text_font_size)


def draw_agenda_line(image, text, origin, font=mono_font_name):
    """Draw a line of agenda text.

    Args:
        image (Image): The image to draw on.
        text (str): The text to draw.
        origin (tuple): The coordinates to draw the text at.
        font (str, optional): The name of the font. Defaults to
                                mono_font_name.
    """
    draw_text(image, text, origin, 12, font)


def draw_train_line(image, text, origin, font=mono_font_name):
    """Draw a line of train text.

    Args:
        image (Image): The image to draw on.
        text (str): The text to draw.
        origin (tuple): The coordinates to draw the text at.
        font (str, optional): The name of the font. Defaults to
                                mono_font_name.
    """
    draw_text(image, text, origin, settings.train_font_size, font)


def draw_temp_line(image, text, origin):
    """Draw a line of temperature text.

    Args:
        image (Image): The image to draw on.
        text (str): The text to draw.
        origin (tuple): The coordinates to draw the text at.
    """
    draw_text(image, text, origin, settings.temp_font_size)


def draw_centered_text(image, text, origin, panel_size, size):
    """Draw centered text.

    Args:
        image (Image): The image to draw on.
        text (str): The text to draw.
        origin (tuple): The origin coordinates of the panel.
        panel_size (tuple): The size of the panel.
        size (int): The size of the font.
    """
    x = get_center_positon(image, text, size, origin, panel_size)
    draw_text(
        image, text, (origin[0] + x, origin[1]), settings.header_font_size
    )


def draw_grid(image):
    """Draw a grid on the image for debugging purposes.

    Args:
        image (Image): The image to draw on.
    """
    d = ImageDraw.Draw(image)
    x = 0
    while x <= settings.displaysize[0]:
        d.line([(x, 0), (x, settings.displaysize[1])], fill=0, width=1)
        x += 10
    y = 0
    while y <= settings.displaysize[1]:
        d.line([(0, y), (settings.displaysize[0], y)], fill=0, width=1)
        y += 10
