import unittest
import pyperclip
from contact import Contact

class TestContact(unittest.TestCase):
  def setUp(self):
    self.new_contact = Contact("james", "Muriuki", "james@gmail.com", "0712345678")

  def test__init(self):
    self.assertEqual(self.new_contact.fname, "james")
    self.assertEqual(self.new_contact.lname, "Muriuki")
    self.assertEqual(self.new_contact.email, "james@gmail.com")
    self.assertEqual(self.new_contact.phone_number, "0712345678")

  def test_save_contact(self):
    self.new_contact.save_contact()
    self.assertEqual(len(Contact.contact_list), 1)

  def tearDown(self):
    Contact.contact_list = []

  def test_save_multiple_contact(self):
    self.new_contact.save_contact()
    test_contact = Contact("Test", "Caller", "test@gmail.com", "0718007324")
    test_contact.save_contact()
    self.assertEqual(len(Contact.contact_list),2)

  def test_delete_contact(self):
    self.new_contact.save_contact()
    test_contact = Contact("Gerald", "Steel", "steel@gmail.com", "0723591588")
    test_contact.save_contact()

    self.new_contact.delete_contact()
    self.assertEqual(len(Contact.contact_list), 1)

  def test_find_contact_by_number(self):
    self.new_contact.save_contact()
    test_contact = Contact("Bill", "Gates", "billgates@gmail.com", "0718007324")
    test_contact.save_contact()

    found_contact = Contact.find_by_number("0718007324")
    self.assertEqual(found_contact.email, test_contact.email)

  def test_contact_exists(self):
    self.new_contact.save_contact()
    test_contact = Contact("leo", "Kipyegon", "leo@gmail.com", "0720467615")
    test_contact.save_contact()
    contact_exists = Contact.contact_exist("0720467615")
    self.assertTrue(contact_exists)

  def test_display_all_contacts(self):
    self.assertEqual(Contact.display_contacts(), Contact.contact_list)

  #PYPERCLIP
  def test_copy_email(self):
    self.new_contact.save_contact()
    Contact.copy_email("0712345678")
    self.assertEqual(self.new_contact.email, pyperclip.paste())

if __name__ == '__main__':
    unittest.main()



