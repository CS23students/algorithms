import time
import random
import matplotlib.pyplot as plt

def linear_search(arr, key):
    """Search for key in arr and return index if found, else -1."""
    for i in range(len(arr)):
        if arr[i] == key:
            return i
    return -1

# List of different sizes for testing
sizes = [1000, 5000, 10000, 20000, 50000, 100000]
times = []

for n in sizes:
    arr = [random.randint(1, 1000000) for _ in range(n)]  # Generate n random numbers
    key = random.choice(arr)  # Choose a random element to search (best case)

    start_time = time.time() # perf_counter() can also be used to show time(ms)
    position = linear_search(arr, key)
    end_time = time.time()

    time_taken = end_time - start_time
    times.append(time_taken)

    # Print search result
    if position != -1:
        print(f"Search element found at position: {position + 1}")  # Convert to 1-based index
    else:
        print("Search element not found.")
    
    print(f"Time taken to search: {time_taken:.6f} seconds\n")

# Plot the results
plt.plot(sizes, times, marker='o', linestyle='-', color='b')
plt.xlabel("Number of Elements (n)")
plt.ylabel("Time Taken (seconds)")
plt.title("Linear Search: Time vs Number of Elements")
plt.grid()
plt.show()
