import os
def read_grades(file_path):
    grades = {}
    if os.path.exists(file_path):
        try:
            with open(file_path, 'r') as file:
                for line in file:
                    subject, grade = line.strip().split(',')
                    grades[subject] = float(grade)
        except (IOError, ValueError) as e:
            print(f"Error reading file: {e}")
    return grades

def write_grades(file_path, grades):
    try:
        with open(file_path, 'w') as file:
            for subject, grade in grades.items():
                file.write(f"{subject},{grade}\n")
    except IOError as e:
        print(f"Error writing to file: {e}")

def calculate_average(grades):
    if not grades:
        return 0
    return sum(grades.values()) / len(grades)

def main():
    file_path = 'grades.txt'
    grades = read_grades(file_path)
    
    while True:
        print("\n1. Add/Update Grade")
        print("2. Calculate Average Grade")
        print("3. Exit")
        choice = input("Enter your choice: ")
        
        if choice == '1':
            subject = input("Enter subject: ")
            try:
                grade = float(input("Enter grade: "))
                while grade < 0 or grade > 100:
                    print("Invalid grade. Grade must be between 0 and 100.")
                    grade = float(input("Enter grade: "))
                grades[subject] = grade
                write_grades(file_path, grades)
            except ValueError:
                print("Invalid grade. Please enter a number.")
        elif choice == '2':
            average = calculate_average(grades)
            print(f"Average Grade: {average:.2f}")
        elif choice == '3':
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
