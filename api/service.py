import os
import requests
from dotenv import load_dotenv


load_dotenv()


URL_API = os.getenv('URL_API')


class Auth:
    def __init__(self):
        self.__base_url = URL_API
        self.__auth_url = f'{self.__base_url}authentication/token/'

    def get_token(self, username, password):
        auth_payload = {
            'username': username,
            'password': password
        }

        auth_response = requests.post(
            self.__auth_url,
            data=auth_payload
        )

        if auth_response.status_code == 200:
            return auth_response.json()
        else:
            return {'error': f'Erro ao autenticar. Status code: {auth_response.status_code}'}
