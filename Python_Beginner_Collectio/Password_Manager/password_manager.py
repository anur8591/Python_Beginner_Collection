import random
import string

password = {}

try:
    with open("passwords.txt", "r") as file:
        for line in file:
            website, passw = line.strip().split(":")
            password[website] = passw
except Exception as e:
    print(f"the error is : {e}")

def generate_password():
    chars = string.ascii_letters + string.digits + "!@#$%&"
    password = "".join(random.choice(chars) for _ in range(8))
    return password

while True:
    print("\n-----PERSONAL PASSWORD MANAGER------")
    print("1. Save Password")   
    print("2. View Password")
    print("3. Generate Password")
    print("4. Exit")

    choice = int(input("Enter your choice : "))

    if choice == 1:
        site = input("enter website : ")
        passw = input("enter password : ")

        password[site] = passw

        with open("passwords.txt", "a") as file:
            file.write(f"{site}:{passw}\n")
        
        print("Saved!")

    elif choice == 2:
        if not password:
            print("No data")
        else:
            for site, passw in password.items():
                print(site, ":", passw)

    elif choice == 3:
        print("Generated Password : ", generate_password())

    elif choice == 4:
        print("Ok bye..")
        break

    else:
        print("In-valid input")
