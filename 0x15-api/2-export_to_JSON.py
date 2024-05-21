#!/usr/bin/python3
"""
for a given employee ID, returns information about
his/her TODO list progress
"""

import csv
import json
import requests
import sys


if __name__ == "__main__":
    USER_ID = sys.argv[1]
    url = 'https://jsonplaceholder.typicode.com/users/' + USER_ID
    userRes = requests.get(url)

    USERNAME = userRes.json().get("username")
    todosUrl = url + '/todos'
    todoRes = requests.get(todosUrl)
    tasks = todoRes.json()

    data_obj = {USER_ID: []}
    for task in tasks:
        TASK_COMPLETED_STATUS = task.get('completed')
        TASK_TITLE = task.get('title')
        data_obj[USER_ID].append({
                                 "task": TASK_TITLE,
                                 "completed": TASK_COMPLETED_STATUS,
                                 "username": USERNAME})

    """print json data"""
    with open('{}.json'.format(USER_ID), 'w') as f:
        json.dump(data_obj, f)
