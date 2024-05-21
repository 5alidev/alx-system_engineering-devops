#!/usr/bin/python3
"""
for a given employee ID, returns information about
his/her TODO list progress
"""

import json
import requests
import sys


if __name__ == "__main__":
    usrsUrl = 'https://jsonplaceholder.typicode.com/users'
    userRes = requests.get(usrsUrl)
    users = userRes.json()

    usersObj = {}
    for usr in users:
        USER_ID = usr.get('id')
        USERNAME = usr.get('username')
        url = 'https://jsonplaceholder.typicode.com/users/{}'.format(USER_ID)
        todosUrl = url + '/todos/'
        todos = requests.get(todosUrl).json()

        usersObj[USER_ID] = []

        for task in todos:
            TASK_COMPLETED_STATUS = task.get('completed')
            TASK_TITLE = task.get('title')
            usersObj[USER_ID].append({
                "task": TASK_TITLE,
                "completed": TASK_COMPLETED_STATUS,
                "username": USERNAME})

    """print json data"""
    with open('todo_all_employees.json', 'w') as f:
        json.dump(usersObj, f)
