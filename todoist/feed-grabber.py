#!/usr/bin/python
import os
import feedparser
from todoist.api import TodoistAPI

def get_token():
    token = ''
    home = os.getenv('HOME')
    with open(home +'/Dropbox/important/todoist-api-token') as f:
        token = f.read()

    return token

# Adds the top item of feed located at url to Todoist
def parse(urls):
    token = get_token()
    api = TodoistAPI(token)

    for url in urls:
        feed = feedparser.parse(url)
        item = feed['entries'][0]
        title = item['title']
        link = item['links'][0]['href']
        api.items.add('[' + title + '](' + link + ')', 2171697157, labels=[2149155667], date_string="today")
        # Use api.state['project'] or ['labels'] to get project or label ids

    api.commit()


if __name__ == '__main__':
    parse(['https://www.theatlantic.com/feed/best-of/',
           'https://hnrss.org/newest?points=300',
           'http://rss.nytimes.com/services/xml/rss/nyt/MostViewed.xml'])
