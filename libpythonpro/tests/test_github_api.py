from unittest.mock import Mock

import pytest

from libpythonpro import github_api


@pytest.fixture
def avatar_url(mocker):
    resp_mock = Mock()
    url = 'https://avatars2.githubusercontent.com/u/2669?v=4'
    resp_mock.json.return_value = {
        "login": "gabriel",
        "id": 12446314,
        "avatar_url": url,
    }
    get_mock = mocker.patch('libpythonpro.github_api.requests.get')
    get_mock.return_value = resp_mock
    return url


def test_get_avatar(avatar_url):
    url = github_api.get_avatar('gabriel')
    assert avatar_url == url


def test_get_avatar_integracao():
    url = github_api.get_avatar('alvesgabriel')
    assert 'https://avatars3.githubusercontent.com/u/12446314?v=4' == url
