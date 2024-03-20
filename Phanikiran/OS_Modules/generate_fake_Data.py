"""
pip install faker
"""
from faker import Faker

fk = Faker()

print("first name :", fk.first_name())
print("lastname :", fk.last_name())


with open("test_data.txt", "a") as file:
    for i in range(50):
        fist_name = fk.first_name()
        last_name = fk.last_name()
        address = fk.address()
        email = fk.email()
        line = f"{fist_name}, {last_name}, {address}, {email}\n"
        file.write(line)




