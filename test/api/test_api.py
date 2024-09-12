import allure

from api_client.api_client import ApiClient


@allure.epic('EM test project')
@allure.suite('API tests')
@allure.title('Получение репозиториев пользователя')
def test_getting_repositories(logger):
    api_client = ApiClient('https://api.github.com', logger)
    api_client.get_user_repositories()
    api_client.assert_getting_repositories()


@allure.epic('EM test project')
@allure.suite('API tests')
@allure.title('Создание нового публичного репозитория')
def test_create_repository(delete_test_repository, logger):
    api_client = ApiClient('https://api.github.com', logger)
    api_client.create_repository(name='my737373')
    api_client.assert_create_repository()


@allure.epic('EM test project')
@allure.suite('API tests')
@allure.title('Удаление репозитория пользователя')
def test_delete_repository(create_test_repository, logger):
    api_client = ApiClient('https://api.github.com', logger)
    api_client.delete_repository(name='my737373')
    api_client.assert_delete_repository()
