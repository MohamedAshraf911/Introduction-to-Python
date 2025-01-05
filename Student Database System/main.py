class Student:
    def __init__(self, name, age, grades):
        self.name = name
        self.age = age
        self.grades = grades

    def display_info(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Grades: {self.grades}")

    def calculate_average_grade(self):
        if len(self.grades) == 0:
            return 0
        return sum(self.grades) / len(self.grades)

# Example usage
students = [
    Student("Alice", 20, [85, 90, 78]),
    Student("Bob", 22, [88, 76, 92]),
    Student("Charlie", 19, [90, 85, 85])
]

for student in students:
    student.display_info()
    print(f"Average Grade: {student.calculate_average_grade():.2f}")
    print()