import json

from base.api_basecode import APIMethods


class MobileAPI(APIMethods):

    def get_all_mobile_details(self):
        api_url = "https://api.restful-api.dev/objects"
        response = self.get_api_call(url=api_url)
        json_data = json.loads(response.text)
        status = response.status_code
        return status, json_data
