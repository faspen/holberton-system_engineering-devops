#!/usr/bin/python3
"""Reddit"""
import requests
import json


def recurse(subreddit, hot_list=[], after=''):
    """Return number of hot posts"""

    url = 'https://www.reddit.com/r/{}/hot/.json?after={}'.format(
        subreddit, after)
    head = {'User-agent': 'url'}
    req = requests.get(url, headers=head, allow_redirects=False).json()
    try:
        tmp = req.get('data').get('children')
        for i in tmp:
            hot_list.append(i.get('data').get('title'))
    except:
        return(None)
    aft = req.get('data').get('after')
    if aft is None:
        return hot_list
    return recurse(subreddit, hot_list, aft)
