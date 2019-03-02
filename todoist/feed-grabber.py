#!/usr/local/bin/python3
"""
Grab one item each from The Atlantic, Hacker News,
and NYT, and save them to Todoist

Saves to a specific project ID, and marks the date for today.
API token is read from a specific folder
"""
import feedparser
import ssl
import todoist_utils as utils


def parse(urls):
    """ Adds the top item of feed located at url to Todoist """
    if hasattr(ssl, '_create_unverified_context'):
        ssl._create_default_https_context = ssl._create_unverified_context
    for url in urls:
        feed = feedparser.parse(url)
        item = feed['entries'][0]
        title = item['title']
        link = item['links'][0]['href']
        utils.add_to_project('To Browse',
                             '[' + title + '](' + link + ')',
                             label='break',
                             date='today')


if __name__ == '__main__':
    parse(['https://www.theatlantic.com/feed/best-of/',
           'https://hnrss.org/newest?points=300',
           'http://rss.nytimes.com/services/xml/rss/nyt/MostViewed.xml'])
