import requests

from core.constants import BASE_URL


class Book:

    def __init__(self):
        self.base_url = BASE_URL + "BookStore/v1/Books"

    def get_books(self):
        return requests.get(self.base_url)
