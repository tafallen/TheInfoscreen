from PIL import Image, ImageDraw, ImageFont
import settings

font_name = "./fonts/Oxygen-Regular.ttf"
mono_font_name = "./fonts/OxygenMono-Regular.ttf"
font_colour = 255

## Helper Methods #############################################################
def get_background(screen_size):
    return Image.new('L', screen_size, font_colour)

def get_font(size, font = font_name):
    return ImageFont.truetype(font, size)

def get_text_size(image, text, size):
    d = ImageDraw.Draw(image)
    return d.textsize(text = text, font = get_font(size))

def create_display(displaysize):
    return get_background(displaysize)

def get_resized_icon(icon_file, icon_dimensions):
    original_icon = Image.open(icon_file)
    return original_icon.resize(icon_dimensions)

def get_center_positon(image, text, font_size, origin, panel):
    size = get_text_size(image, text, font_size)
    width = size[0]
    avail = panel[0] - origin[0]
    return int((avail - width)/2)

def get_right_align_positon(image, text, font_size, origin, panel):
    size = get_text_size(image, text, font_size)
    avail = panel[0] - origin[0]
    return avail - size[0]

## Primitive Drawing Methods ##################################################
def draw_line(image, line):
    d = ImageDraw.Draw(image)
    d.line(line, fill=settings.line_fill, width=settings.line_width)

def draw_text(image, text, origin, size, font = font_name):
    d = ImageDraw.Draw(image)
    d.text(origin, text, font=get_font(size, font), fill=0)

## Applied Drawing Methods ####################################################
def draw_icon(image, icon_file, origin, icon_dimensions):
    box = (origin[0], origin[1], origin[0] + icon_dimensions[0], origin[1] + icon_dimensions[1])
    image.paste(get_resized_icon(icon_file, icon_dimensions), box)

def draw_footer(image, origin, panel):
    y = origin[1] + panel[1]
    line = (origin[0] + settings.divider_indent_x, y, panel[0] - settings.divider_indent_x, y)
    draw_line(image, line)

def draw_section_header(image, text, origin):
    draw_text(image, text, origin, settings.title_font_size)

def draw_summary_header(image, text, origin):
    draw_text(image, text, origin, settings.summary_font_size)

def draw_text_line(image, text, origin):
    draw_text(image, text, origin, settings.text_font_size)

def draw_agenda_line(image, text, origin, font = mono_font_name):
    draw_text(image, text, origin, 12, font)

def draw_train_line(image, text, origin, font = mono_font_name):
    draw_text(image, text, origin, settings.train_font_size, font)

def draw_temp_line(image, text, origin):
    draw_text(image, text, origin, settings.temp_font_size)

def draw_centered_text(image, text, origin, panel_size, size):
    x = get_center_positon(image, text, size, origin, panel_size)
    draw_text(image, text, (origin[0] + x, origin[1]), settings.header_font_size)

def draw_grid(image):
    d = ImageDraw.Draw(image)
    x = 0
    while x <= settings.displaysize[0]:
        d.line([(x, 0),(x, settings.displaysize[1])], fill=0, width=1)
        x+=10
    y = 0
    while y <= settings.displaysize[1]:
        d.line([(0, y),(settings.displaysize[0], y)], fill=0, width=1)
        y+=10