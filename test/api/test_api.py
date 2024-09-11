from api_client.api_client import ApiClient


def test_getting_repositories():
    api_client = ApiClient('https://api.github.com')
    api_client.get_user_repositories()
    api_client.assert_getting_repositories()


def test_create_repository():
    api_client = ApiClient('https://api.github.com')
    api_client.create_repository(name='my737373')
    api_client.assert_create_repository()


def test_delete_repository():
    api_client = ApiClient('https://api.github.com')
    api_client.delete_repository(name='my737373')
    api_client.assert_delete_repository()
