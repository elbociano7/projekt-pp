import requests

class Request:

    def __init__(self, server_url, endpoint, payload):
        self.url = server_url
        self.endpoint = endpoint
        self.payload = payload

    def make(self):
        response = requests.get(f"{self.url}{self.endpoint}", data=self.payload)
        print(response)
