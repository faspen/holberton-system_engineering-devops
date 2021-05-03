#!/usr/bin/python3
""" Export to csv """
import csv
import requests
from sys import argv


def csv_writer(user_id):
    """Write to csv format"""
    url = "https://jsonplaceholder.typicode.com"
    user_url = "{}/users/{}".format(url, user_id)
    username = requests.get(user_url).json().get('name')
    tasks = requests.get('{}/todos?userId={}'.format(url, user_id)).json()

    with open('{}.csv'.format(user_id), 'w') as f:
        writer = csv.writer(f, quoting=csv.QUOTE_ALL)
        for task in tasks:
            task_name = task.get('title')
            task_stat = task.get('completed')
            writer.writerow([user_id, username, task_stat, task_name])


if __name__ == "__main__":
    csv_writer(argv[1])
