students = []

while True:
    print("\n===== STUDENT MANAGEMENT SYSTEM =====")
    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        name = input("Enter student name: ")
        age = int(input("Enter age: "))
        mark = int(input("Enter mark: "))

        student = {
            "name": name,
            "age": age,
            "mark": mark
        }

        students.append(student)
        print("Student added successfully!")

    elif choice == "2":
        if len(students) == 0:
            print("No student records found.")
        else:
            for student in students:
                print(student)

    elif choice == "3":
        search_name = input("Enter student name: ")
        found = False

        for student in students:
            if student["name"].lower() == search_name.lower():
                print("Student found:", student)
                found = True

        if found == False:
            print("Student not found.")

    elif choice == "4":
        print("Thank you!")
        break

    else:
        print("Invalid choice. Try again.")
