arr = input("Enter the numbers separated by space: ").split()

if not arr:
    print("No numbers provided")
    exit()

while not all(num.isdigit() for num in arr):
    print("Please enter valid numbers")
    arr = input("Enter the numbers separated by space: ").split()

def calculate_average(numbers):
    return sum(numbers) / len(numbers)

arr = list(map(int, arr))
average = calculate_average(arr)

print("Average is:", average)