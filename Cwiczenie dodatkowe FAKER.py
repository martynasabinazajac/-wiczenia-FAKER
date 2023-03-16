from faker import Faker


fake=Faker()

class Contact_list:

    
    def __init__(self, name, company, job, email):
        self.name=name
        self.company=company
        self.job=job
        self.email=email


    def __str__(self):
        return f'Name:{self.name},e-mail:<{self.email}>'
        


list=[]

for x in range (5):
    contact=Contact_list(fake.name, fake.company, fake.job, fake.address)
    list.append(contact)


def display_list():
    for contact in list:
        print(contact.name, contact.company, contact.job, contact.email)

display_list()