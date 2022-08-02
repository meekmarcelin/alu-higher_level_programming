#!/usr/bin/python3
""" Send a request """
import requests
import sys



if __name == "__main__":
    url = sys.argv[1]
    r = requests.get(url)
    print(r.headers.get('x-request-id'))
