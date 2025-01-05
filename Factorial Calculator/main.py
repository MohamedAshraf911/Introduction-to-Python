n = input("Enter the number for factorial calculation: ")
while n.isdigit() != True:
    print("Please enter a valid number")
    n = input("Enter the number for factorial calculation: ")

if int(n) == 0:
    print(1)
else:
    fact = 1
    for i in range(1, int(n) + 1):
        fact *= i
    print(fact)

