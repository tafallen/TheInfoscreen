from __future__ import print_function
from newsapi import NewsApiClient
import apis
import infologging as log

def get_client():
    return NewsApiClient(api_key=apis.news_key)

def get_headlines(news_client=get_client()):
    return news_client.get_top_headlines(sources='bbc-news')

def get_news(headlines_provider=get_headlines):
    log.log_message('news: Getting news')
    headlines = headlines_provider()

    articleCount = headlines['totalResults']
    result = []

    log.log_message('news: Collating headlines')
    i=0
    while( i < articleCount ):
        article = Article( headlines['articles'][i] )
        result.append(article)
        i+=1

    log.log_message('news: Returning headlines')
    return result

class Article:
    def __init__(self, article_json):
        self.author = article_json['author']
        self.title = article_json['title']
        self.description = article_json['description']
        self.publicationDate = article_json['publishedAt']

    def dump(self):
        print(self.author + ': ' + self.title)
        print(self.description)
        print(self.publicationDate)