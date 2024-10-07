#!/usr/bin/env python3
import asyncio
import logging
import os
from typing import Dict, Any
import agentql
from pymongo import MongoClient
from flask import Flask, request, jsonify
from dotenv import load_dotenv
from agentql.ext.playwright.sync_api import Page
from playwright.sync_api import sync_playwright

# Load environment variables
load_dotenv()

# Configure logging
logging.basicConfig(level=logging.DEBUG)
log = logging.getLogger(__name__)

# Initialize Flask app
app = Flask(__name__)

# Initialize MongoDB connection
mongo_uri = os.getenv("MONGODB_URI", "mongodb://localhost:27017")
db_name = os.getenv("DB_NAME", "articles_db")
client = MongoClient(mongo_uri)
db = client[db_name]

# AgentQL queries
ARTICLE_QUERY = """
{
  article {
    author
    published_date(Format the output as an ISO 8601 date string)
    title
    image_url
    body
  }
}
"""

def main(url: str) -> Dict[str, Any]:
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=True)
        page = agentql.wrap(browser.new_page())
        page.goto(url)

        data = page.query_data(ARTICLE_QUERY)

        browser.close()
        return data

@app.route('/ingest', methods=['POST'])
def ingest():
    data = request.get_json()
    if not data or 'url' not in data:
        return jsonify({"error": "URL parameter is required in the JSON body"}), 400
    
    url = data['url']
    articles = db.articles
    result = articles.insert_one({'url': url, 'summary': None})
    
    return jsonify({"result": "Document inserted", "id": str(result.inserted_id)}), 201

@app.route('/process', methods=['GET'])
def process_latest():
    articles = db.articles
    article = articles.find_one({'summary': None})
    
    if not article:
        return jsonify({"message": "No unprocessed articles found"}), 404

    url = article.get('url')
    if not url:
        return jsonify({"message": "No URL found for the article"}), 404

    summary = main(url)
    
    # Update the article with the summary
    articles.update_one({'_id': article['_id']}, {'$set': {'summary': summary}})
    
    return jsonify({
        "message": "Article processed successfully",
        "article_id": str(article['_id']),
        "url": article['url'],
        "summary": summary
    }), 200
