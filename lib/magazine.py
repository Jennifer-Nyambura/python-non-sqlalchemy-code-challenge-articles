class Magazine:
    all = []  # Class variable to keep track of all magazines

    def __init__(self, name, category):
        if not isinstance(name, str) or not (2 <= len(name) <= 16):
            raise Exception("Name must be a string between 2 and 16 characters")
        if not isinstance(category, str) or len(category) == 0:
            raise Exception("Category must be a non-empty string")
        
        self._name = name
        self._category = category
        Magazine.all.append(self)

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not isinstance(value, str) or not (2 <= len(value) <= 16):
            raise Exception("Name must be a string between 2 and 16 characters")
        self._name = value

    @property
    def category(self):
        return self._category

    @category.setter
    def category(self, value):
        if not isinstance(value, str) or len(value) == 0:
            raise Exception("Category must be a non-empty string")
        self._category = value

    def articles(self):
        # Import here to avoid circular imports
        from lib.article import Article
        return [article for article in Article.all if article.magazine == self]

    def contributors(self):
        author_list = []
        for article in self.articles():
            if article.author not in author_list:
                author_list.append(article.author)
        return author_list

    def article_titles(self):
        articles_list = self.articles()
        if not articles_list:
            return None
        return [article.title for article in articles_list]

    def contributing_authors(self):
        articles_list = self.articles()
        if not articles_list:
            return None
        
        author_count = {}
        for article in articles_list:
            if article.author in author_count:
                author_count[article.author] += 1
            else:
                author_count[article.author] = 1
        
        contributing_authors_list = [author for author, count in author_count.items() if count > 2]
        return contributing_authors_list if contributing_authors_list else None

    @classmethod
    def top_publisher(cls):
        # Import here to avoid circular imports
        from lib.article import Article
        if not Article.all:
            return None
        
        magazine_count = {}
        for article in Article.all:
            if article.magazine in magazine_count:
                magazine_count[article.magazine] += 1
            else:
                magazine_count[article.magazine] = 1
        
        if not magazine_count:
            return None
        
        top_magazine = max(magazine_count.items(), key=lambda x: x[1])
        return top_magazine[0]