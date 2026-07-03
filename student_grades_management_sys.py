student_grade = {}

def add_student(name, grade):
    student_grade[name] = grade

    print(f"Added {name} with {grade}")


def update_student(name, grade):
    if name in student_grade:
        student_grade[name] = grade
        print(f"{name} with marks are updated {grade}")
    else:
        print(f"{name} is not found ")


def delete_student(name):
    if name in student_grade:
        del student_grade[name]
        print(f"{name} has been successfully deleted")
    else:
        print(f"{name} is not found")
    

def display_all_students():
    if student_grade:
        for name, grade in student_grade.items():
            print(f"{name} : {grade}")
    else:
        print("No students found/added ")

def main():
    while True:
        print("\n Student Grades Management system")
        print("1. Add student")
        print("2. Update student")
        print("3. delete student")
        print("4. view Student")
        print("5. Exit")

        choice = int(input("Enter your choice = "))
        if choice == 1:
            name = input("Enter student name = ")
            grade = int(input("Enter student grade = "))
            add_student(name, grade)
        elif choice == 2:
            name = input("Enter student namee = ")
            grade = int(input("Enter student grade = "))
            update_student(name, grade)
        elif choice == 3:
            name = input("Enter student name = ")
            delete_student(name)
        elif choice == 4:
            display_all_students()
        elif choice == 5:
            print("closing the program.....")
            break
        else:
            print("Invalid choice, please try again...")



