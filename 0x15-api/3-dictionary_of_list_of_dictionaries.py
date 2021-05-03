#!/usr/bin/python3
""" Export to json """
import json
import requests
from sys import argv


def to_json():
    """ Convert to json """
    url = "https://jsonplaceholder.typicode.com"
    user = requests.get('{}/users'.format(url)).json()

    d = {}
    udict = {}
    for u in user:
        user_id = u.get('id')
        d[user_id] = []
        udict[user_id] = u.get('username')

    jobs = requests.get("{}/todos".format(url)).json()

    for task in jobs:
        tdict = {}
        user_id = task.get('userId')
        tdict['task'] = task.get('title')
        tdict['completed'] = task.get('completed')
        tdict['username'] = udict.get(user_id)
        d.get(user_id).append(tdict)

    with open('todo_all_employees.json', 'w') as f:
        json.dump(d, f)

if __name__ == "__main__":
    to_json()
