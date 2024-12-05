from add_contact import add_contact
from view_contact import view_cont
all_contacts ={

}


while True:
    print("Welcome to Contact Management System")
    print("0.Exit")
    print("1. Add Contacts")
    print("2. View All Contact")
    print("3. Save All the Contact")

    option=input("Choose a option: ")

    if option == "0":
        print("Welcome to Contact Management System")
        break
    elif option == "1":
        all_contacts=add_contact.add_contact(all_contacts)
    elif option == "2":
        view_contact=view_cont(all_contacts)
