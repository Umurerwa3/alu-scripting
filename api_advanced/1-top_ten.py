#!/usr/bin/python3
"""
This module queries the Reddit API to retrieve and display the titles of the first 10 hot posts for a given subreddit.
If the subreddit is invalid or has no posts, it prints "OK".
"""
import requests

def top_ten(subreddit):
    """Fetches and prints the titles of the first 10 hot posts for a given subreddit."""
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {'User-Agent': 'Mozilla/5.0'}
    params = {'limit': 10}
    
    response = requests.get(url, headers=headers, params=params, allow_redirects=False)
    
    if response.status_code == 200:
        data = response.json()
        posts = data.get('data', {}).get('children', [])
        if posts:
            for post in posts:
                print(post['data']['title'])
        else:
            print("OK")
    else:
        print("OK")

