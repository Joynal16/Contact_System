from contact_management import all_contacts
from save_file import save_file
from contact_management import all_contacts

def add_contact(all_contact):
    name = input("enter book ISBN number : ")
    email = input("enter the  publishing year : ")
    number = int(input("enter the price: "))
    address = input("enter the Quantity: ")


    contact = {
        "name":name,
        "email":email,
        "number":number,
        "address":address
    }


    all_contacts.apend(contact)
    save_file(contact)
    print("Contact added successfully")
    return (all_contacts)


