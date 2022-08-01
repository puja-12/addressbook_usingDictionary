class Contact:

    def __init__(self, f_name, l_name, address, email, phone_number):
        self.first_name = f_name
        self.last_name = l_name
        self.address = address
        self.email = email
        self.phone = phone_number

    def full_name(self):
        return self.first_name + " " + self.last_name

    def details(self):
        return f"{self.full_name()},{self.address},{self.email},{self.phone}"


class Addressbook:

    def __init__(self):
        self._people_dict = {}
        # {contact1.first_name:contact1,contact2.first_name:contact2}

    def add_contacts(self, contact_object):
        self._people_dict.update({contact_object.first_name: contact_object})

    def all_values(self):
        # Iterate over all values of the dictionary
        for key, value in self._people_dict.items():
            print(key, value.details())

    def edit(self, first_name, last_name, address, email, phone):
        contact = self.get_contact(first_name)
        if not contact:
            print("key is not present")
            return

        contact.last_name = last_name
        contact.address = address
        contact.email = email
        contact.phone = phone
        print("updated successfully")

    def get_contact(self, first_name):
        return self._people_dict.get(first_name)

    def remove_contact(self, first_name):
        contact = self.get_contact(first_name)
        if not contact:
            print("given name not exists")
            return
        self._people_dict.pop(first_name)

        print("contact deleted successfully")


if __name__ == "__main__":
    address_book = Addressbook()

    while True:
        print("Enter the option : \n1)Add Contact \n2)Display contact\n3)update contact\n4)RemoveContact")
        option = int(input())
        if option == 1:
            contact1 = Contact('f_name', 'l_name', 'address', 'email', 'phone_number')
            print("Enter the First name :")
            contact1.first_name = input()
            print("Enter the Last name :")
            contact1.last_name = input()
            print("Enter the Address :")
            contact1.address = input()
            print("Enter the Email :")
            contact1.email = input()
            print("Enter the Phone Number :")
            contact1.phone = input()
            address_book.add_contacts(contact1)
        elif option == 2:
            address_book.all_values()
        elif option == 3:
            key = input("Enter key to check:")
            print("given name contact exists")
            print("Please enter the last name : ")
            last_name = input()
            print("Please enter the Address : ")
            address = input()
            print("Please enter the email : ")
            email = input()
            print("Please enter the Phone Number : ")
            phone = input()
            address_book.edit(key, last_name, address, email, phone)
        elif option == 4:
            key = input("Enter key to check:")
            address_book.remove_contact(key)

        else:
            print("Please choose correct option")
