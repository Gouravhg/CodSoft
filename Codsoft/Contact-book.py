import sys

class Contact:
    def __init__(self, name, phone, email, address):
        self.name = name
        self.phone = phone
        self.email = email
        self.address = address

    def __str__(self):
        return f"Name: {self.name}\nPhone: {self.phone}\nEmail: {self.email}\nAddress: {self.address}"

class ContactList:
    def __init__(self):
        self.contacts = []

    def add_contact(self, name, phone, email, address):
        new_contact = Contact(name, phone, email, address)
        self.contacts.append(new_contact)
        print(f"Contact '{name}' added successfully.")

    def view_contacts(self):
        if not self.contacts:
            print("No contacts available.")
        else:
            for idx, contact in enumerate(self.contacts):
                print(f"\nContact {idx + 1}:")
                print(contact)

    def search_contact(self, search_term):
        found_contacts = [contact for contact in self.contacts if search_term.lower() in contact.name.lower() or search_term in contact.phone]
        if found_contacts:
            for contact in found_contacts:
                print(f"\nFound Contact:\n{contact}")
        else:
            print("No contacts found.")

    def update_contact(self, search_term):
        for contact in self.contacts:
            if search_term.lower() in contact.name.lower() or search_term in contact.phone:
                print("\nCurrent Contact Details:")
                print(contact)

                name = input("Enter new name (leave blank to keep current): ") or contact.name
                phone = input("Enter new phone (leave blank to keep current): ") or contact.phone
                email = input("Enter new email (leave blank to keep current): ") or contact.email
                address = input("Enter new address (leave blank to keep current): ") or contact.address

                contact.name = name
                contact.phone = phone
                contact.email = email
                contact.address = address

                print(f"\nContact '{name}' updated successfully.")
                return

        print("No contact found with that name or phone number.")

    def delete_contact(self, search_term):
        for contact in self.contacts:
            if search_term.lower() in contact.name.lower() or search_term in contact.phone:
                self.contacts.remove(contact)
                print(f"\nContact '{contact.name}' deleted successfully.")
                return

        print("No contact found with that name or phone number.")

def main():
    contact_list = ContactList()

    while True:
        print("\nContact Management System")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")
        
        choice = input("Choose an option: ")

        if choice == '1':
            name = input("Enter name: ")
            phone = input("Enter phone number: ")
            email = input("Enter email: ")
            address = input("Enter address: ")
            contact_list.add_contact(name, phone, email, address)
        
        elif choice == '2':
            contact_list.view_contacts()

        elif choice == '3':
            search_term = input("Enter name or phone number to search: ")
            contact_list.search_contact(search_term)

        elif choice == '4':
            search_term = input("Enter name or phone number to update: ")
            contact_list.update_contact(search_term)

        elif choice == '5':
            search_term = input("Enter name or phone number to delete: ")
            contact_list.delete_contact(search_term)

        elif choice == '6':
            print("Exiting the application.")
            sys.exit()
        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main()
