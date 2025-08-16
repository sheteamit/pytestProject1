import requests

class APIClient:
    def get(self, url, headers,params=None):
        return requests.get(url, params=params)
    def post(self, url, json=None, headers=None):
        return requests.post(url, json=json, headers=headers)
    def put(self, url, json=None, headers=None):
        return requests.put(url, json=json, headers=headers)