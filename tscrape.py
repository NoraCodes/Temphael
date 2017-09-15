#!/usr/bin/env python3
"""
Build PyMarkovChain databases from Tumblr blogs
"""
import urllib

import argparse
import requests
from bs4 import BeautifulSoup
from pymarkovchain import MarkovChain

PARSER = argparse.ArgumentParser(
    description="Build a Markov Chain bot from a Tumblr blog (or single tag on a blog).")
PARSER.add_argument('url', metavar="URL", type=str,
                    help='The Tumblr subdomain to scrape. For staff.tumblr.com, URL would be staff')
PARSER.add_argument('--tag',
                    help="The tag to scrape on the given blog. Don't include the hash symbol '#'.")
PARSER.add_argument('start_page', type=int, metavar='START_PAGE',
                    help="The page from which to start scraping content.")
PARSER.add_argument('end_page', type=int, metavar='END_PAGE',
                    help="The final page to scrape content from.")
PARSER.add_argument("--debug", action="store_true")
PARSER.add_argument("--notags", action="store_true", help="Don't scrape tags, only content.")
PARSER.add_argument("--hash", action="store_true", help="Add # symbol to text from tags.")

ARGS = PARSER.parse_args()

if ARGS.tag is None:
    TARGET_URL = "https://{}.tumblr.com/page/".format(ARGS.url)
    TARGET_FILE = "{}.posts.markov".format(ARGS.url)
else:
    TARGET_URL = "https://{}.tumblr.com/tagged/{}/page/".format(ARGS.url,
                                                                urllib.parse.quote(ARGS.tag))
    TARGET_FILE = "{}.{}.markov".format(ARGS.url, urllib.parse.quote(ARGS.tag))


CORPUS = ""

for page_number in range(ARGS.start_page, ARGS.end_page + 1):
    print("Scraping page {}".format(page_number))
    soup = BeautifulSoup(requests.get(TARGET_URL + str(page_number)).text, 'lxml')

    # Search <p> tags for post content
    for para in soup.find_all('p'):
        t = para.get_text()
        if t is None:
            continue
        if "Originally posted by" in t:
            continue
        if "replied to your post" in t:
            continue
        CORPUS += t + "\n"

    if ARGS.notags:
        continue

    # Search <a> tags for post tags
    for tag in soup.find_all('a'):
        h = tag.get('href')
        if h is None:
            continue

        # Only extract tagged URLs
        if "/tagged" not in h:
            continue

        # If there's no text, skip
        try:
            t = tag.get_text()
        except Exception:
            continue
        if t is None:
            continue

        # Very commonly used tags
        if "//" in t:
            continue
        if "cw: " in t:
            continue

        # Tags which are just numbers should not be in the corpus
        try:
            int(t.strip())
            continue
        except ValueError:
            pass

        if ARGS.hash:
            CORPUS += "#" + t + " "
        else:
            CORPUS += t + " "
    CORPUS += "\n"


if ARGS.debug:
    print(CORPUS)
    exit(1)
print("Generating database...")
BOT = MarkovChain(TARGET_FILE)
BOT.generateDatabase(CORPUS)
print("Dumping database to {}".format(TARGET_FILE))
BOT.dumpdb()
