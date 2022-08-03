from addressbook import *


class TestAddressbook:
    def test_add_contacts(self):
        address_book = Addressbook()
        contact_dict = {'first_name': "Pooja", 'last_name': "Rana", 'address': "Delhi", 'email': 'gfff',
                        'phone_number': '4323521'}
        contact = Contact(**contact_dict)
        assert len(address_book._people_dict) == 0
        address_book.add_contacts(contact)
        assert len(address_book._people_dict) == 1

    def test_edit(self):
        address_book = Addressbook()
        contact_dict = {'first_name': "Pooja", 'last_name': "Rana", 'address': "Delhi", 'email': 'gfff',
                    'phone_number': '4323521'}
        contact = Contact(**contact_dict)
        assert contact.first_name == "Pooja"
        address_book.edit(contact.first_name,contact.last_name,contact.address,contact.email,contact.phone)
        contact.last_name = 'sharma'
        assert contact.last_name == "sharma"

    def test_remove_contact(self):
        address_book = Addressbook()
        contact_dict = {'first_name': "Pooja", 'last_name': "Rana", 'address': "Delhi", 'email': 'gfff',
                        'phone_number': '4323521'}
        contact = Contact(**contact_dict)
        address_book.add_contacts(contact)
        assert len(address_book._people_dict) == 1
        address_book.remove_contact(contact.first_name)
        assert len(address_book._people_dict) == 0




