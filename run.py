#!/usr/bin/env python3.8

from contact import Contact

def create_contact(fname,lname,email,phone_number):
  new_contact = Contact(fname, lname, email, phone_number)
  return new_contact

def save_contacts(contact):
  Contact.save_contact(contact)

def del_contacts(contact):
  Contact.delete_contact()

def find_contact(number):
  return Contact.find_by_number(number)

def check_existing_contacts(number):
  return Contact.contact_exist(number)

def display_contacts():
  return Contact.display_contacts()

def copies_email(string):
  return Contact.copy_email(string)

def main():
  print("Hello Welcome to your contact list. What is your name?")
  user_name = input()
  print(f"Hello {user_name}. What would you like to do?")
  print('\n')

  while True:
    print("Use these short codes : cc - create a new contact, dc - display contacts,\n"
     "fc -find a contact, ex -exit the contact list ")
    short_code = input().lower()
    
    if short_code == 'cc':
      print("New Contact")
      print("-" *10)

      print("First Name")
      f_name = input()
      print("Last Name")
      l_name = input()
      print("Email Address")
      e_mail = input()
      print("Telephone Number")
      phone = input()

      save_contacts(create_contact(f_name,l_name,e_mail,phone))

      print("\n")
      print(f"New Contact {f_name} {l_name} Created")
      print("\n")

    elif short_code == 'dc':
      if display_contacts():
        print("Here is a list of all your Contacts")
        print("\n")

        for contact in display_contacts():
          print(f"{contact.fname} {contact.lname} {contact.email} {contact.phone_number}")

          print("\n")

      else:
        print("\n")
        print("You have no saved contacts")
        print("\n")

    elif short_code == "fc":
      print("Enter the number you want to search for")
      search_number = input()
      if check_existing_contacts(search_number):
        search_contact = find_contact(search_number)
        print(f"{search_contact.fname} {search_contact.lname}")
        print("-" *20)

        print(f"Phone number ---- {search_contact.phone_number}")
        print(f"Phone number ---- {search_contact.email}")
        
      else:
        print("That contact does not exist")

    elif short_code == 'ex':
      print("Bye.......")
      break
    else:
      print("I really did not get that. Kindly use the short-codes")

if __name__ == '__main__':

    main()

