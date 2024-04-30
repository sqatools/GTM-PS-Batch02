from datetime import  datetime
import json


def get_unique_name():
    return datetime.now().strftime("%d_%m_%Y_%H_%M_%S")

def read_json_file(filename="data/testcase_data.json"):
    with open(filename) as file:
        data = file.read()
        json_data = json.loads(data)
        return json_data



