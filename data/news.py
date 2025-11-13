"""This module provides functions for fetching news headlines from the News
API."""
from __future__ import print_function
from newsapi import NewsApiClient
import apis
import infologging as log


def get_client():
    """Get a NewsApiClient instance.

    Returns:
        NewsApiClient: An instance of the NewsApiClient.
    """
    return NewsApiClient(api_key=apis.news_key)


def get_headlines(news_client=get_client()):
    """Get the top headlines from BBC News.

    Args:
        news_client (NewsApiClient): The NewsApiClient instance to use.

    Returns:
        dict: A dictionary containing the top headlines.
    """
    return news_client.get_top_headlines(sources="bbc-news")


def get_news(headlines_provider=get_headlines):
    """Get a list of news articles.

    Args:
        headlines_provider (function): The function to use for getting the
                                        headlines.

    Returns:
        list: A list of Article objects.
    """
    log.log_message("news: Getting news")
    headlines = headlines_provider()

    articleCount = headlines["totalResults"]
    result = []

    log.log_message("news: Collating headlines")
    i = 0
    while i < articleCount:
        article = Article(headlines["articles"][i])
        result.append(article)
        i += 1

    log.log_message("news: Returning headlines")
    return result


class Article:
    """A class to represent a news article."""

    def __init__(self, article_json):
        """Initialize the Article object.

        Args:
            article_json (dict): The JSON object representing the article.
        """
        self.author = article_json["author"]
        self.title = article_json["title"]
        self.description = article_json["description"]
        self.publicationDate = article_json["publishedAt"]

    def dump(self):
        """Print the article to the console."""
        print(self.author + ": " + self.title)
        print(self.description)
        print(self.publicationDate)
