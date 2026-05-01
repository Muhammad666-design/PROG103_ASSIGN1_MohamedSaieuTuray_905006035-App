import json
import os
#this is the data_base file
FILE_NAME = "students.json"
#now I define the function below so it could be reusable

def load_students():

    if os.path.exists(FILE_NAME):

        with open(FILE_NAME, "r") as file:
            return json.load(file)

    return []

#this function save records
def save_students(students):

    with open(FILE_NAME, "w") as file:
        json.dump(students, file, indent=4)

# this line calls the function in line 7
students = load_students()

#this function calculates the grades
def calculate_grade(avg):

    if avg >= 80:
        return "A"

    elif avg >= 70:
        return "B"

    elif avg >= 60:
        return "C"

    elif avg >= 50:
        return "D"

    else:
        return "F"

#this statement adds records
def add_student():

    print("\n===== ADD STUDENT =====")

    name = input("Enter student name: ")

    math = float(input("Enter Math score: "))
    science = float(input("Enter Science score: "))
    english = float(input("Enter English score: "))

    average = (math + science + english) / 3

    grade = calculate_grade(average)

    student = {
        "name": name,
        "math": math,
        "science": science,
        "english": english,
        "average": round(average, 2),
        "grade": grade
    }

    students.append(student)

    save_students(students)

    print("\nStudent added successfully!")
    print(f"Average Score: {average:.2f}")
    print(f"Grade: {grade}")
#this function displays the existing student records

def display_students():

    print("\n===== STUDENT RECORDS =====")

    if len(students) == 0:
        print("No student records found.")
        return

    for student in students:

        print("--------------------------------")

        print(f"Name     : {student['name']}")
        print(f"Math     : {student['math']}")
        print(f"Science  : {student['science']}")
        print(f"English  : {student['english']}")
        print(f"Average  : {student['average']}")
        print(f"Grade    : {student['grade']}")

        print("--------------------------------")

#this statement searches for existing records
def search_student():

    print("\n===== SEARCH STUDENT =====")

    search_name = input("Enter student name: ")

    found = False

    for student in students:

        if student["name"].lower() == search_name.lower():

            print("\nStudent Found!")

            print("--------------------------------")

            print(f"Name     : {student['name']}")
            print(f"Math     : {student['math']}")
            print(f"Science  : {student['science']}")
            print(f"English  : {student['english']}")
            print(f"Average  : {student['average']}")
            print(f"Grade    : {student['grade']}")

            print("--------------------------------")

            found = True

    if not found:
        print("Student not found.")

#this statement deletes records
def delete_student():

    print("\n===== DELETE STUDENT =====")

    name = input("Enter student name to delete: ")

    for student in students:

        if student["name"].lower() == name.lower():

            students.remove(student)

            save_students(students)

            print("Student deleted successfully.")
            return
# this statement tells the user the wanted record is not in the system
    print("Student not found.")


def menu():

    while True:

        print("""

========================================
 STUDENT RECORD MANAGEMENT SYSTEM
========================================

1. Add Student
2. Display Students
3. Search Student
4. Delete Student
5. Exit

========================================
""")
#the user should input a choice to continue
        choice = input("Enter your choice: ")

        if choice == "1":
            add_student()

        elif choice == "2":
            display_students()

        elif choice == "3":
            search_student()

        elif choice == "4":
            delete_student()

        elif choice == "5":

            print("\nExiting program...")
            break

        else:
            print("\nInvalid choice. Try again.")


menu()