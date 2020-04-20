
experimental = False#True

## Panel Size #################################################################
displaysize = (384, 640)

## Panel Locations ############################################################
header_location = (10, 10)
header_size = (374, 35)

weather_location = (10,55)
weather_size = (374, 246)

news_location = (10,258)
news_size = (374, 180)

trains_location = (10, 455)
trains_size = (374, 100)

heating_location = (10,555)
heating_size = (374, 70)
###############################################################################

line_width = 2
line_fill = 128

header_font_size = 24
title_font_size = 18
temp_font_size = 16
text_font_size = 14
train_font_size = 13
summary_font_size = 11

text_height = 24

divider_indent_x = 8

## News Panel #################################################################
title_prefix = 'News'
title_indent_x = 6

article_indent_x = 15
article_indent_y = 30
article_limit = 6
###############################################################################

## Train Panel ################################################################
travel_title_indent_x = 10
travel_title_indent_y = 430
travel_sub_title_indent_y = 0

service_limit = 3
service_indent = 20
service_times_indent = 5
service_column_width = 182

service_line_prefix = 'Due: '
source_crs = 'SWN'
dest_crs = 'MHS'
###############################################################################

## Weather Panel ##############################################################
temp_units = '°C'
temp_indent_y = 140
temp_separator = '/'

day_indent_y = 6

summary_indent_x = 2
summary_indent_line1_y = 158
summary_indent_line2_y = summary_indent_line1_y + 14

weather_offset = 122
weather_content_indent = 10
weather_icon_size = 100
weather_icon_offset = int((weather_offset - weather_icon_size)/2)
weather_icon_indent_y = 15

weather_start_indent_y = 5
weather_end_indent_y = weather_start_indent_y + 180
weather_divider_indent_x = 6
weather_divider_indent_y = weather_end_indent_y + weather_divider_indent_x
###############################################################################

## Heating Panel ##############################################################
thermostat_name = 'Thermostat 2'
x_offset = 50
y1 = 25
y2 = 35
heating_icon_size = 50
heating_icon_indent = 10


## Countdown
countdown_targetdate = '14/04/2020'
countdown_event = 'Lockdown reviewed'

