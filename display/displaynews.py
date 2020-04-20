import draw
import datetime
import settings
import sys
sys.path.insert(1, './data')
import news

def trim_headline(image, text, origin, displaysize):
    avail = displaysize[0] - (origin[0] + settings.article_indent_x)
    width = draw.get_text_size(image, text, settings.text_font_size)[0]
    while width > avail: 
        text = text[:(len(text)-4)]
        text += '...'
        width = draw.get_text_size(image, text, settings.text_font_size)[0]
    return text

def draw_news_article(image, article, origin, displaysize, i):
    text = trim_headline(image, article.title, origin, displaysize)
    position = (origin[0] + settings.article_indent_x, origin[1] + settings.article_indent_y + (settings.text_height * i))
    draw.draw_text_line(image, text, position)

def draw_news_headlines(image, news, origin, displaysize):
    i = 0
    while i < settings.article_limit:
        draw_news_article(image, news[i], origin, displaysize, i)
        i += 1

def display_news(image, origin, displaysize):
    articles = news.get_news()

    draw.draw_section_header(image, settings.title_prefix, (origin[0] + settings.travel_title_indent_x, origin[1]))

    draw.draw_footer(image, origin, displaysize)    

    draw_news_headlines(image, articles, origin, displaysize)