class Contact:

    def __init__(self, f_name, l_name, address, email, phone_number):
        self.first_name = f_name
        self.last_name = l_name
        self.address = address
        self.email = email
        self.phone = phone_number

    def full_name(self):
        return self.first_name + " " + self.last_name


class Addressbook:

    def __init__(self):
        self._people_dict = {}
        # {contact1.first_name:contact1,contact2.first_name:contact2}

    def add_contacts(self, contact_object):

        num = int(input("Please enter initial number of contacts: "))

        for i in range(num):
            print("Enter the First name :")
            contact_object.first_name = input()
            print("Enter the Last name :")
            contact_object.last_name = input()
            print("Enter the Address :")
            contact_object.address = input()
            print("Enter the Email :")
            contact_object.email = input()
            print("Enter the Phone Number :")
            contact_object.phone = input()
            self._people_dict.update({contact_object.first_name: contact_object})

    def all_values(self):
        # Iterate over all values of the dictionary
        for key, value in self._people_dict.items():
            print(key, f"{value.full_name()},{value.address},{value.email},{value.phone}")

    def edit(self, contact_object):

        key = input("Enter key to check:")
        if key in self._people_dict:
            print("given name contact exists")
            print(
                "choose the option to change the data : \n1) firstName\n2)lastName\n3)address\n4)Email\n5)Phone "
                "Number")
            choice = int(input())
            if choice == 1:
                print("Please enter the first name : ")
                first_name = input()
                contact_object.first_name = first_name
            elif choice == 2:
                print("Please enter the last name : ")
                last_name = input()
                contact_object.last_name = last_name
            elif choice == 3:
                print("Please enter the Address : ")
                address = input()
                contact_object.address = address
            elif choice == 4:
                print("Please enter the email : ")
                email = input()
                contact_object.email = email
            elif choice == 5:
                print("Please enter the Phone Number : ")
                phone = input()
                contact_object.phone = phone
            else:
                print("please choose from above options :")

            print("updated successfully :")

    def remove_contact(self):
        key = input("Enter key to check:")
        if key in self._people_dict:
            print("given name contact exists")
            self._people_dict.pop(key)

            print("contact deleted successfully")
        else:
            print("Key isn't present!")


if __name__ == "__main__":
    address_book = Addressbook()
    contact1 = Contact('f_name', 'l_name', 'address', 'email', 'phone_number')
    while True:
        print("Enter the option : \n1)Add Contact \n2)Display contact\n3)update contact\n4)RemoveContact")
        option = int(input())
        if option == 1:
            address_book.add_contacts(contact1)
        elif option == 2:
            address_book.all_values()
        elif option == 3:
            address_book.edit(contact1)
        elif option == 4:
            address_book.remove_contact()
        else:
            print("Please choose correct option")
