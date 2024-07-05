contact = {}

def display_contact():
    if not contact:
        print("Contact list is empty")
    else:
        print("Name \tContact Number \tEmail Address \tAddress")
        for key in contact:
            print ("{}\t{}".format(key, contact.get(key)))

while True:
    choice = int(input("1. Add new contact \n 2.Search contact \n 3.Display contact \n 4.Edit contact \n 5.Delete contact \n 6.EXIT\nEnter_your_choice>>"))
    if choice == 1:
        name = input("Enter the contact name>>")
        phone = input("Enter the phone number>>")
        email = input("Enter the email address>>")
        address = input("Enter the address>>")
        print("New Contact Created")
        contact[name] = phone + "   " + email + "   " + address
    elif choice == 2:
        search_name = input("Enter the contact name>>")
        if search_name in contact:
            print(search_name, "'s Contact Detail's:>>", contact[search_name])
        else:
            print("Entered contact name is not in contact list")
    elif choice == 3:
        display_contact()
    elif choice == 4:
        edit_contact = input("Enter the contact to be edited>>")
        if edit_contact in contact:
            name = input("Enter the contact name>>")
            phone = input("Enter the phone number>>")
            email = input("Enter the email address>>")
            address = input("Enter the address>>")
            contact[edit_contact] = phone + " " + email + " " + address
            print("Contact updated")
            display_contact()
        else:
            print("Name is not found in contact list")
    elif choice == 5:
        delete_contact = input("Enter the contact to be deleted>>")
        if delete_contact in contact:
            confirm = input("Are you sure you want to delete (y/n)>> ")
            if confirm.lower() == 'y':
                contact.pop(delete_contact)
                print("Contact deleted")
                display_contact()
            else:
                print("Deletion cancelled")
        else:
            print("Name is not found in contacts")
    elif choice == 6:
        break
    else:
        print("Invalid choice. Please choose a valid option.")