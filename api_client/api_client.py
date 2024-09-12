import requests
import os
import json


class ApiClient:
    def __init__(self, base_url, logger):
        self.base_url = base_url
        self.repositories = []
        self.logger = logger

    def get_user_repositories(self):
        url = self.base_url + '/user/repos'
        headers = {
            "Authorization": f"token {os.getenv('GIT_TOKEN')}",
            "Content-Type": "application/json"
        }
        try:
            raw_repos_data = requests.get(url,  headers=headers)
            raw_repos_data.raise_for_status()
            self.logger.info('* Try to get user repositories"')
            self.repositories = [
                repository['name'] for repository in raw_repos_data.json()
            ]
        except requests.exceptions.RequestException:
            self.logging.error(f"Failed to get user repositories (status code = {raw_repos_data.status_code})")
            raise Exception(f"Failed to get user repositories (status code = {raw_repos_data.status_code})")

    def create_repository(self, name):
        self.new_repository_name = name
        url = self.base_url + '/user/repos'
        data = {
            "name": name,
            "private": True,
        }
        headers = {
            "Authorization": f"token {os.getenv('GIT_TOKEN')}",
            "Content-Type": "application/json"
        }
        try:
            self.logger.info('* Try create new repository"')
            response = requests.post(
                url,
                headers=headers,
                data=json.dumps(data)
            )
            response.raise_for_status()
        except requests.exceptions.RequestException as e:
            self.logging.error(f'Cannot create repository {name}: {e}')
            raise Exception(f'Cannot create repository {name}: {e}')

    def delete_repository(self, name):
        self.deleted_repository_name = name
        owner = os.getenv('GIT_USER')
        url = f'{self.base_url}/repos/{owner}/{name}'
        headers = {
            "Authorization": f"token {os.getenv('GIT_TOKEN')}",
            "Content-Type": "application/json"
        }
        try:
            response = requests.delete(url, headers=headers)
            response.raise_for_status()
        except requests.exceptions.RequestException as e:
            self.logging.error(f'Cannot delete repository {name}: {e}')
            raise Exception(f'Cannot delete repository {name}: {e}')

    def assert_getting_repositories(self):
        try:
            assert len(self.repositories) > 0
            self.logger.info('*** Test completed successful ***')
        except AssertionError:
            self.logging.error('!!! Test failed !!!')
            raise

    def assert_create_repository(self):
        try:
            self.get_user_repositories()
            self.logger.info('* Check new repo in user repositories"')
            assert self.new_repository_name in self.repositories
            self.logger.info('*** Test completed successful ***')
        except AssertionError:
            self.logging.error('!!! Test failed !!!')
            raise

    def assert_delete_repository(self):
        try:
            self.get_user_repositories()
            self.logger.info('* Check new repo  not in user repositories"')
            assert self.deleted_repository_name not in self.repositories
            self.logger.info('*** Test completed successful ***')
        except AssertionError:
            self.logging.error('!!! Test failed !!!')
            raise
