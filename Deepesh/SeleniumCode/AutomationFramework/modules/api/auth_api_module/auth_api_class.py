from base.api_basecode import APIMethods
from data.api_data.api_session_data import *


class AuthAPI(APIMethods):

    def get_all_users_details(self):
        url = f'{api_base_url}/users'
        headers = {
            'Authorization': f'Bearer {api_auth_bearer_token}'
        }
        response = self.get_api_call(url=url, headers=headers)
        return response

    def get_all_posts_details(self):
        url = f'{api_base_url}/posts'
        headers = {
            'Authorization': f'Bearer {api_auth_bearer_token}'
        }
        response = self.get_api_call(url=url, headers=headers)
        return response


    def get_all_comments(self):
        url = f"{api_base_url}/comments"
        headers = {
            'Authorization': f'Bearer {api_auth_bearer_token}'
        }
        response = self.get_api_call(url=url, headers=headers)
        return response

    def get_all_to_do_list(self):
        url = f"{api_base_url}/todos"
        headers = {
            'Authorization': f'Bearer {api_auth_bearer_token}'
        }
        response = self.get_api_call(url=url, headers=headers)
        return response
