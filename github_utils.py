import github3


def get_followers(username):
    api_client = github3.GitHub()
    return api_client.user(username).followers
