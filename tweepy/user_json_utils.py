# -*- coding:utf-8 -*-

import json
import tweepy

def get_user(method, **kwargs):
    user = method(raw_json={'parse': False}, **kwargs)
    return json.loads(user)


def get_users(method, **kwargs):
    """
    return mutliple users json objects
    parameters:
      - method: api.friends etc
      - kwargs: cursor=True if get previous_cursor and next_cursor

    >>> api = tweepy.api
    >>> users, cursors = users_cursor(api.friends, id=1234567)
    >>> (previous_cursor, next_cursor) = cursors

    Of cource you can omit id or screen_name etc.,
    if the api already authenticated.
    >>> auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
    >>> auth.set_access_token(USER_KEY, USER_SECRET)
    >>> api = tweepy.API(auth_handler=auth)
    >>> users, cursors = users_cursor(api.friends)

    users is list of json object
    each json object corresponds user.
    you can get id by
    >>> users[0]['id']

    If you want to get TweepyUserObject,
    >>> tweepy_user = parse_user(json.dumps(users[0]))
    >>> tweepy_user.id
    """
    if 'cursor' in kwargs:
        use_cursor = True
        cursor = kwargs['cursor']
        del kwargs['cursor']
        users = method(cursor=cursor, raw_json={'parse': False}, **kwargs)
    else:
        use_cursor = False
        users = method(raw_json={'parse': False}, **kwargs)
    loaded = json.loads(users)
    if use_cursor:
        next_cursor = loaded['next_cursor']
        previous_cursor = loaded['previous_cursor']
        next_cursor_str = loaded['next_cursor_str']
        previous_cursor_str = loaded['previous_cursor_str']
        del loaded['next_cursor']
        del loaded['previous_cursor']
        del loaded['next_cursor_str']
        del loaded['previous_cursor_str']

    if isinstance(loaded, list):
        users = loaded
    else:
        users = loaded['users']

    if use_cursor:
        return users, (previous_cursor, next_cursor)
    else:
        return users


def parse_user(json):
    result = tweepy.api.get_user(raw_json={'parse': True, 'data': json})
    return result
