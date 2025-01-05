first_number = input("Enter the first number: ")

if not first_number.isdigit():
    print("Please enter a valid number")
    exit()
second_number = input("Enter the second number: ")

if not second_number.isdigit():
    print("Please enter a valid number")
    exit()

sum = int(first_number) + int(second_number)
subtraction = int(first_number) - int(second_number)
multiplication = int(first_number) * int(second_number)
print(f"Sum: {sum}")
print(f"Subtraction: {subtraction}")
print(f"Multiplication: {multiplication}")

if int(second_number) == 0:
    print("Division by zero is not allowed")
else:
    division = int(first_number) / int(second_number)
    print(f"Division: {division}")
