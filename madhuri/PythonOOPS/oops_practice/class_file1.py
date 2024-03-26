import json
import os

global filepath
filepath ='school_data.json'

class Admin:
    def __init__(self, admin_name="Madhuri", admin_username="madhuri", admin_password='1234'):
        self.admin_name = admin_name
        self.username = admin_username
        self.password = admin_password

    def admin_details(self):
        print("username: ", self.username)
        print("password: ", self.password)


