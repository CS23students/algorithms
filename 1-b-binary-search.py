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
    position = binary_search(arr, key, 0, len(arr) - 1)
    end_time = time.perf_counter()  

    time_taken = end_time - start_time  # Time in seconds
    times.append(time_taken)

    # Print search result
    if position != -1:
        print(f"Search element found at position: {position + 1}")  # Convert to 1-based index
    else:
        print("Search element not found.")
    
    print(f"Time taken to search: {time_taken:.6f} seconds\n")

# Plot graph
plt.plot(sizes, times, marker='o', linestyle='-', color='r')
plt.xlabel("Number of Elements (n)")
plt.ylabel("Time Taken (seconds)")
plt.title("Recursive Binary Search: Time vs Number of Elements")
plt.grid()
plt.show()
