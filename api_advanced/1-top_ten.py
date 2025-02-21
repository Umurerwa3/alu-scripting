#!/usr/bin/python3
"""
Module to query Reddit API and print titles of first 10 hot posts
for a given subreddit
"""
import requests


def top_ten(subreddit):
    """
    Queries the Reddit API and prints the titles of the first 10 hot posts
    for a given subreddit.
    
    Args:
        subreddit (str): The name of the subreddit to query
        
    Returns:
        None: Prints the titles or None if subreddit is invalid
    """
    # Reddit API URL for hot posts in a subreddit
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    
    # Custom User-Agent to avoid too many requests error
    headers = {
        "User-Agent": "linux:0.1:alu-scripting (by /u/aluscripting)"
    }
    
    # Set a parameter to limit to the first 10 posts
    params = {
        "limit": 10
    }
    
    # Make request with allow_redirects=False to avoid following redirects
    response = requests.get(
        url,
        headers=headers,
        params=params,
        allow_redirects=False
    )
    
    # Check if the response status code indicates success
    if response.status_code == 200:
        # Parse the JSON response
        data = response.json()
        
        # Extract and print the titles of the first 10 hot posts
        posts = data.get("data", {}).get("children", [])
        for post in posts:
            print(post.get("data", {}).get("title"))
    else:
        # If not a valid subreddit, print None
        print(None)
