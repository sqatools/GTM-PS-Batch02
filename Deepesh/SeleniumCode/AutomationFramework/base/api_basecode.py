import requests


class APIMethods:

    def get_api_call(self, url, headers=None, payload=None, auth=None):
        response = requests.request("GET", url, headers=headers, data=payload, auth=auth)
        return response

    def post_api_call(self, url, headers=None, payload=None, auth=None):
        response = requests.request("POST", url, headers=headers, data=payload, auth=auth)
        return response

    def put_api_call(self, url, headers=None, payload=None, auth=None):
        response = requests.request("PUT", url, headers=headers, data=payload, auth=auth)
        return response

    def patch_api_call(self, url, headers=None, payload=None, auth=None):
        response = requests.request("PATCH", url, headers=headers, data=payload, auth=auth)
        return response

    def delete_api_call(self, url, headers=None, payload=None, auth=None):
        response = requests.request("DELETE", url, headers=headers, data=payload, auth=auth)
        return response
