arr = [64, 34, 25, 12, 22, 11, 90]
n = len(arr)
swap = False
for i in range(n):
    for j in range(0, n-i-1):
        if arr[j] > arr[j+1]:
            arr[j], arr[j+1] = arr[j+1], arr[j]
            swap = True
    if swap == False:
        break

print("Sorted array is:", arr)