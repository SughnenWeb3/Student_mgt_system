students_db = {}

def add_student():
    print("--- Add Student ---")
    name = input("Student name: ")
    age = int(input("Enter age: "))
    dept = input("Department: ")
    key = len(students_db) + 1
    students_db[key] = {"name": name, "dept": dept, "age": age}
    print(f"Student added with ID: {key}")

def delete_student():
    print("--- Delete Student ---")
    student_id = int(input("Enter student ID to delete: "))
    if student_id in students_db:
        del students_db[student_id]
        print(f"Student with ID {student_id} deleted successfully")
    else:
        print("Student not found")

def update_student():
    print("Update Student ")
    student_id = int(input("Enter student ID to update: "))
    if student_id in students_db:
        print(f"Current info: {students_db[student_id]}")
        print("1. Update name")
        print("2. Update department")
        print("3. Update age")
        update = int(input("What would you like to update? "))
        if update == 1:
            student_new_name = input("Enter new name: ")
            students_db[student_id]["name"] = student_new_name
            print("Name updated successfully")
        elif update == 2:
            student_new_dept = input("Enter new department: ")
            students_db[student_id]["dept"] = student_new_dept
            print("Department updated successfully")
        elif update == 3:
            student_new_age = int(input("Enter new age: "))
            students_db[student_id]["age"] = student_new_age
            print("Age updated successfully")
        else:
            print("Invalid choice")
        print(f"Updated info: {students_db[student_id]}")
    else:
        print("Student not found")

def get_student():
    student_id = int(input("Enter student ID: "))
    if student_id in students_db:
        print("Student info:", students_db[student_id])
    else:
        print("Student not found")


def display_all():
    if students_db:
        for student in students_db:
             print("ID", student, ":", students_db[student])
    else:
        print("No students found")
def search_student_by_name():
    name = input("Enter name to search: ")
    for student in students_db:
        if students_db[sid]["name"] == name:
            print(student, students_db[student])
def total_students():
    print("Total students:", len(students_db))
def filter_by_age():
    age = input("Enter age to filter: ")
    for student in students_db:
        if students_db[student]["age"] == age:
            print(student, students_db[student])
def start():
    while True:
        print("--- Student Management System ---")
        print("""
        1. Add student
        2. Delete student
        3. Update student record
        4. Get a particular student
        5. Display all students
        6. Search student by name
        7. Count of all available students
        8. Get student by age
        """)
        user_choice = int(input("Choice: "))
        if user_choice == 1:
            add_student()
        elif user_choice == 2:
            delete_student()
        elif user_choice == 3:
            update_student()
        elif user_choice == 4:
            get_student()
        elif user_choice == 5:
            display_all()
        elif user_choice == 6:
            search_student_by_name()
        elif user_choice == 7:
            total_students()
        elif user_choice == 8:
            filter_by_age()
        else:
            print("Invalid choice")

start()

