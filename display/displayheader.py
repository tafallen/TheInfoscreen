import datetime
import draw
import settings

def get_day_suffix(b):
    if b.endswith('1'):
        return 'st'
    elif b.endswith('2'):
        return 'nd'
    elif b.endswith('3'):
        return 'rd'
    else:
        return 'th'

def get_displayable_date(timestamp):
    date = timestamp.strftime("%d").lstrip('0')
    return timestamp.strftime('%A') + ' ' + date + get_day_suffix(date) + ' ' + timestamp.strftime("%b")

def get_displayable_time(timestamp):
    time = timestamp.strftime("%I:%M").lstrip('0')
    p = timestamp.strftime("%p")
    return (time + p.lower())

def get_display_text():
    timestamp = datetime.datetime.now()
    return get_displayable_date(timestamp) + ' at ' + get_displayable_time(timestamp)

def display_header(image, origin, panel):
    draw.draw_centered_text(image, get_display_text(), origin, panel, settings.header_font_size)
    draw.draw_footer(image, origin, panel)

class Panel:
    def __init__(self, image):
        self.image = image

    def display(self, origin, panel):
        draw.draw_centered_text(self.image, get_display_text(), origin, panel, settings.header_font_size)
        draw.draw_footer(self.image, origin, panel)
