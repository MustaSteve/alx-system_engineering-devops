#!/usr/bin/python3
'''function that queries the Reddit API and returns the number of subscribers
'''
import requests


def number_of_subscribers(subreddit):
    '''Returns the number of subscribers'''
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    res = requests.get(url)
    if res.status_code == 200:
        return res.json()['data']['subscribers']
    else:
        return 0
