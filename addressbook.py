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

    def add_contacts(self):

        num = int(input("Please enter initial number of contacts: "))

        for i in range(num):
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
            self._people_dict.update({contact1.first_name: contact1})

    def all_values(self):
        # Iterate over all values of the dictionary
        for key, value in self._people_dict.items():
            print(key, f"{value.full_name()},{value.address},{value.email},{value.phone}")

    def edit(self):

        key = input("Enter key to check:")
        if key in self._people_dict:
            update= self._people_dict.get(key)
            print("given name contact exists")
            print(
                "choose the option to change the data : \n1) firstName\n2)lastName\n3)address\n4)Email\n5)Phone "
                "Number")
            choice = int(input())
            if choice == 1:
                print("Please enter the first name : ")
                first_name = input()
                update.first_name = first_name
            elif choice == 2:
                print("Please enter the last name : ")
                last_name = input()
                update.last_name = last_name
            elif choice == 3:
                print("Please enter the Address : ")
                address = input()
                update.address = address
            elif choice == 4:
                print("Please enter the email : ")
                email = input()
                update.email = email
            elif choice == 5:
                print("Please enter the Phone Number : ")
                phone = input()
                update.phone = phone
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

    while True:
        print("Enter the option : \n1)Add Contact \n2)Display contact\n3)update contact\n4)RemoveContact")
        option = int(input())
        if option == 1:
            address_book.add_contacts()
        elif option == 2:
            address_book.all_values()
        elif option == 3:
            address_book.edit()
        elif option == 4:
            address_book.remove_contact()
        else:
            print("Please choose correct option")
