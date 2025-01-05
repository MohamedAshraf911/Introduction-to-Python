arr = input("Enter the numbers separated by space: ").split()

def calculate_average(numbers):
    return sum(numbers) / len(numbers)

arr = list(map(int, arr))
average = calculate_average(arr)

print("Average is:", average)