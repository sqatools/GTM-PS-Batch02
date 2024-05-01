import json

import requests

"""
# website for API testing with Authentication

https://gorest.co.in/
"""


def get_api_call_with(url, headers= {}, payload={}):

    response = requests.request("GET", url, headers=headers, data=payload)
    #response = requests.request("GET", url, headers=headers, data=payload, auth=(username, password))

    print(response.status_code)
    print(response.text)

    for data in response.json():
        print(data)


URL = "https://gorest.co.in/public/v2/users"
headers = {
  'Authorization': 'Bearer 3dd714d8136c1dd602bf48f6279faffc781af759084e87c1a0186e96cbcdac14'
}

get_api_call_with(url=URL, headers=headers)



posts_url = "https://gorest.co.in/public/v2/posts"
posts_headers = {
  'Authorization': 'Bearer a6834a99361fe4c8898e305e9fbce62f9138d781849ff7c8285a5fc1b667d041'
}

print("_"*40)
get_api_call_with(url=posts_url, headers=posts_headers)


#headers = { 'Authorization' : basic_auth(username, password) }
