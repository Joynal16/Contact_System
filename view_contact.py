def view_cont(all_contacts):
    if all_contacts != {}:
        for contact in all_contacts:
            print(f"Name: {contact['name']} | Email: {contact['email']} | Number: {contact['number']} | Address: {contact['address']}")
    else:
        print("No contact found in All contacts")