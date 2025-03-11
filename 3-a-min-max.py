def find_max_min(arr, low, high):
    # If only one element
    if low == high:
        return arr[low], arr[low]

    # If two elements
    elif high == low + 1:
        if arr[low] > arr[high]:
            return arr[low], arr[high]
        else:
            return arr[high], arr[low]

    else:
        # Divide the array
        mid = (low + high) // 2
        max1, min1 = find_max_min(arr, low, mid)
        max2, min2 = find_max_min(arr, mid + 1, high)

        # Combine the results
        maximum = max(max1, max2)
        minimum = min(min1, min2)

        return maximum, minimum

# Main program
n = int(input("Enter the number of elements: "))
arr = list(map(int, input("Enter the elements: ").split()))

maximum, minimum = find_max_min(arr, 0, n - 1)

print("\nMaximum element:", maximum)
print("Minimum element:", minimum)


# OP:
# Enter the number of elements: 6
# Enter the elements: 5 12 7 9 3 15
# Maximum element: 15
# Minimum element: 3

