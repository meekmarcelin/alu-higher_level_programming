#!/usr/bin/python3
""" Send a request to URL """
import urllib.request
import sys


if __name__ == "__main__":
    with urllib.request.urlopen(sys.arg[1]) as response:
        print(response.info()['X-Request_Id'])
