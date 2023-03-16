from faker import Faker

fake=Faker()

class Fake_contact_list:

    def __init__(self, name, email):
        self.name=name
        self.email=email

    def __str__(self):
       return f'Name:{self.name}, email: {self.email} '
    
    
contact=Fake_contact_list(fake.name(), fake.email())

print(contact)

