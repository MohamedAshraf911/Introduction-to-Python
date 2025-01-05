start_year =input("Enter your birth year: ")
if not start_year.isdigit():
    print("Please enter a valid year")
    exit()
end_year = input("Enter the year you want to calculate your age: ")
if not end_year.isdigit():
    print("Please enter a valid year")
    exit()
if int(start_year) > int(end_year):
    print("Please enter a valid year")
    exit()
age = int(end_year) - int(start_year)
print(f"Your age is {age} years old")