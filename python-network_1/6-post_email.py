#!/usr/bin/python3
""" Send a post request with an email """
import requests
import sys


if __name__ == "__main__":
    url = sys.argv[1]
    postreq = {'email': sys.argv[2]}
    r = request.post(url, data=postreq)
    print(r.text)
