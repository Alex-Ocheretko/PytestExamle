import requests

from utils.base_utils import BASE_UPL


class Book:

    def __init__(self):
        self.base_url = BASE_UPL + "BookStore/v1/Books"

    def get_books(self):
        return requests.get(self.base_url)
