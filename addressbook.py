class Contact:

    def __init__(self, first_name, last_name, address, email, phone_number):
        self.first_name = first_name
        self.last_name = last_name
        self.address = address
        self.email = email
        self.phone = phone_number

    def full_name(self):
        return self.first_name + " " + self.last_name

    def details(self):
        return f"{self.full_name()},{self.address},{self.email},{self.phone}"


class Addressbook:
    """
    creating a class in which we define functions for addressbook
    """

    def __init__(self):

        self._people_dict = {}

    def add_contacts(self, contact_object):
        """
        method to read all values from addressbook
        """
        self._people_dict.update({contact_object.first_name: contact_object})

    def all_values(self):
        """
        method to read all values from addressbook
        """
        # Iterate over all values of the dictionary
        for key, value in self._people_dict.items():
            print(key, value.details())

    def edit(self, first_name, last_name, address, email, phone):
        """
          method to edit existing data in addressbook
        """
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

    """
    method to remove contact from the addressbook
    """

    def remove_contact(self, first_name):
        contact = self.get_contact(first_name)
        if not contact:
            print("given name not exists")
            return
        self._people_dict.pop(first_name)

        print("contact deleted successfully")


if __name__ == "__main__":
    address_book = Addressbook()


    def choice1():
        print("Enter the First name :")
        first_name = input()
        print("Enter the Last name :")
        last_name = input()
        print("Enter the Address :")
        address = input()
        print("Enter the Email :")
        email = input()
        print("Enter the Phone Number :")
        phone = input()
        contact1 = Contact(first_name, last_name, address, email, phone)

        address_book.add_contacts(contact1)


    def choice2():
        address_book.all_values()


    def choice3():
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


    def choice4():
        key = input("Enter key to check:")
        address_book.remove_contact(key)


    def default():
        print("Please choose correct option")


    switcher = {
        1: choice1,
        2: choice2,
        3: choice3,
        4: choice4,

    }
    while True:
        print("Enter the option : \n1)Add Contact \n2)Display contact\n3)update contact\n4)RemoveContact")
        option = int(input())
        if option == 1:
            switcher.get(option)()

        elif option == 2:
            switcher.get(option)()

        elif option == 3:
            switcher.get(option)()

        elif option == 4:
            switcher.get(option)()

        else:
            default()


