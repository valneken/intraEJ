import feedparser
import json
import requests

RSS_FEED_URL = 'https://www.eurojust.europa.eu/rss/press-releases.xml'
JSON_FILE_PATH = 'rss_data.json'

def fetch_and_save_feed():
    feed = feedparser.parse(RSS_FEED_URL)
    entries = feed.entries

    with open(JSON_FILE_PATH, 'w') as json_file:
        json.dump(entries, json_file, indent=2)

if __name__ == '__main__':
    fetch_and_save_feed()
