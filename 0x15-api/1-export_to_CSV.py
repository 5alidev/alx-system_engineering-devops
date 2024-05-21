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
    usr_id = sys.argv[1]
    usr = requests.get(url + "users/{}".format(usr_id)).json()
    usr_name = usr.get("username")

    params = {"userId": usr_id}
    todos = requests.get(url + "todos", params).json()

    with open("{}.csv".format(usr_id), "w", newline="") as csvfile:
        writer = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
        [writer.writerow(
            [usr_id, usr_name, t.get("completed"), t.get("title")]
        ) for t in todos]
