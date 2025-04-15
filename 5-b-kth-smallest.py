import random

def partition(arr, low, high):
    pivot_index = random.randint(low, high)
    arr[pivot_index], arr[high] = arr[high], arr[pivot_index]
    pivot = arr[high]
    i = low - 1
    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1

def quickselect(arr, low, high, k):
    if low == high:
        return arr[low]

    pivot_index = partition(arr, low, high)
    if k == pivot_index:
        return arr[k]
    elif k < pivot_index:
        return quickselect(arr, low, pivot_index - 1, k)
    else:
        return quickselect(arr, pivot_index + 1, high, k)

def kth_smallest(arr, k):
    return quickselect(arr, 0, len(arr) - 1, k - 1)

# Input handling
n = int(input("Enter the size of the array: "))
arr = list(map(int, input("Enter the elements of the array: ").split()))
k = int(input("Enter the value of k: "))

print(f"{k}th smallest element is", kth_smallest(arr, k))


# Enter the size of the array: 8
# Enter the elements of the array: 12 3 5 7 19 1 2 8
# Enter the value of k: 4
# 4th smallest element is 5
