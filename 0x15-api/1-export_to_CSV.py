#!/usr/bin/python3
"""
for a given employee ID, returns information about
his/her TODO list progress
"""
import csv
import requests
import sys

if __name__ == "__main__":
    url = 'https://jsonplaceholder.typicode.com/'
    USER_ID = sys.argv[1]
    user = requests.get(url + "users/{}".format(USER_ID)).json()
    USERNAME = user.get("username")

    params = {"userId": USER_ID}
    todos = requests.get(url + "todos", params).json()

    with open("{}.csv".format(USER_ID), "w", newline="") as csvfile:
        writer = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
        [writer.writerow(
            [USER_ID, USERNAME, t.get("completed"), t.get("title")]
        ) for t in todos]
