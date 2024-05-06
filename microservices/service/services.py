import requests

class Services:
    def __init__(self):
        self.api_url = 'http://localhost:5000/api/v1'

    def get_users(self):
        """Get a list of users from the API."""
        response = requests.get(f'{self.api_url}/users')
        return response.json()

    def get_user(self, user_id):
        """Get a specific user from the API."""
        response = requests.get(f'{self.api_url}/users/{user_id}')
        return response.json()
