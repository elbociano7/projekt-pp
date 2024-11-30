from urllib.parse import urlencode

import requests

from src.configuration import CONFIG


class Request:
    endpoint = None

    def __init__(self, server_url):
        self.url = server_url

    @staticmethod
    def fromConfig():
        """
        Make a request object from configuration.

        :return Request: Request object
        """
        return Request(CONFIG.get('API_URL'))

    def build(self, endpoint, payload):
        """
        Build a request object from payload and endpoint. Payload is encoded as GET request's parameters.
        :param endpoint:
        :param payload:
        :return:
        """
        payload = str(urlencode(payload))
        self.endpoint = endpoint + "?" + payload


    def make(self):
        """
        Makes a request based on object's configuration and returns request data if response code is 200.
        :return array: Response data
        """
        if self.endpoint is None:
            raise Exception("Endpoint is not set")
        response = requests.get(f"{self.url}{self.endpoint}")
        if response.ok:
            return response.json()
        return []
