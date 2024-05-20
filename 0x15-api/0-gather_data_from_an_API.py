#!/usr/bin/python3
"""
for a given employee ID, returns information about
his/her TODO list progress
"""
import requests
import sys

if __name__ == "__main__":
    url = 'https://jsonplaceholder.typicode.com/users/{}'.format(sys.argv[1])
    usrs = requests.get(url)
    usrsJson = usrs.json()
    name = usrsJson["name"]
    nbr_t_done = 0
    total_t = 0

    todosURL = 'https://jsonplaceholder.typicode.com/todos'
    todos = requests.get(todosURL)
    todosJson = todos.json()

    for t in todosJson:
        if t["userId"] == int(sys.argv[1]):
            total_t += 1
            if t["completed"]:
                nbr_t_done += 1

    print('Employee {} is done with tasks({}/{}):'
          .format(name, nbr_t_done, total_t))

    print('\n'.join("\t " + t["title"] for t in todosJson
          if t['userId'] == int(sys.argv[1]) and t['completed']))
