# Student Management System

students = []

while True:
    print("\n===== Student Management System =====")
    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Delete Student")
    print("5. Exit")

    choice = input("Enter your choice: ")

    # Add Student
    if choice == "1":
        name = input("Enter student name: ")
        roll = input("Enter roll number: ")

        student = {
            "name": name,
            "roll": roll
        }

        students.append(student)

        # Save student data to file
        with open("students.txt", "a") as file:
            file.write(f"Name: {name}, Roll: {roll}\n")

        print("Student Added Successfully")

    # View Students
    elif choice == "2":
        if len(students) == 0:
            print("No student records found")

        else:
            print("\n--- Student Records ---")

            for student in students:
                print(f"Name: {student['name']}")
                print(f"Roll: {student['roll']}")
                print("----------------------")

    # Search Student
    elif choice == "3":
        roll = input("Enter roll number to search: ")

        found = False

        for student in students:
            if student["roll"] == roll:
                print("\nStudent Found")
                print(f"Name: {student['name']}")
                print(f"Roll: {student['roll']}")

                found = True
                break

        if not found:
            print("Student Not Found")

    # Delete Student
    elif choice == "4":
        roll = input("Enter roll number to delete: ")

        found = False

        for student in students:
            if student["roll"] == roll:
                students.remove(student)

                print("Student Deleted Successfully")

                found = True
                break

        if not found:
            print("Student Not Found")

    # Exit Program
    elif choice == "5":
        print("Exiting Program...")
        break

    else:
        print("Invalid Choice")
