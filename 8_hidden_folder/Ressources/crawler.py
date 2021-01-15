#!/usr/bin/env python3

import argparse
import requests
import re
import sys

# find whatever is in between quotes in href
# find all patterns (excluding '../' or 'README') that were preceded with href=" and until "
PATTERN = re.compile(r'(?!../|README)(?<=href=")[^"]*')
TEXT = set()


def main(URL):
    global TEXT
    readme = requests.get(URL + "README")
    TEXT.add(readme.text)
    if readme.text and " " not in readme.text:
        for entry in TEXT:
            print(entry)
        sys.exit()
    r = requests.get(URL)
    links = re.findall(PATTERN, r.text)
    for link in reversed(links):
        main(URL + link)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Crawl website and find the right README")
    parser.add_argument("URL", help="URL address of the server")
    args = parser.parse_args()
    main(args.URL + "/.hidden/")
