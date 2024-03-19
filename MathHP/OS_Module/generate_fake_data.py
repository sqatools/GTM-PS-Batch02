################ Last 2 lines pending


"""
pip install faker

pip install faker d

do in cmd command prompt

"""

from faker  import Faker
fk = Faker()

print("user_name:",fk.first_name())           # This is a random generator
print("lastname:",fk.last_name())

#user_name: Christine
#lastname: Torres

print(dir(fk))

with open("test_data.txt","a") as file:
    for i in range(50):
        first_name = fk.first_name()
        last_name = fk.last_name()
        address = fk.address()
        email = fk.email()
        line = f"{first_name},{last_name},{address},{email}"




