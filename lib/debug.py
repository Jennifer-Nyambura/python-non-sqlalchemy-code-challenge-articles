# debug.py

from lib.classes.many_to_many import Author, Magazine, Article

if __name__ == "__main__":
    # Create Authors
    author1 = Author("John Doe")
    author2 = Author("Jane Smith")

    # Create Magazines
    magazine1 = Magazine("TechMag", "Technology")
    magazine2 = Magazine("HealthLife", "Health")

    # Add Articles
    article1 = author1.add_article(magazine1, "The Future of AI")
    article2 = author1.add_article(magazine1, "Cybersecurity in 2025")
    article3 = author2.add_article(magazine2, "Healthy Living Tips")
    article4 = author1.add_article(magazine2, "Nutrition and Wellness")
    article5 = author2.add_article(magazine2, "Mental Health Matters")

    # Debugging Prints
    print("=== Authors ===")
    print(author1.name)
    print(author2.name)

    print("\n=== Magazines ===")
    print(magazine1.name, "-", magazine1.category)
    print(magazine2.name, "-", magazine2.category)

    print("\n=== Articles by John Doe ===")
    for article in author1.articles():
        print(article.title, "in", article.magazine.name)

    print("\n=== Articles by Jane Smith ===")
    for article in author2.articles():
        print(article.title, "in", article.magazine.name)

    print("\n=== Magazines John Doe Contributes To ===")
    for mag in author1.magazines():
        print(mag.name)

    print("\n=== TechMag Contributors ===")
    for contributor in magazine1.contributors():
        print(contributor.name)

    print("\n=== HealthLife Contributors ===")
    for contributor in magazine2.contributors():
        print(contributor.name)

    print("\n=== TechMag Article Titles ===")
    print(magazine1.article_titles())

    print("\n=== HealthLife Contributing Authors (more than 2 articles) ===")
    contributing_authors = magazine2.contributing_authors()
    if contributing_authors:
        for author in contributing_authors:
            print(author.name)
    else:
        print("No contributing authors with more than 2 articles.")

    print("\n=== John Doe Topic Areas ===")
    print(author1.topic_areas())

    print("\n=== Jane Smith Topic Areas ===")
    print(author2.topic_areas())
