"""This module is responsible for displaying the train times section of the
display."""
import sys
import trains
import draw
import settings

sys.path.insert(1, "./data")


def draw_train_service_header(image, source, dest, column, origin):
    """Draw the header for a train service.

    Args:
        image (Image): The image to draw on.
        source (str): The source station CRS code.
        dest (str): The destination station CRS code.
        column (int): The column to draw the header in.
        origin (tuple): The origin coordinates of the train times section.
    """
    position = (
        origin[0]
        + settings.service_indent
        + (column * settings.service_column_width),
        origin[1] + settings.travel_sub_title_indent_y,
    )
    draw.draw_text_line(image, source + " to " + dest, position)


def draw_train_service_time(image, service, origin, column, i):
    """Draw a single train service time.

    Args:
        image (Image): The image to draw on.
        service (Service): The service to draw.
        origin (tuple): The origin coordinates of the train times section.
        column (int): The column to draw the service time in.
        i (int): The index of the service time.
    """
    train_service = settings.service_line_prefix
    position = (
        origin[0]
        + settings.service_indent
        + settings.service_times_indent
        + (column * settings.service_column_width),
        origin[1]
        + settings.travel_sub_title_indent_y
        + (settings.text_height * (i + 1)),
    )
    draw.draw_train_line(image, train_service, position, draw.font_name)
    if service.etd == "On time" or service.etd == "Cancelled":
        draw.draw_train_line(
            image, service.std, (position[0] + 30, position[1] + 1)
        )
        draw.draw_train_line(
            image,
            service.etd,
            (position[0] + 80, position[1]),
            font=draw.font_name,
        )
    else:
        draw.draw_train_line(
            image,
            service.std + " " + service.etd,
            (position[0] + 29, position[1] + 1),
        )


def draw_train_service_times(image, services, count, column, origin):
    """Draw all the train service times.

    Args:
        image (Image): The image to draw on.
        services (list): A list of Service objects.
        count (int): The number of services to draw.
        column (int): The column to draw the service times in.
        origin (tuple): The origin coordinates of the train times section.
    """
    i = 0
    while i < count:
        draw_train_service_time(image, services[i], origin, column, i)
        i += 1


def get_service_count(board):
    """Get the number of services to display.

    Args:
        board (StationBoard): The station board to get the service count
                                from.

    Returns:
        int: The number of services to display.
    """
    services_to_display = len(board.train_services)

    if services_to_display > settings.service_limit:
        services_to_display = settings.service_limit
    return services_to_display


def display_train_services(image, source, dest, column, origin):
    """Display the train services for a given route.

    Args:
        image (Image): The image to draw on.
        source (str): The source station CRS code.
        dest (str): The destination station CRS code.
        column (int): The column to draw the services in.
        origin (tuple): The origin coordinates of the train times section.
    """
    board = trains.get_train_times(source, dest)
    services_to_display = get_service_count(board)

    draw_train_service_header(image, source, dest, column, origin)
    draw_train_service_times(
        image, board.train_services, services_to_display, column, origin
    )


def display_trains(image, origin, displaysize):
    """Display the train times section.

    Args:
        image (Image): The image to draw on.
        origin (tuple): The origin coordinates of the train times section.
        displaysize (tuple): The size of the train times section.
    """
    display_train_services(
        image,
        settings.source_crs,
        settings.dest_crs,
        0,
        (origin[0] + 35, origin[1]),
    )
    display_train_services(
        image,
        settings.dest_crs,
        settings.source_crs,
        1,
        (origin[0] + 5, origin[1]),
    )
    draw.draw_icon(
        image, "icons/train.bmp", (origin[0] + 5, origin[1]), (50, 50)
    )
    draw.draw_footer(image, origin, displaysize)
