import requests
import os
import json


class ApiClient:
    def __init__(self, base_url):
        self.base_url = base_url
        self.repositories = []

    def get_valid_request(self, endpoint, schema, params=None, ):
        url = f'{self.base_url}{endpoint}'
        response = requests.get(
            url,
            params,
            headers=self.headers,
            verify=False
        )

        data = response.json()
        [schema(**item) for item in data['results']]
        return response

    def get_user_repositories(self):
        url = self.base_url + '/user/repos'
        headers = {
            "Authorization": f"token {os.getenv('GIT_TOKEN')}",
            "Content-Type": "application/json"
        }
        try:
            raw_repos_data = requests.get(url,  headers=headers)
            raw_repos_data.raise_for_status()
            for repository in raw_repos_data.json():
                self.repositories.append(repository['name'])
        except requests.exceptions.RequestException:
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
            response = requests.post(
                url,
                headers=headers,
                data=json.dumps(data)
            )
            response.raise_for_status()
        except:
            raise Exception('Хуй')

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
        except:
            raise Exception('Хуй2')

    def assert_getting_repositories(self):
        assert len(self.repositories) > 0

    def assert_create_repository(self):
        self.get_user_repositories()
        assert self.new_repository_name in self.repositories

    def assert_delete_repository(self):
        self.get_user_repositories()
        assert self.deleted_repository_name not in self.repositories
