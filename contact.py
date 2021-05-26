import pyperclip
class Contact:

  contact_list = []

  def __init__(self,fname,lname,email,phone_number):
    self.fname = fname
    self.lname = lname
    self.email = email
    self.phone_number = phone_number

  def save_contact(self):
    Contact.contact_list.append(self)

  def delete_contact(self):
    Contact.contact_list.remove(self)

  @classmethod
  def find_by_number(cls,number):
    for contact in cls.contact_list:
      if contact.phone_number == number:
        return contact
  
  @classmethod
  def contact_exist(cls,number):
    for contact in cls.contact_list:
      if contact.phone_number == number:
        return True
    return False

  @classmethod
  def display_contacts(cls):
    return cls.contact_list

  @classmethod
  def copy_email(cls,number):
    contact_found = Contact.find_by_number(number)
    pyperclip.copy(contact_found.email)