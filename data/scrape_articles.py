# data/scrape_articles.py
import requests
from newspaper import Article
import time
from data.article_urls import article_urls

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.82 Safari/537.36'
}

session = requests.Session()
pages_content = []

for url in article_urls:
    try:
        time.sleep(2)
        response = session.get(url, headers=headers, timeout=10)

        if response.status_code == 200:
            article = Article(url)
            article.download()
            article.parse()
            pages_content.append({"url": url, "text": article.text})
        else:
            print(f"Failed to fetch article at {url}")
    except Exception as e:
        print(f"Error occurred while fetching article at {url}: {e}")
