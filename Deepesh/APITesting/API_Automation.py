import requests

url = "https://api.restful-api.dev/objects"

payload = {}
headers = {}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.status_code)
print(response.text)

for data in response.json():
    print(data)


