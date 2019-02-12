import requests


def get_avatar(user):
    """
    Get the avatar of Github user
    :param user: str Github username
    :return: str avatar link
    """
    url = f'https://api.github.com/users/{user}'
    resp = requests.get(url)
    return resp.json()['avatar_url']


if __name__ == '__main__':
    print(get_avatar('alvesgabriel'))
