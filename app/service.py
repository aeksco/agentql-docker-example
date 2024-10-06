from pymongo import MongoClient
import os
from bson import ObjectId

def get_mongodb_client():
    mongodb_uri = os.environ.get('MONGODB_URI', 'mongodb://localhost:27017/myapp')
    return MongoClient(mongodb_uri)

def get_articles():
    client = MongoClient(os.environ['MONGODB_URI'])
    db = client.myapp
    articles = db.articles.find()
    return list(articles)

def process_articles():
    articles = get_articles()
    for article in articles:
        # Process each article
        print(f"Processing article: {article['title']}")
        # Add your processing logic here
        # For example:
        # - Update article content
        # - Perform sentiment analysis
        # - Extract keywords
        # - etc.

    print(f"Processed {len(articles)} articles")

# # # # # 

process_articles()

