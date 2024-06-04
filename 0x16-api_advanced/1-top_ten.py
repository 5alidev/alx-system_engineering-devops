#!/usr/bin/python3
"""
Reddit API - Top 10 hot posts  Subreddit
"""
import requests


def top_ten(subreddit):
    """
    prints the titles of the first 10 hot posts listed for a given subreddit
    """

    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    response = requests.get(url)
    if response.status_code == 200:
        children = response.json()["data"]["children"]
        for child in children[:10]:
            print(child["data"]["title"])
    else:
        print("None")
