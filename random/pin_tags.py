#!/usr/bin/env python
"""
Adds the domain name as a tag for all pinboard bookmarks,
so I can organise by site
"""

import os
from urllib.parse import urlparse
import pinboard


def replace_stuff(url):
    stuff = ['www.', 'm.', 'blog.', 'help.', 'blogs.',
             'gist.', 'en.', '.co', 'www2.', '.wordpress']
    for item in stuff:
        url = url.replace(item, '')

    return url


def main(pb):
    all_bookmarks = pb.posts.all()
    for bookmark in all_bookmarks:
        url = bookmark.url
        tags = bookmark.tags
        parsed = urlparse(url).netloc
        parsed = parsed[:parsed.rfind('.')]
        if '1.1.1.1' in url:
            parsed = "cloudflare"

        parsed = replace_stuff(parsed)

        # This if doesn't need to be here, pinboard will filter
        if parsed not in tags:
            print("==============================")
            print("Bookmark: {}".format(bookmark))
            print("Tag to add: {}".format(parsed))
            print("Current tags: {}".format(tags))
            tags = [parsed] + tags
            if "utoronto" in parsed or "cs.toronto" in parsed:
                tags = ["utoronto"] + tags
            bookmark.tags = tags
            print("New tags: {}".format(bookmark.tags))
            bookmark.save()
            print("==============================")


if __name__ == '__main__':
    api_token = os.getenv("PINBOARD_API_TOKEN")
    pb = pinboard.Pinboard(api_token)
    main(pb)
