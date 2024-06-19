#!/usr/bin/python3
"""Function to query subscribers on a given Reddit subreddit."""
import requests

def number_of_subscribers(subreddit):
    """Return the total number of subscribers on a given subreddit."""
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {
        "User-Agent": "linux:0x16.api.advanced:v1.0.0 (by /u/bdov)"
    }
    response = requests.get(url, headers=headers, allow_redirects=False)
    if response.status_code == 404:
        return None
    results = response.json().get("data")
    return results.get("subscribers", 0)

if __name__ == "__main__":
    existing_subreddit = "learnpython"
    nonexisting_subreddit = "nonexistingsubredditname12345"
    
    existing_subscribers = number_of_subscribers(existing_subreddit)
    nonexisting_subscribers = number_of_subscribers(nonexisting_subreddit)
    
    if existing_subscribers is not None:
        print("OK")
    else:
        print("FAIL")

    if nonexisting_subscribers is None:
        print("OK")
    else:
        print("FAIL")

