class Contact:

    def __init__(self, f_name, l_name, address, email, phone_number):
        self.first_name = f_name
        self.last_name = l_name
        self.address = address
        self.email = email
        self.phone = phone_number


class Addressbook:

    def __init__(self):
        self._people_dict = {}
        # {contact1.first_name:contact1,contact2.first_name:contact2}

    def add_contacts(self, contact_object):
        self._people_dict.update({contact_object.first_name: contact_object})
        self._people_dict.update({contact_object.last_name: contact_object})
        self._people_dict.update({contact_object.address: contact_object})
        self._people_dict.update({contact_object.email: contact_object})
        self._people_dict.update({contact_object.phone: contact_object})

    def all_values(self):
        # Iterate over all values of the dictionary
        for key, value in self._people_dict.items():
            print(key, value)

    def edit(self, contact_object):
        self._people_dict[contact_object.first_name] = 'Richa'
        self._people_dict[contact_object.last_name] = 'Mishra'
        self._people_dict[contact_object.address] = 'UP'
        self._people_dict[contact_object.email] = 'dscnsj@123'
        self._people_dict[contact_object.phone] = '567894390'
        print(self._people_dict)

    def delete(self, contact_object):
        del self._people_dict[contact_object.first_name]
        del self._people_dict[contact_object.last_name]
        del self._people_dict[contact_object.address]
        del self._people_dict[contact_object.email]
        del self._people_dict[contact_object.phone]
        print("Deleted the contact.")


if __name__ == "__main__":
    address_book = Addressbook()
    contact1 = Contact(f_name="Pooja", l_name="Rana", address="Delhi", email="pooja@123", phone_number="786869543")
    contact2 = Contact(f_name="Rahul", l_name="Sharma", address="Meerut", email="rahul@123", phone_number="123456789")

    while True:
        print("Enter the option : \n1)Add Contact \n2)Display contact\n3)update contact\n4)RemoveContact")
        option = int(input())
        if option == 1:
            address_book.add_contacts(contact1)
            address_book.add_contacts(contact2)
            print(address_book._people_dict)
            # x = address_book._people_dict.get("xyz")
            # y = address_book._people_dict.get("dhhdf")
            # print(y.phone)
            # print(x.phone)
        elif option == 2:
            address_book.all_values()
        elif option == 3:
            address_book.edit(contact2)
        elif option == 4:
            address_book.delete(contact2)
        else:
            print("Please choose correct option")