class Author:
    def __init__(self, name):
        if not isinstance(name, str) or len(name) == 0:
            raise Exception("Name must be a non-empty string")
        self._name = name

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if hasattr(self, '_name'):
            raise Exception("Name cannot be changed after instantiation")
        self._name = value

    def articles(self):
        # Import here to avoid circular imports
        from lib.article import Article
        return [article for article in Article.all if article.author == self]

    def magazines(self):
        magazine_list = []
        for article in self.articles():
            if article.magazine not in magazine_list:
                magazine_list.append(article.magazine)
        return magazine_list

    def add_article(self, magazine, title):
        # Import here to avoid circular imports
        from lib.article import Article
        return Article(self, magazine, title)

    def topic_areas(self):
        articles_list = self.articles()
        if not articles_list:
            return None
        
        categories = []
        for article in articles_list:
            if article.magazine.category not in categories:
                categories.append(article.magazine.category)
        return categories