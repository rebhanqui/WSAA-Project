from contactsDAO import ContactsDAO

def main():
    #instance creation
    contactsDAO = ContactsDAO()
    
    #get all contacts
    allContacts = contactsDAO.getAll()
    for contacts in allContacts:
        print(contacts)
        
    #create contact
    #user input
    firstName = input("Enter first name: ")
    lastName = input("Enter last name: ")
    department = input("Enter department: ")
    telNum = int(input("Enter telephone number: "))
    
    #get maximum cid from the database
    maxCid = contactsDAO.getMaxCID()

    #increment the maximum cid by 1 rather than id done by user input
    newCid = maxCid + 1

    #new contact using the user input
    newContactValues = (newCid, firstName, lastName, department, telNum)
    contactsDAO.create(newContactValues)

    print(f"New contact created with ID: {newCid}")

    #find by CID
    cidSearch = int(input("Enter contact ID: "))
    contact = contactsDAO.findByCID(cidSearch)

    if contact:
        print("Contact found:")
        print(contact)
    else:
        print(f"No contact found with cid {cidSearch}")
        
    #update contact
    updateContactID = int(input("Enter contact ID to update: "))
    
    #search contact by CID
    contactToUpdate = contactsDAO.findByCID(updateContactID)
    
    if contactToUpdate:
        print(f"Contact found: {contactToUpdate}")
        
        #new details by user input
        firstName = input("Enter updated first name: ")
        lastName = input("Enter updated last name: ")
        department = input("Enter updated department: ")
        telNum = int(input("Enter updated telephone number: "))
        
        #update with new details
        updatedValues = (firstName, lastName, department, telNum, updateContactID)
        contactsDAO.update(updatedValues)
        
        print("Contact updated successfully.")
    else:
        print(f"No contact found with CID {updateContactID}")
        
    #delete contact
    deleteContact = int(input("Enter contact ID to delete: "))
    
    #search contact based on CID
    contactToDelete = contactsDAO.findByCID(deleteContact)
    
    if contactToDelete:
        print(contacts)
        print("Contact found:")
        print(contactToDelete)
        
        #confirm delete
        confirmation = input("Are you sure you want to delete this contact? (yes/no): ").lower()
        if confirmation == "yes":
            #delete from db
            contactsDAO.delete(deleteContact)
            print("Contact deleted successfully.")
        else:
            print("Deletion canceled.")
    else:
        print(f"No contact found with CID {deleteContact}")
        

if __name__ == "__main__":
    main()
