import os 

def create_file(file_name):
    try:
        with open(file_name, 'x') as f:
            print(f"File created: {file_name}")
    except FileExistsError:
        print(f"File already exists: {file_name}")
    except Exception as e:
        print("An error occurred while creating the file:", e)

def view_all_files():
    files = os.listdir()
    if not files:
        print("No files found in the current directory.")
    else:
        print("files in the current directory:")
        for file in files:
            print(file)

def delete_file(file_name):
    try:
        os.remove(file_name)
        print(f"{file_name} has been deleted.")
    except FileNotFoundError:
        print(f'{file_name} not found.')
    except Exception as e:
        print("An error occurred while deleting the file:", e)

def read_file(file_name):
    try:
        with open("temp.txt", 'r') as f:
            content = f.read()
            print(f"content of '{file_name}' :\n{content}")
    except FileNotFoundError:
        print(f"{file_name} does not exist.")
    except Exception as e:
        print("An error occurred while reading the file:", e)

def edit_file(file_name):
    try:
        with open('temp.txt', 'a') as f:
            content = input("Enter the content to append to the file:")
            f.write(content + '\n')
            print(f'content added to the {file_name} successfully')
    except FileNotFoundError:
        print(f"{file_name} doesn't exist.")
    except Exception as e:
        print("An error occurred while editing the file:", e)

def main():
    while True:
        print("\nFile Management system ")
        print("1. create a file")
        print("2. view all files")
        print("3. delete a file")
        print("4. read a file")
        print("5. edit a file")
        print("6. exit")
        choice = input("Enter your choice: ")
        if choice == '1':
            file_name = input("Enter the name of the file to create: ")
            create_file(file_name)
        elif choice == '2':
            view_all_files()
        elif choice == '3':
            file_name = input("Enter the name of the file to delete: ")
            delete_file(file_name)
        elif choice == '4':
            file_name = input("Enter the name of the file to read: ")
            read_file(file_name)
        elif choice == '5':
            file_name = input("Enter the name of the file to edit: ")
            edit_file(file_name)
        elif choice == '6':
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()