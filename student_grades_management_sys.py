# creating empty dictionary
student_grade = {}

# creating function to add student and grade
def add_student(name, grade):
    student_grade[name] = grade
    # message to show that student is added successfully 
    print(f"Added {name} with {grade}")

# creating function to update student and grade
def update_student(name, grade):
    if name in student_grade:
        student_grade[name] = grade
        # message to show that student is updated successfully
        print(f"{name} with marks are updated {grade}")
    else:
        print(f"{name} is not found ")

# creating function to delete student and grade
def delete_student(name):
    if name in student_grade:
        del student_grade[name]
        # message to show that student is deleted successfully
        print(f"{name} has been successfully deleted")
    else:
        print(f"{name} is not found")
    
# creating function to display all students and grades
def display_all_students():
    if student_grade:
        for name, grade in student_grade.items():
            # message to show all students and grades
            print(f"{name} : {grade}")
    else:
        print("No students found/added ")

# creating main function to run the program
def main():
    # running the program in infinite loop until user chooses to exit
    while True:
        print("\n Student Grades Management system")
        print("1. Add student")
        print("2. Update student")
        print("3. delete student")
        print("4. view Student")
        print("5. Exit")
        
        # taking user input for choice 
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

main()

