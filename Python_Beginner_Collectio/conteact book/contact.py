contacts = {}

while True:
    print('\n contact book app')
    print('1. create contact')
    print('2. view contact')
    print('3. update contact')
    print('4. Delete contact')
    print('5. search contact')
    print('6. count contact')
    print('7. exit')    

    choice = input('Enter your choice:')

    if choice == '1':
        name = input('Enter contact name:')
        if name in contacts:
            print(f'contact with name {name} already exists.')
        else:
            age = int(input('Enter age: '))
            email = input('Enter email: ')
            phone = input('Enter phone number: ')
            contacts[name] = {'age': age, 'email': email, 'phone': phone}
            print(f'contact {name} created successfully.')
    
    elif choice == '2':
        name = input('Enter contact name to view:')
        if name in contacts:
            contact = contacts[name]
            print(f'Name: {name}')
            print(f'Age: {contact["age"]}')
            print(f'Email: {contact["email"]}')
            print(f'phone: {contact["phone"]}')
        else:
            print(f'contact with name {name} does not exist.')

    elif choice == '3':
        name = input('Enter contact name to update:')
        if name in contacts:
            age = input('Enter new age: ')
            email = input('Enter new email: ')
            phone = input('Enter new phone number: ')
            contacts[name] = {'age': age, 'email': email, 'phone': phone}
            print(f'contact {name} updated successfully.')
        else:
            print(f'contact with name {name}does not exist.')

    elif choice == '4':
        name = input('Enter contact name to delete:')
        if name in contacts:
            del contacts[name]
            print(f'contact {name} deleted successfully.')
        else:
            print(f'contact with name {name} does not exist.')
        
    elif choice == '5':
        search_name = input('Enter contact name to search:')
        found = False
        for name,contact in contacts.items():
            if search_name.lower() in name.lower():
                print(f'Found - \nName {name}, \nAge: {contact["age"]}, \nEmail: {contact["email"]}, \nPhone: {contact["phone"]}')
                found = True
        if not found:
            print(f'contact with name {search_name} not found.')

    elif choice == '6':
        count = len(contacts)
        print(f'Total contacts: {count}')
    
    elif choice == '7':
        print('Exiting the contact book app.')
        break

    else:
        print('Invalid choice. please try again.')