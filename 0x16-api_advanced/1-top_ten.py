#!/usr/bin/python3
'''prints the titles of the first 10 hot posts listed for a given subreddit.
'''
import requests


def top_ten(subreddit):
    '''prints the titles of the first 10 hot posts'''
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    res = requests.get(url)
    if res.status_code == 200:
        data = res.json()['data']
        for post in data:
            print(post['title'])
    else:
        print("None")
