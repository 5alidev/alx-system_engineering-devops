#!/usr/bin/python3
"""
for a given employee ID, returns information about
his/her TODO list progress
"""
import requests
import sys

if __name__ == "__main__":
    url = 'https://jsonplaceholder.typicode.com/users/'
    usrs = requests.get(url)
    usrsJson = usrs.json()

    for u in usrsJson:
        if u.get("id") == int(sys.argv[1]):
            name = u.get('name')
    nbr_t_done = 0
    total_t = 0

    todosURL = 'https://jsonplaceholder.typicode.com/todos'
    todos = requests.get(todosURL)
    todosJson = todos.json()
    tasks = []

    for t in todosJson:
        if t["userId"] == int(sys.argv[1]):
            total_t += 1
            if t.get("completed"):
                nbr_t_done += 1
                tasks.append(t.get('title'))

    print('Employee {} is done with tasks({}/{}):'
          .format(name, nbr_t_done, total_t))

    for task in tasks:
        print("\t {}".format(task))
