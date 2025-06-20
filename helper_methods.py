import requests

from curl import Url
from data import RequestAndResponseKeys as Key

class HelperMethods:

    # Отправляем запрос на создание пользователя через API
    @staticmethod
    def register_new_user(user_data):
        return requests.post(f'{Url.BASE_URL}{Url.REGISTER_USER}', data=user_data)

    # Отправляем запрос на удаление существующего пользователя
    @staticmethod
    def delete_user(access_token):
        return requests.delete(f'{Url.BASE_URL}{Url.DELETE_USER}', headers={Key.AUTH_FIELD_NAME: access_token})
