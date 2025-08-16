class Article:
    all = []  # Class variable to keep track of all articles

    def __init__(self, author, magazine, title):
        # Import here to avoid circular imports
        from lib.author import Author
        from lib.magazine import Magazine
        
        if not isinstance(author, Author):
            raise Exception("Author must be an Author instance")
        if not isinstance(magazine, Magazine):
            raise Exception("Magazine must be a Magazine instance")
        if not isinstance(title, str) or not (5 <= len(title) <= 50):
            raise Exception("Title must be a string between 5 and 50 characters")
        
        self._author = author
        self._magazine = magazine
        self._title = title
        Article.all.append(self)

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, value):
        if hasattr(self, '_title'):
            raise Exception("Title cannot be changed after instantiation")
        self._title = value

    @property
    def author(self):
        return self._author

    @author.setter
    def author(self, value):
        # Import here to avoid circular imports
        from lib.author import Author
        if not isinstance(value, Author):
            raise Exception("Author must be an Author instance")
        self._author = value

    @property
    def magazine(self):
        return self._magazine

    @magazine.setter
    def magazine(self, value):
        # Import here to avoid circular imports
        from lib.magazine import Magazine
        if not isinstance(value, Magazine):
            raise Exception("Magazine must be a Magazine instance")
        self._magazine = value