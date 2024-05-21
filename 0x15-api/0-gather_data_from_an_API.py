#!/usr/bin/python3
"""
for a given employee ID, returns information about
his/her TODO list progress
"""

import requests
import sys


if __name__ == "__main__":
    employee_ID = sys.argv[1]
    url = "https://jsonplaceholder.typicode.com/users/{}".format(employee_ID)

    empRes = requests.get(url)
    EMPLOYEE_NAME = empRes.json().get('name')

    todosUrl = url + "/todos"
    todoRes = requests.get(todosUrl)
    todos = todoRes.json()
    nb_done = 0
    tasks_arr = []

    for t in todos:
        if t.get('completed'):
            tasks_arr.append(t)
            nb_done += 1

    print("Employee {} is done with tasks({}/{}):"
          .format(EMPLOYEE_NAME, nb_done, len(tasks_arr)))

    for t in tasks_arr:
        print("\t {}".format(t.get('title')))
