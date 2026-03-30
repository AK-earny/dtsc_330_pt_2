import sqlite3
from entity_resolution_pipeline.readers.articles import Articles
from entity_resolution_pipeline.readers.grants import Grants

def minimal_create_database():
    """The bare minimum to create a new sqlite database."""
    connection = sqlite3.connect("data/article_grant_db.sqlite")
    print(connection.execute("SELECT sqlite_version();").fetchall())

if __name__ == "__main__":
    minimal_create_database()
    articles = Articles("C:/Users/alexk/Downloads/pubmed26n1384.xml.gz")
    articles.to_db()

    grants = Grants("C:/Users/alexk/Downloads/RePORTER_PRJ_C_FY2025.zip")
    grants.to_db()