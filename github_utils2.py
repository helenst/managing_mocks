from requests import get


def get_followers(username):
    response = get('https://api.github.com/users/%s' % username)
    return response.json()['followers']
