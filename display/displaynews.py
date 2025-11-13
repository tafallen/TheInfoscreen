"""This module is responsible for displaying the news section of the
display."""
import draw
import settings
import sys
import news

sys.path.insert(1, "./data")


def trim_headline(image, text, origin, displaysize):
    """Trim a headline to fit within the display.

    Args:
        image (Image): The image to draw on.
        text (str): The text to trim.
        origin (tuple): The origin coordinates of the news section.
        displaysize (tuple): The size of the news section.

    Returns:
        str: The trimmed headline.
    """
    avail = displaysize[0] - (origin[0] + settings.article_indent_x)
    width = draw.get_text_size(image, text, settings.text_font_size)[0]
    while width > avail:
        text = text[: (len(text) - 4)]
        text += "..."
        width = draw.get_text_size(image, text, settings.text_font_size)[0]
    return text


def draw_news_article(image, article, origin, displaysize, i):
    """Draw a single news article.

    Args:
        image (Image): The image to draw on.
        article (Article): The article to draw.
        origin (tuple): The origin coordinates of the news section.
        displaysize (tuple): The size of the news section.
        i (int): The index of the article.
    """
    text = trim_headline(image, article.title, origin, displaysize)
    position = (
        origin[0] + settings.article_indent_x,
        origin[1] + settings.article_indent_y + (settings.text_height * i),
    )
    draw.draw_text_line(image, text, position)


def draw_news_headlines(image, news, origin, displaysize):
    """Draw all the news headlines.

    Args:
        image (Image): The image to draw on.
        news (list): A list of Article objects.
        origin (tuple): The origin coordinates of the news section.
        displaysize (tuple): The size of the news section.
    """
    i = 0
    while i < settings.article_limit:
        draw_news_article(image, news[i], origin, displaysize, i)
        i += 1


def display_news(image, origin, displaysize):
    """Display the news section.

    Args:
        image (Image): The image to draw on.
        origin (tuple): The origin coordinates of the news section.
        displaysize (tuple): The size of the news section.
    """
    articles = news.get_news()

    draw.draw_section_header(
        image,
        settings.title_prefix,
        (origin[0] + settings.travel_title_indent_x, origin[1]),
    )

    draw.draw_footer(image, origin, displaysize)

    draw_news_headlines(image, articles, origin, displaysize)
