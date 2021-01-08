import json

import requests


def auth():
    return "AAAAAAAAAAAAAAAAAAAAAI20LAEAAAAApJpQAPAVWZcLlh5FoaV5vpseZ" \
           "%2F4%3Du3f9LYyWBxQJMNXDecJtsSlL8qSCPwbF9YyvTZHMfDtM2hQoUB"


def create_headers(bearer_token):
    headers = {"Authorization": "Bearer {}".format(bearer_token)}
    return headers


def get_rules(headers, bearer_token):
    response = requests.get(
        "https://api.twitter.com/2/tweets/search/stream/rules", headers=headers
    )
    if response.status_code != 200:
        raise Exception(
            "Cannot get rules (HTTP {}): {}".format(response.status_code, response.text)
        )
    print(json.dumps(response.json()))
    return response.json()


def create_query():
    query = "query=COVID&expansions=author_id,geo.place_id"
    return query


def create_fields():
    field = "user.fields=location&tweet.fields=text,geo,public_metrics,referenced_tweets"
    return field


def get_stream(headers, query, fields):
    response = requests.get(
        "https://api.twitter.com/2/tweets/search/recent?" + query + "&" + fields, headers=headers, stream=True,
    )
    print(response.status_code)
    if response.status_code != 200:
        raise Exception(
            "Cannot get stream (HTTP {}): {}".format(
                response.status_code, response.text
            )
        )
    for response_line in response.iter_lines():
        if response_line:
            json_response = json.loads(response_line)
            print(json.dumps(json_response, indent=4, sort_keys=True))


def main():
    bearer_token = auth()
    headers = create_headers(bearer_token)
    query = create_query()
    fields = create_fields()
    get_stream(headers, query, fields)