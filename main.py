from database import (
    create_table,
    add_student,
    view_students,
    search_student,
    update_student,
    delete_student
)


def get_non_empty(prompt):
    while True:
        value = input(prompt).strip()

        if value:
            return value

        print("This field cannot be empty. Please try again.")


def get_marks(prompt):
    while True:
        try:
            marks = float(input(prompt))

            if 0 <= marks <= 100:
                return marks

            print("Marks must be between 0 and 100.")

        except ValueError:
            print("Please enter a valid number.")


def main():
    create_table()

    while True:
        print("\n================================")
        print("     STUDENT MANAGEMENT SYSTEM")
        print("================================")
        print("1. Add Student")
        print("2. View Students")
        print("3. Search Student")
        print("4. Update Student")
        print("5. Delete Student")
        print("6. Exit")

        choice = input("\nEnter your choice: ").strip()

        if choice == "1":
            print("\n--- Add Student ---")

            roll_no = get_non_empty("Enter Roll Number: ")
            name = get_non_empty("Enter Name: ")
            course = get_non_empty("Enter Course: ")
            marks = get_marks("Enter Marks: ")
            email = input("Enter Email (optional): ").strip()

            add_student(roll_no, name, course, marks, email)

        elif choice == "2":
            print("\n--- Student Records ---")

            students = view_students()

            if not students:
                print("No student records found.")
            else:
                print("-" * 75)
                print(
                    f"{'ID':<5}{'Roll No':<12}{'Name':<15}"
                    f"{'Course':<12}{'Marks':<10}{'Email'}"
                )
                print("-" * 75)

                for student in students:
                    print(
                        f"{student[0]:<5}{student[1]:<12}{student[2]:<15}"
                        f"{student[3]:<12}{student[4]:<10}{student[5]}"
                    )

                print("-" * 75)

        elif choice == "3":
            print("\n--- Search Student ---")

            roll_no = get_non_empty(
                "Enter Roll Number to search: "
            )

            student = search_student(roll_no)

            if student:
                print("\nStudent Found!")
                print("-" * 40)
                print(f"ID       : {student[0]}")
                print(f"Roll No  : {student[1]}")
                print(f"Name     : {student[2]}")
                print(f"Course   : {student[3]}")
                print(f"Marks    : {student[4]}")
                print(f"Email    : {student[5]}")
                print("-" * 40)
            else:
                print("\nStudent not found.")

        elif choice == "4":
            print("\n--- Update Student ---")

            roll_no = get_non_empty(
                "Enter Roll Number to update: "
            )
            name = get_non_empty("Enter New Name: ")
            course = get_non_empty("Enter New Course: ")
            marks = get_marks("Enter New Marks: ")
            email = input("Enter New Email (optional): ").strip()

            update_student(
                roll_no,
                name,
                course,
                marks,
                email
            )

        elif choice == "5":
            print("\n--- Delete Student ---")

            roll_no = get_non_empty(
                "Enter Roll Number to delete: "
            )

            student = search_student(roll_no)

            if student:
                print(f"\nStudent: {student[2]}")
                confirmation = input(
                    "Are you sure you want to delete this student? (y/n): "
                ).strip().lower()

                if confirmation == "y":
                    delete_student(roll_no)
                else:
                    print("\nDelete operation cancelled.")
            else:
                print("\nStudent not found.")

        elif choice == "6":
            print("\nThank you for using Student Management System!")
            break

        else:
            print("\nInvalid choice. Please try again.")


if __name__ == "__main__":
    main()