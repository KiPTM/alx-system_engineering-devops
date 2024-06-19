#!/usr/bin/python3
"""Function to query subscribers on a given Reddit subreddit."""
import requests

def number_of_subscribers(subreddit):
    """Return the total number of subscribers on a given subreddit."""
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {
        "User-Agent": "MathewTuweiBot/1.0 (by /u/MathewTuwei)"
    }
    response = requests.get(url, headers=headers, allow_redirects=False)
    
    if response.status_code == 200:
        return 0
    
    data = response.json().get("data")
    if data is None:
        return 0
    
    return data.get("subscribers", 0)

if __name__ == "__main__":
    existing_subreddit = "learnpython"
    nonexisting_subreddit = "nonexistingsubredditname12345"
    
    existing_subscribers = number_of_subscribers(existing_subreddit)
    nonexisting_subscribers = number_of_subscribers(nonexisting_subreddit)
    
    if existing_subscribers != 0:
        print("OK")
    else:
        print("FAIL")
    
    if nonexisting_subscribers == 0:
        print("OK")
    else:
        print("FAIL")
