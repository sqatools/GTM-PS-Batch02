import json

import requests


def get_api_call():
    url = "https://api.restful-api.dev/objects"

    payload = {}
    headers = {}

    response = requests.request("GET", url, headers=headers, data=payload)

    print(response.status_code)
    print(response.text)

    for data in response.json():
        print(data)

#get_api_call()


def get_api_call_specific_ids():
    url = "https://api.restful-api.dev/objects?id=3&id=5&id=10"

    payload = {}
    headers = {}

    response = requests.request("GET", url, headers=headers, data=payload)

    print(response.status_code)
    print(response.text)

    for data in response.json():
        print(data)


#get_api_call_specific_ids()

def get_api_call_single_id(id_num):
    url = f"https://api.restful-api.dev/objects/{id_num}"

    payload = {}
    headers = {}

    response = requests.request("GET", url, headers=headers, data=payload)

    print(response.status_code)
    print(response.text)

    for data in response.json():
        print(data)


#get_api_call_single_id(6)
#get_api_call_single_id(8)

def post_api_call():
    url = "https://api.restful-api.dev/objects"

    payload = {
               "name": "Apple MacBook Pro 20",
               "data": {
                  "year": 2020,
                  "price": 100000,
                  "CPU model": "Intel Core i10",
                  "Hard disk size": "2 TB"
               }
            }
    headers = {"Content-Type": "application/json"}

    response = requests.request("POST", url, headers=headers, data=json.dumps(payload))

    print(response.status_code)
    print(response.text)

#post_api_call()


# {"id":"ff8081818f28dba8018f343fd46f2133","name":"Apple MacBook Pro 20","createdAt":"2024-05-01T13:02:29.487+00:00","data":{"year":2020,"price":100000,"CPU model":"Intel Core i10","Hard disk size":"2 TB"}}
# {"id":"ff8081818f28dba8018f343fd46f2133","name":"Apple MacBook Pro 20","updatedAt":"2024-05-01T13:05:15.810+00:00","data":{"year":2020,"price":200000,"CPU model":"Intel Core i11","Hard disk size":"3 TB"}}

def put_method_call(object_id):
    url = f"https://api.restful-api.dev/objects/{object_id}"

    payload = {
               "name": "Apple MacBook Pro 20",
               "data": {
                  "year": 2020,
                  "price": 200000,
                  "CPU model": "Intel Core i11",
                  "Hard disk size": "3 TB"
               }
            }
    headers = {"Content-Type": "application/json"}

    response = requests.request("PUT", url, headers=headers, data=json.dumps(payload))

    print(response.status_code)
    print(response.text)

#put_method_call("ff8081818f28dba8018f343fd46f2133")
# {"id":"ff8081818f28dba8018f343fd46f2133","name":"Apple MacBook Pro 20","updatedAt":"2024-05-01T13:05:15.810+00:00","data":{"year":2020,"price":200000,"CPU model":"Intel Core i11","Hard disk size":"3 TB"}}

def patch_method_call(object_id):
    url = f"https://api.restful-api.dev/objects/{object_id}"

    payload = {
                   "name": "Apple MacBook Pro 21",
              }
    headers = {"Content-Type": "application/json"}

    response = requests.request("PATCH", url, headers=headers, data=json.dumps(payload))

    print(response.status_code)
    print(response.text)

patch_method_call("ff8081818f28dba8018f343fd46f2133")
# {"id":"ff8081818f28dba8018f343fd46f2133","name":"Apple MacBook Pro 21","updatedAt":"2024-05-01T13:11:42.575+00:00","data":{"year":2020,"price":200000,"CPU model":"Intel Core i11","Hard disk size":"3 TB"}}
# {"error":"The Object with id = ff8081818f28dba8018f343fd46f2133 doesn't exist. Please provide an object id which exists or generate a new Object using POST request and capture the id of it to use it as part of PATCH request after that."}


def delete_api_call(object_id):
    url = f"https://api.restful-api.dev/objects/{object_id}"

    payload = {
              }
    headers = {"Content-Type": "application/json"}

    response = requests.request("DELETE", url, headers=headers, data=payload)

    print(response.status_code)
    print(response.text)

# delete_api_call("ff8081818f28dba8018f343fd46f2133")
# {"message":"Object with id = ff8081818f28dba8018f343fd46f2133 has been deleted."}
