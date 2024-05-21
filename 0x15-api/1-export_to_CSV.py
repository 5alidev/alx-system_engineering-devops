#!/usr/bin/python3
"""
for a given employee ID, returns information about
his/her TODO list progress
"""

import csv
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

    with open("{}.csv".format(USER_ID), "w", newline="") as csvfile:
        for task in tasks:
            completed = task.get('completed')
            title = task.get('title')
            csvfile.write('"{}","{}","{}","{}"\n'
                          .format(USER_ID, USERNAME, completed, title))
