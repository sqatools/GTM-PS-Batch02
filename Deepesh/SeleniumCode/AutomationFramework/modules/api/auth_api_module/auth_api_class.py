from base.api_basecode import APIMethods
from data.api_data.api_session_data import *


class AuthAPI(APIMethods):

    def get_all_users_details(self):
        url = 'https://gorest.co.in/public/v2/users'
        headers = {
            'Authorization': f'Bearer {api_auth_bearer_token}'
        }
        response = self.get_api_call(url=url, headers=headers)
        return response
