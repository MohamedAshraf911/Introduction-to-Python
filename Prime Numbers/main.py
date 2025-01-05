n = input("Enter the number: ")
while n.isdigit() != True:
    print("Please enter a valid number")
    n = input("Enter the number: ")

while int(n) < 2:
    print("Please enter a number greater than 2")
    n = input("Enter the number: ")

#print all the prime numbers between 2 and a number (N) given by the user
for i in range(2, int(n)+1):
    prime = True
    for j in range(2, i):
        if i % j == 0:
            prime = False
            break
    if prime:
        print(i)