count = input("Enter the number for fibonacci calculation: ")
while count.isdigit() != True:
    print("Please enter a valid number")
    count = input("Enter the number for fibonacci calculation: ")

def fibonacci(n):
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    else:
        seq = fibonacci(n - 1)
        seq.append(seq[-1] + seq[-2])
        return seq

count = int(count)
fib_sequence = fibonacci(count)
print(f"Fibonacci sequence up to {count} numbers is: {fib_sequence}")