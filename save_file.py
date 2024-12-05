def save_contact(all_contacts):
    with open("all_contacts.csv","w") as fp:
        for book in all_books:
            line = f"{contact['name']},{contact['email']},{contact['number']},{contact['address']}\n"
            fp.write(line)