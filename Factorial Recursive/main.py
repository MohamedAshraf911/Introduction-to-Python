n = input("Enter the number for factorial calculation: ")
while n.isdigit() != True:
    print("Please enter a valid number")
    n = input("Enter the number for factorial calculation: ")

def factorial(n):
    if n == 1:
        return n
    else:
        return n * factorial(n - 1)

if int(n) == 0:
    print(1)
else:
    print("The factorial of", n, "is", factorial(int(n)))  

