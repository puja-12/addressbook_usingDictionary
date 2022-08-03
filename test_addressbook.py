import pytest

import addressbook
from addressbook import Addressbook
import test_addressbook


class Test_Addresbook:
    address_book = Addressbook()

    # def __init__(self):
    #
    #
    #     self._people_dict = {}
    #
    # def test_getContacts(self, contact_object):
    #     self._people_dict.update({contact_object.first_name: contact_object})
    # @pytest.fixture
    def test_add(self):
        contact = addressbook.address_book.add_contacts()
        # contact=addressbook.
        contact.first_name('Pooja')
        # contact.last_name('Rana')
        # contact.address('Delhi')
        # contact.email('bhdbs')
        # contact.phone('1234567')
        # addressbook.address_book.add_contacts(contact)
        assert 'Pooja' == contact.first_name
    #
    # def test_updateContact(first_name, last_name, address, email, phone):
    #     contact = addressbook.Contact(first_name, last_name, address, email, phone)
    #     contact.first_name(1)
    #     contact.last_name("Name4")
    #     contact.address("Name4")
    #     contact.email("Name4")
    #     contact.phone("Name4")


    # def test_display_all_contacts(self):
    #     self.assert[self.people_dict, addressbook.address_book.all_values()]
    #
    # def Test_removeCcontact(self):
    #     response = self.people_dict.remove_contact('Pooja')
    #
    #
