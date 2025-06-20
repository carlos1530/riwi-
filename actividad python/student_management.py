# Main dictionary to store students
students = {}

# Function to generate a unique ID automatically
def generate_id():
    return str(len(students) + 1)

# Function to register a student
def register_student():
    """Function to register a student with name, age, and grades."""
    try:
        student_id = generate_id()  # Generate a unique ID
        name = input("Enter the student's name: ")

        # Validate age
        age_valid = False
        while not age_valid:
            try:
                age = int(input("Enter the student's age: "))
                if 0 <= age <= 120:  # Validate that age is within a logical range
                    age_valid = True
                else:
                    print("Please enter a valid age between 0 and 120.")
            except ValueError:
                print("Error: Please enter a valid age.")

        # Register grades
        grades = []
        for i in range(3):
            grade_valid = False
            while not grade_valid:
                try:
                    grade = float(input(f"Enter grade {i+1}: "))
                    if 0 <= grade <= 10:  # Validate that the grade is between 0 and 10
                        grades.append(grade)
                        grade_valid = True
                    else:
                        print("Grade must be between 0 and 10. Try again.")
                except ValueError:
                    print("Error: Please enter a numerical value for the grade.")

        students[student_id] = {
            "name": name,
            "age": age,
            "grades": grades
        }

        print("Student registered successfully.")
    except Exception as e:
        print(f"Error: {e}")

# Function to query a student
def query_student():
    """Function to query the data of a student by their ID."""
    student_id = input("Enter the student's ID: ")
    if student_id in students:
        student = students[student_id]
        average = sum(student["grades"]) / len(student["grades"])
        print(f"\nName: {student['name']}")
        print(f"Age: {student['age']}")
        print(f"Grades: {student['grades']}")
        print(f"Average: {average:.2f}\n")
    else:
        print("Student not found.")

# Function to update grades
def update_grades():
    """Function to update the grades of a student."""
    student_id = input("Enter the student's ID whose grades you want to update: ")
    if student_id in students:
        print(f"\nStudent: {students[student_id]['name']}")
        
        option = None
        while option != "4":  # Exit when option "4" is selected
            print("\nOptions to update grades:")
            print("1. Add a new grade")
            print("2. Modify an existing grade")
            print("3. Remove a grade")
            print("4. Finish updating")

            option = input("Select an option: ")

            if option == "1":
                # Add a new grade
                grade_valid = False
                while not grade_valid:
                    try:
                        new_grade = float(input("Enter the new grade (0-10): "))
                        if 0 <= new_grade <= 10:
                            students[student_id]["grades"].append(new_grade)
                            print("Grade added successfully.")
                            grade_valid = True
                        else:
                            print("Grade must be between 0 and 10.")
                    except ValueError:
                        print("Please enter a numerical value.")
            
            elif option == "2":
                # Modify an existing grade
                index_valid = False
                while not index_valid:
                    try:
                        index = int(input(f"Enter the index of the grade to modify (0 to {len(students[student_id]['grades'])-1}): "))
                        if 0 <= index < len(students[student_id]["grades"]):
                            new_grade = float(input(f"Enter the new grade for index {index} (0-10): "))
                            if 0 <= new_grade <= 10:
                                students[student_id]["grades"][index] = new_grade
                                print("Grade modified successfully.")
                                index_valid = True
                            else:
                                print("Grade must be between 0 and 10.")
                        else:
                            print("Index out of range. Try again.")
                    except ValueError:
                        print("Please enter a valid index.")

            elif option == "3":
                # Remove a grade
                index_valid = False
                while not index_valid:
                    try:
                        index = int(input(f"Enter the index of the grade to remove (0 to {len(students[student_id]['grades'])-1}): "))
                        if 0 <= index < len(students[student_id]["grades"]):
                            del students[student_id]["grades"][index]
                            print("Grade removed successfully.")
                            index_valid = True
                        else:
                            print("Index out of range. Try again.")
                    except ValueError:
                        print("Please enter a valid index.")
            
            elif option == "4":
                print("Updating finished.")
            else:
                print("Invalid option. Try again.")
    else:
        print("Student not found.")

# Function to delete a student
def delete_student():
    """Function to delete a student by their ID."""
    student_id = input("Enter the student's ID you want to delete: ")
    if student_id in students:
        del students[student_id]
        print("Student deleted successfully.")
    else:
        print("Student not found.")

# Function to view all students
def view_all():
    """Function to display the list of all registered students."""
    if not students:
        print("No students registered.")
        return
    for student_id, data in students.items():
        average = sum(data["grades"]) / len(data["grades"])
        print(f"{data['name']} (ID: {student_id}) - Average: {average:.2f}")

# Main menu function
def menu():
    """Main menu to interact with the student management system."""
    continue_running = True
    while continue_running:
        print("\n----- Student Management -----")
        print("1. Register student")
        print("2. Query student")
        print("3. Update grades")
        print("4. Delete student")
        print("5. View all students")
        print("6. Exit")

        option = input("Select an option: ")

        if option == "1":
            register_student()
        elif option == "2":
            query_student()
        elif option == "3":
            update_grades()
        elif option == "4":
            delete_student()
        elif option == "5":
            view_all()
        elif option == "6":
            print("Goodbye!")
            continue_running = False  # Exit the loop
        else:
            print("Invalid option. Please try again.")

# Run the program
if __name__ == "__main__":
    menu()
