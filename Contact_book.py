class ContactBook:
    def __init__(self):
        self.contacts = []

    def add_contact(self, name, phone, email, address):
        contact = {'Name': name, 'Phone': phone, 'Email': email, 'Address': address}
        self.contacts.append(contact)
        print(f"Contact '{name}' added successfully.")

    def view_contact_list(self):
        if not self.contacts:
            print("Contact list is empty.")
        else:
            print("\nContact List:")
            for contact in self.contacts:
                print(f"Name: {contact['Name']}, Phone: {contact['Phone']}")

    def search_contact(self, keyword):
        found_contacts = []
        for contact in self.contacts:
            if keyword.lower() in contact['Name'].lower() or keyword in contact['Phone']:
                found_contacts.append(contact)

        if not found_contacts:
            print("No matching contacts found.")
        else:
            print("\nMatching Contacts:")
            for contact in found_contacts:
                print(f"Name: {contact['Name']}, Phone: {contact['Phone']}")

    def update_contact(self, name, new_phone=None, new_email=None, new_address=None):
        for contact in self.contacts:
            if contact['Name'].lower() == name.lower():
                if new_phone:
                    contact['Phone'] = new_phone
                if new_email:
                    contact['Email'] = new_email
                if new_address:
                    contact['Address'] = new_address
                print(f"Contact '{name}' updated successfully.")
                return

        print(f"No contact found with the name '{name}'.")

    def delete_contact(self, name):
        for contact in self.contacts:
            if contact['Name'].lower() == name.lower():
                self.contacts.remove(contact)
                print(f"Contact '{name}' deleted successfully.")
                return

        print(f"No contact found with the name '{name}'.")
      
contact_book = ContactBook()

contact_book.add_contact("John Doe", "123-456-7890", "john@example.com", "123 Main St")
contact_book.add_contact("Jane Smith", "987-654-3210", "jane@example.com", "456 Oak Ave")

contact_book.view_contact_list()

contact_book.search_contact("John")

contact_book.update_contact("John Doe", new_phone="555-555-5555")

contact_book.view_contact_list()

contact_book.delete_contact("Jane Smith")

contact_book.view_contact_list()
