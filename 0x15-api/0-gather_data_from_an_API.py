#!/usr/bin/python3
""" 0-gather_data_from_an_API """
import requests
from sys import argv


def todo_list(user_id):
    """Return todo list info """
    url = "https://jsonplaceholder.typicode.com/todos/1"
    user_url = "{}/users/{}".format(url, user_id)
    username = requests.get(user_url).json().get('name')
    tasks = requests.get('{}/todos?userId={}'.format(url, user_id)).json()
    tmp = '{}/todos?userId={}&completed=true'.format(url, user_id)
    done = requests.get(tmp).json()

    api_tasks = len(tasks)
    api_done = len(done)

    print(
        "Employee {} is done with tasks({}/{}):".format(
            username,
            api_done,
            api_tasks))

    for task in done:
        task_name = task.get('title')
        print("\t " + task_name)

if __name__ == "__main__":
    todo_list(argv[1])
