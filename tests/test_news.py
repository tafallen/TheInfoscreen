import unittest
from unittest.mock import Mock
import sys
sys.path.insert(1, './data')
sys.path.insert(1, './')
import news

class TestNews(unittest.TestCase):

    def test_get_news(self):
        # Create a mock headlines provider
        mock_headlines = {
            "totalResults": 1,
            "articles": [
                {
                    "author": "BBC News",
                    "title": "Test Title",
                    "description": "Test Description",
                    "publishedAt": "2024-01-01T12:00:00Z"
                }
            ]
        }

        mock_provider = Mock(return_value=mock_headlines)

        # Call the get_news function with the mock provider
        articles = news.get_news(headlines_provider=mock_provider)

        # Assert that the articles list is not empty
        self.assertIsNotNone(articles)
        self.assertEqual(len(articles), 1)

        # Assert that the Article object has the correct data
        article = articles[0]
        self.assertEqual(article.author, "BBC News")
        self.assertEqual(article.title, "Test Title")
        self.assertEqual(article.description, "Test Description")
        self.assertEqual(article.publicationDate, "2024-01-01T12:00:00Z")

if __name__ == '__main__':
    unittest.main()