import requests


def get_followers(username):
    response = requests.get('https://api.github.com/users/%s' % username)
    return response.json()['followers']
