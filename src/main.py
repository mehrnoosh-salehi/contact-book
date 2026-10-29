

class ContactBook:
    """ A class use to represent a contact book
    """
    def __init__(self):
        """ Initialize contact book with an empty dictionary
        """
        self.contacts: dict = {}

    def add_contact(self, name: str, phone: str, email: str, address: str):
        """_summary_

        :param name: The contact name
        :type name: str
        :param phone: The contact phone number
        :type phone: str
        :param email: The contact email address
        :type email: str
        :param address: The contact phisical address
        :type email: str
        """

        if name not in self.contacts:
            self.contacts[name] = {
                'phone': phone,
                'email': email,
                'address': address

            }
            print('Contact added successfully!')
        else:
            print('The contact already exists!')

    def view_contact(self):
        """
        display all contact that you added
        """
        for name, info in self.contacts.items():
            print("Name: ", name)
            print("Phone: ", info['phone'])
            print("Email: ", info['email'])
            print("Address: ", info['address'])
            print('-' * 60)

    def delete_contact(self, name):
        """Deletes a contact from the contact book.
        """
        if name in self.contacts:
            del self.contacts[name]
            print('Contact deleted successfully')

        else:
            print("Contact not found")
        

    def edit_contact(self, name, new_name=None, phone=None, email=None, address=None):
        """Edit a contact from contact book
        """

        if name in self.contacts:
            contact = self.contacts[name]

            if new_name and new_name != name:
                if new_name in self.contacts:
                    print("This contact already exists")
                    return

                del self.contacts[name]
                self.contacts[new_name] = contact

            if phone:
                self.contacts[name]['phone'] = phone
            if email:
                self.contacts[name]['email'] = email
            if address:
                self.contacts[name]['address'] = address
            print('Contact edited successfully!')
        else:
            print('Contact not found!')


if __name__ == '__main__':
    book = ContactBook()
    while True:
        print('\n--Contact Book Application--')
        print('1. Add contact')
        print('2. Edit contact')
        print('3. View contact')
        print('4. Delete contact')
        print('5. Quit')

        user_choice = input('Please choose an option from 1, 2, 3, 4, 5: ')

        if user_choice == '1':
            name = input('\nplease enter contact name: ')
            phone = input('\nplease enter contact phone: ')
            email = input('\nPlease enter contact email: ')
            address = input('\nPlease enter contact address: ')
            book.add_contact(name=name, phone= phone, email=email, address=address)

        elif user_choice == '2':
            name = input("\nEnter name of the contact to edit: ")
            phone = input("Enter new/updated phone number or press Enter to keep unchanged: ")
            email = input("Enter new/updated email or press Enter to keep unchanged: ")
            address = input("Enter new/updated address or press Enter to keep unchanged: ")
            book.edit_contact(name, phone=phone, email=email, address=address)

        elif user_choice == '3':
            print('\nList of contact')
            book.view_contact()

        elif user_choice == '4':
            name = input('\nPlease enter a contact name to delete: ')
            book.delete_contact(name)

        elif user_choice == '5':
            print('\nThank you for using contact book applicatin! Goodbye!!')
            break

        else:
            print("\nInvalid choice! Please try again.")