from github3 import GitHub


def get_followers(username):
    api_client = GitHub()
    return api_client.user(username).followers
