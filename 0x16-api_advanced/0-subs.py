#!/usr/bin/python3
"""Subreddit count"""
import requests
import json


def number_of_subscribers(subreddit):
    """ Return sub count"""
    url = 'https://www.reddit.com/r/{}/about/.json'.format(subreddit)
    head = {'User-agent': 'URL'}
    req = requests.get(url, headers=head, allow_redirects=False).json()
    try:
        return (req.get('data').get('subscribers'))
    except:
        return 0
