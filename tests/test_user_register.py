from datetime import datetime

import requests

from lib.base_case import BaseCase


class TestUserRegister(BaseCase):
    def setup_method(self):
        base_part = "learnqa"
        domain = "example.com"
        ramdom_part = datetime.now().strftime("%m%d%Y%H%M%S")
        self.email = f"{base_part}{ramdom_part}@{domain}"

    def test_create_user_successfully(self):
        data = {
            'password': '123',
            'username': 'learnqa',
            'firstName': 'learnqa',
            'lastName': 'learnqa',
            'email': self.email
        }

        response = requests.post("https://playground.learnqa.ru/api/user/", data=data)

        assert response.status_code == 200, f"Unexpected status code {response.status_code}"
        print(response.content)

    def test_create_user_with_existing_email(self):
        email = 'vinkotov@example.com'
        data = {
            'password': '123',
            'username': 'learnqa',
            'firstName': 'learnqa',
            'lastName': 'learnqa',
            'email': email
        }

        response = requests.post("https://playground.learnqa.ru/api/user/", data=data)

        assert response.status_code == 400, f"Unexpected status code {response.status_code}"
        assert response.content.decode(
            "utf-8") == f"Users with email '{email}' already exists", f"Unexpected response content '{response.content}'"
