import time
import random
import matplotlib.pyplot as plt

def binary_search(arr, key, low, high):
    """Recursive Binary Search function"""
    if low > high:
        return -1  # Element not found
    mid = (low + high) // 2
    if arr[mid] == key:
        return mid
    elif arr[mid] > key:
        return binary_search(arr, key, low, mid - 1)
    else:
        return binary_search(arr, key, mid + 1, high)

# List sizes for testing
sizes = [1000, 5000, 10000, 50000, 100000, 500000, 1000000]
times = []

for n in sizes:
    arr = sorted(random.sample(range(1, 10000000), n))  # Generate a sorted list of n unique random numbers
    key = random.choice(arr)  # Pick a random element to search

    start_time = time.perf_counter()  # High-precision timer
    binary_search(arr, key, 0, len(arr) - 1)
    end_time = time.perf_counter()  

    times.append((end_time - start_time) * 1e6)  # Convert to microseconds

# Plot graph
plt.plot(sizes, times, marker='o', linestyle='-', color='r')
plt.xlabel("Number of Elements (n)")
plt.ylabel("Time Taken (µs) (Microseconds)")
plt.title("Recursive Binary Search: Time vs Number of Elements")
plt.grid()
plt.show()
