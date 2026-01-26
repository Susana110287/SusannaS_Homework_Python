import requests


class ProjectYouGile:
    # Инициализация
    def __init__(self, url) -> None:
        self.url = url

    # Получить ключ авторизации
    def get_token(self):
        payload = {
            "login": "данные в письме о сдаче ДЗ",
            "password": "данные в письме о сдаче ДЗ",
            "companyId": "данные в письме о сдаче ДЗ"
        }
        resp = requests.post(self.url + 'auth/keys/get', json=payload)
        return resp.json()[0]['key']

    # Получить список проектов
    def get_project_list(self):
        key = self.get_token()
        headers = {
            'Authorization': f'Bearer {key}',
            'Content-Type': 'application/json'
        }

        resp = requests.get(self.url + 'projects', headers=headers)
        return resp.json()['content']

    # Добавить проект:
    def create_project(self, title, users):
        key = self.get_token()
        headers = {
            'Authorization': f'Bearer {key}',
            'Content-Type': 'application/json'
        }
        body = {
            "title": title,
            "users": users
        }
        resp = requests.post(self.url + 'projects',
                             headers=headers,
                             json=body)
        return resp.json()

    # Получить проект по id
    def get_project_with_id(self, project_id):
        key = self.get_token()
        headers = {
            'Authorization': f'Bearer {key}'
        }
        resp = requests.get(self.url + f'projects/{project_id}',
                            headers=headers)
        return resp.json()

    # Изменить название проекта
    def edit_project(self, project_id, new_deleted, new_title):
        key = self.get_token()
        headers = {
            'Authorization': f'Bearer {key}',
            'Content-Type': 'application/json'
        }
        project = {
            "deleted": new_deleted,
            "title": new_title
        }
        resp = requests.put(self.url + f'projects/{project_id}',
                            headers=headers, json=project)
        return resp.json()
