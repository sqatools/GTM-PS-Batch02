import requests
from utilities.get_logger import logger

log = logger


class APIMethods:

    def get_api_call(self, url, headers=None, payload=None, auth=None):
        log.info(f"Get call with :{url}, header = {headers}, payload: {payload}")
        response = requests.request("GET", url, headers=headers, data=payload, auth=auth)
        log.info(f"{response.status_code}")
        log.info(f"{response.text}")
        return response

    def post_api_call(self, url, headers=None, payload=None, auth=None):
        log.info(f"POST call with :{url}, header = {headers}, payload: {payload}")
        response = requests.request("POST", url, headers=headers, data=payload, auth=auth)
        log.info(f"{response.status_code}")
        log.info(f"{response.text}")
        return response

    def put_api_call(self, url, headers=None, payload=None, auth=None):
        log.info(f"PUT API call with :{url}, header = {headers}, payload: {payload}")
        response = requests.request("PUT", url, headers=headers, data=payload, auth=auth)
        log.info(f"{response.status_code}")
        log.info(f"{response.text}")
        return response

    def patch_api_call(self, url, headers=None, payload=None, auth=None):
        log.info(f"PATCH API call with :{url}, header = {headers}, payload: {payload}")
        response = requests.request("PATCH", url, headers=headers, data=payload, auth=auth)
        log.info(f"{response.status_code}")
        log.info(f"{response.text}")
        return response

    def delete_api_call(self, url, headers=None, payload=None, auth=None):
        log.info(f"PATCH API call with :{url}, header = {headers}, payload: {payload}")
        response = requests.request("DELETE", url, headers=headers, data=payload, auth=auth)
        log.info(f"{response.status_code}")
        log.info(f"{response.text}")
        return response
