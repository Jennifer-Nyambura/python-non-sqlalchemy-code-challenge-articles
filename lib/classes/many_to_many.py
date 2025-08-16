# many_to_many.py

class Author:
    def __init__(self, name):
        if not isinstance(name, str):
            raise TypeError("Author name must be a string")
        if len(name.strip()) == 0:
            raise ValueError("Author name must be longer than 0 characters")
        self._name = name
        self._articles = []

    @property
    def name(self):
        return self._name

    def articles(self):
        """Return all articles written by this author"""
        return self._articles

    def magazines(self):
        """Return unique magazines this author has written for"""
        return list({article.magazine for article in self._articles})


class Magazine:
    def __init__(self, name, category):
        if not isinstance(name, str):
            raise TypeError("Magazine name must be a string")
        if len(name) < 2 or len(name) > 30:
            raise ValueError("Magazine name must be between 2 and 30 characters")
        if not isinstance(category, str):
            raise TypeError("Magazine category must be a string")
        if len(category) == 0:
            raise ValueError("Magazine category must not be empty")

        self._name = name
        self._category = category
        self._articles = []

    @property
    def name(self):
        return self._name

    @property
    def category(self):
        return self._category

    def articles(self):
        """Return all articles in this magazine"""
        return self._articles

    def contributors(self):
        """Return unique authors who wrote for this magazine"""
        return list({article.author for article in self._articles})


class Article:
    def __init__(self, author, magazine, title):
        if not isinstance(title, str):
            raise ValueError("Title must be a string")   # <-- FIXED HERE
        if len(title) < 5 or len(title) > 50:
            raise ValueError("Title must be between 5 and 50 characters")
        if not isinstance(author, Author):
            raise TypeError("Author must be an Author instance")
        if not isinstance(magazine, Magazine):
            raise TypeError("Magazine must be a Magazine instance")

        self._title = title
        self.author = author
        self.magazine = magazine

        # link relationships
        author._articles.append(self)
        magazine._articles.append(self)

    @property
    def title(self):
        return self._title
