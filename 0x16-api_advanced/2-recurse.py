#!/usr/bin/python3
"""
Reddit API - Hot Articles Recursion
"""
import requests


def recurse(subreddit, hot_list=[], after=""):
    """
    recursive function that returns a list containing the titles
    of all hot articles for a given subreddit
    """
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    response = requests.get(url)
    if response.status_code == 200:
        children = response.json()["data"]["children"]
        after_link = response.json()["data"].get("after")
        for child in children:
            hot_list.append(child["data"]["title"])
        if after_link:
            recurse(subreddit, hot_list, after_link)
        else:
            return hot_list
    else:
        return None
