import pytest
from classes.many_to_many import Author, Magazine, Article


class TestArticle:
    """Article in many_to_many.py"""

    def test_has_title(self):
        author = Author("John Doe")
        magazine = Magazine("Tech Today", "Technology")
        article = Article(author, magazine, "The Future of AI")

        assert article.title == "The Future of AI"

    def test_title_is_immutable(self):
        author = Author("Jane Doe")
        magazine = Magazine("Health Weekly", "Health")
        article = Article(author, magazine, "Wellness Trends")

        with pytest.raises(AttributeError):
            article.title = "New Title"

    def test_belongs_to_author(self):
        author = Author("Alice")
        magazine = Magazine("Fashion Daily", "Fashion")
        article = Article(author, magazine, "Fall Collection")

        assert article.author == author

    def test_belongs_to_magazine(self):
        author = Author("Bob")
        magazine = Magazine("Sports Illustrated", "Sports")
        article = Article(author, magazine, "Championship Highlights")

        assert article.magazine == magazine

    def test_title_must_be_string(self):
        author = Author("Sam")
        magazine = Magazine("Cooking Monthly", "Cooking")

        with pytest.raises(ValueError):
            Article(author, magazine, 12345)

    def test_title_length_constraints(self):
        author = Author("Max")
        magazine = Magazine("Travel Guide", "Travel")

        # too short
        with pytest.raises(ValueError):
            Article(author, magazine, "Go")

        # too long
        with pytest.raises(ValueError):
            Article(author, magazine, "A" * 51)

        # valid
        article = Article(author, magazine, "Exploring the Alps")
        assert article.title == "Exploring the Alps"
