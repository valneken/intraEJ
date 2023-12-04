import feedparser
import json
import requests
from datetime import datetime

RSS_FEED_URL = 'https://www.eurojust.europa.eu/rss/press-releases.xml'
JSON_FILE_PATH = 'rss_data.json'

def fetch_and_save_feed():
    feed = feedparser.parse(RSS_FEED_URL)
    entries = feed.entries

    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    data_with_timestamp = {
        'timestamp': timestamp,
        'entries': entries
    }

    with open(JSON_FILE_PATH, 'w') as json_file:
        json.dump(data_with_timestamp, json_file, indent=2)

if __name__ == '__main__':
    fetch_and_save_feed()
