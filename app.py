import os
import requests
import json
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

search_url = "https://api.twitter.com/2/tweets/search/recent"

query_params = {'query': 'neon genesis evangelion', 'tweet.fields': 'text'}


def bearer_oauth(r):
    """
    Method required by bearer token authentication.
    """

    r.headers["Authorization"] = f"Bearer {os.getenv('TWITTER_BEARER')}"
    r.headers["User-Agent"] = "v2RecentSearchPython"
    return r

def connect_to_endpoint(url, params):
    response = requests.get(url, auth=bearer_oauth, params=params)
    print(response.status_code)
    if response.status_code != 200:
        raise Exception(response.status_code, response.text)
    return response.json()


def main():
    json_response = connect_to_endpoint(search_url, query_params)
    print(json.dumps(json_response, indent=4, sort_keys=True))


if __name__ == "__main__":
    main()