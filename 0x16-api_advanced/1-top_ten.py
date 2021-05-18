#!/usr/bin/python3
"""Reddit"""
import json
import requests


def top_ten(subreddit):
    """Return top ten trending posts"""
    url = 'https://www.reddit.com/r/{}/hot/.json?limit=10'.format(subreddit)
    head = {'User-agent': 'url'}
    req = requests.get(url, headers=head, allow_redirects=False).json()
    try:
        hot = req.get('data').get('children')
        for i in hot:
            print(i.get('data').get('title'))
    except:
        print(None)
