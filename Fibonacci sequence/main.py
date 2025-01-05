n = input("Enter the number for fibonacci sequence: ")
a = 0
b = 1

while n.isdigit() != True:
    print("Please enter a valid number")
    n = input("Enter the number for fibonacci sequence: ")

if int(n) == 1:
    print(a)
else:
    print(a)
    print(b)
    for i in range(2, int(n)):
        c = a + b
        a = b
        b = c
        print(c)