from faker import Faker
fk = Faker()
#print(dir(fk))

user_details = {
    "first_name" : "John",
    "last_name" : "Doe",
    "DOB" : "04/24/2024",
    "select_pass" : "Add 2 more passenger (200%)",
    "from_city" : "Mumbai",
    "dest_city" : "Bangalore",

    "billing_name" : fk.user_name(),
    "billing_phone" : fk.phone_number(),
    "billing_email" : fk.email(),
    "billing_address" : fk.address(),
    "billing_postal_code" : fk.zipcode(),
    "billing_prefecture" : fk.zipcode_in_state()

}

