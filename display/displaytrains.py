import sys
sys.path.insert(1, './data')
import trains
import datetime
import draw 
import settings

def draw_train_service_header(image, source, dest, column, origin):
    position = (origin[0] + settings.service_indent + (column * settings.service_column_width), origin[1] + settings.travel_sub_title_indent_y)
    draw.draw_text_line(image, source + ' to ' + dest, position)

def draw_train_service_time(image, service, origin, column, i):
    train_service = settings.service_line_prefix
    position = (origin[0] + settings.service_indent + settings.service_times_indent + (column * settings.service_column_width), origin[1] + settings.travel_sub_title_indent_y + (settings.text_height * (i +1)))
    draw.draw_train_line(image, train_service, position, draw.font_name)
    if service.etd == 'On time' or service.etd == 'Cancelled':
        draw.draw_train_line(image, service.std, (position[0]+30, position[1] + 1))
        draw.draw_train_line(image, service.etd, (position[0]+80, position[1]), font=draw.font_name)
    else:
        draw.draw_train_line(image, service.std + ' ' + service.etd, (position[0]+29, position[1] + 1))

def draw_train_service_times(image, services, count, column, origin):
    i = 0
    while i < count:
        draw_train_service_time(image, services[i], origin, column, i)
        i += 1

def get_service_count(board):
    services_to_display = len(board.train_services)

    if services_to_display > settings.service_limit:
        services_to_display = settings.service_limit
    return services_to_display

def display_train_services(image, source, dest, column, origin):
    board = trains.get_train_times(source, dest)
    services_to_display = get_service_count(board)

    draw_train_service_header(image, source, dest, column, origin)
    draw_train_service_times(image, board.train_services, services_to_display, column, origin)

def display_trains(image, origin, displaysize):
    display_train_services(image, settings.source_crs, settings.dest_crs, 0, (origin[0] + 35, origin[1]))
    display_train_services(image, settings.dest_crs, settings.source_crs, 1, (origin[0] + 5, origin[1]))
    draw.draw_icon(image, 'icons/train.bmp', (origin[0]+5,origin[1]), (50, 50))
    draw.draw_footer(image, origin, displaysize)