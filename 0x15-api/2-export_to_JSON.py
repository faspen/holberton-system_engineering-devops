#!/usr/bin/python3
""" Export to json """
import json
import requests
from sys import argv


def to_json(user_id):
    """ Convert to json """
    url = "https://jsonplaceholder.typicode.com"
    user_url = "{}/users/{}".format(url, user_id)
    username = requests.get(user_url).json().get('name')
    tasks = requests.get('{}/todos?userId={}'.format(url, user_id)).json()

    d = {}
    dlist = []
    for task in tasks:
        tdict = {}
        tdict['task'] = task.get('title')
        tdict['completed'] = task.get('completed')
        tdict['username'] = username
        dlist.append(tdict)

    with open('{}.json'.format(user_id), 'w') as f:
        d[user_id] = dlist
        json.dump(d, f)

if __name__ == "__main__":
    to_json(argv[1])
