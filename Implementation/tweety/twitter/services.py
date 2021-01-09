import json

import requests


def auth():
    return "AAAAAAAAAAAAAAAAAAAAAI20LAEAAAAApJpQAPAVWZcLlh5FoaV5vpseZ" \
           "%2F4%3Du3f9LYyWBxQJMNXDecJtsSlL8qSCPwbF9YyvTZHMfDtM2hQoUB"


def get_base_url():
    return "https://api.twitter.com/2/tweets/search/recent"


def create_headers(bearer_token):
    headers = {
        "content-type": "application/json",
        "Authorization": "Bearer {}".format(bearer_token)
    }
    return headers


def create_params():
    params = {
        'max_results': 100,
        'query': 'corona pandemic is:retweet lang:en has:mentions',
        'expansions': 'referenced_tweets.id,referenced_tweets.id.author_id',
        'tweet.fields': 'public_metrics,geo',
        'user.fields': 'location'
    }
    return params


def get_stream(base_url, headers, params):
    response = requests.get(base_url, headers=headers, params=params)
    if response.status_code != 200:
        raise Exception(
            "Cannot get stream (HTTP {}): {}".format(
                response.status_code, response.text
            )
        )
    response_json = response.json()
    print(response_json)
    while response_json['meta']['next_token'] is not None:
        params['next_token'] = response_json['meta']['next_token']
        response = requests.get(
            base_url, headers=headers, params=params
        )
        if response.status_code != 200:
            raise Exception(
                "Cannot get stream (HTTP {}): {}".format(
                    response.status_code, response.text
                )
            )
        response_json = response.json()
        print(response_json)


def handle_response(response):
    for response_line in response.iter_lines():
        if response_line:
            json_response = json.loads(response_line)
            print(json.dumps(json_response, indent=4, sort_keys=True))


def main():
    base_url = get_base_url()
    bearer_token = auth()
    headers = create_headers(bearer_token)
    params = create_params()
    get_stream(base_url, headers, params)
