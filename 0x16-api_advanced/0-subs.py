#!/usr/bin/python3
"""
Reddit API: subreddit - subscribers number
"""

import requests


def number_of_subscribers(subreddit):
    """
    returns the number of subscribers for a given subreddit.
    """

    url = 'https://www.reddit.com/r/{}/about.json'.format(subreddit)
    response = requests.get(url)
    if response.status_code == 200:
        subsribers = response.json()["data"]["subscribers"]
        return subsribers
    return 0
