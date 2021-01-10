import requests

from twitter.models import TwitterUser, ContextAnnotation, Tweet, Entities


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
        'tweet.fields': 'public_metrics,geo,context_annotations,entities',
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
    handle_response(response_json)
    iteration = 0
    while response_json['meta']['next_token'] is not None and iteration < 5:
        print(response_json['meta'])
        # iteration += 1
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
        handle_response(response_json)


def handle_response(response_json):
    for twitter_user in response_json['includes']['users']:
        twitter_user = TwitterUser(int(twitter_user['id'][0:49]),
                                   twitter_user['location'][0:49] if 'location' in twitter_user else None,
                                   twitter_user['name'][0:49],
                                   twitter_user['username'][0:49])
        twitter_user.save()
    for tweet in response_json['data']:
        tweet_row = Tweet(
            id=int(tweet['id']),
            author_id=TwitterUser.objects.get(id=tweet['author_id']),
            like_count=int(tweet['public_metrics']['like_count']),
            quote_count=int(tweet['public_metrics']['quote_count']),
            reply_count=int(tweet['public_metrics']['reply_count']),
            retweet_count=int(tweet['public_metrics']['retweet_count']),
            text=tweet['text'][0:399]
        )
        tweet_row.save()
        if 'context_annotations' in tweet:
            for context_annotations in tweet['context_annotations']:
                context_annotation = ContextAnnotation(
                    tweet_id=Tweet.objects.get(id=tweet['id']),
                    domain_id=int(context_annotations['domain']['id']),
                    domain_name=context_annotations['domain']['name'][0:49],
                    domain_description=context_annotations['domain']['description'][0:49] if 'description' in context_annotations[
                        'domain'] else None,
                    entity_id=int(context_annotations['entity']['id']),
                    entity_name=context_annotations['entity']['name'][0:49],
                    entity_description=context_annotations['entity']['description'][0:49] if 'context_annotations' in context_annotations[
                        'entity'] else None
                )
                context_annotation.save()
        if 'entities' in tweet:
            if 'annotations' in tweet['entities']:
                for annotations in tweet['entities']['annotations']:
                    entity = Entities(
                        tweet_id=Tweet.objects.get(id=tweet['id']),
                        start_char=int(annotations['start']),
                        end_char=int(annotations['end']),
                        probability=float(annotations['probability']),
                        type=annotations['type'],
                        normalized_text=annotations['normalized_text'][0:49]
                    )
                    entity.save()


def make_twitter_call():
    base_url = get_base_url()
    bearer_token = auth()
    headers = create_headers(bearer_token)
    params = create_params()
    get_stream(base_url, headers, params)
