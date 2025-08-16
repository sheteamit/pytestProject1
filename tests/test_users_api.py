import pytest
from utils.api_client import APIClient
import logging
headers = {'x-api-key': 'reqres-free-v1'}
logger =logging.getLogger()
logger.setLevel(logging.DEBUG)
class TestUsersAPI:
    client = APIClient()

    # def test_get_users(self, base_url):
    #     response = self.client.get(f"{base_url}/api/users", headers=headers)
    #     print(response.text)
    #     assert response.status_code == 200

    def test_register_user(self, base_url):
        data = {"email": "eve.holt@reqres.in","password": "pistol"}
        logger.info("\nheaders : ",headers)

        response = self.client.post(f"{base_url}/api/register", json=data, headers=headers)
        print(response.text)
        assert response.status_code == 200

    def test_update_user(self, base_url):
        # data = {"name": "Test User", "job": "Software Engineer"}
        response = self.client.put(f"{base_url}/api/users/2", headers=headers)

        logger.info(response.text)
        print(response.text)
        # assert response.status_code == 200