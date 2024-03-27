import json

def read_json_data (filename) :
    with open(filename,"r") as file:
        file_data = file.read()
        data = json.loads(file_data)
        print(data)
        return data


#output = read_json_data("test_data.json")
#print("name: ", output["name"])

def write_content_json_file(filename, content):
    with open(filename,"w") as file:
        data= json.dumps(content)
        file.write(data)

dic = {
  "name" : "Priya",
  "phone" : 88725678,
  "email" : "priya@gmail.com"
}

write_content_json_file("new_json_file.json", dic)