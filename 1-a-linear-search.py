import time
import random
import matplotlib.pyplot as plt

def linear_search(arr, key):
    """Search for key in arr and return index if found, else -1."""  # not necessary
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

    start_time = time.time()
    linear_search(arr, key)
    end_time = time.time()

    times.append(end_time - start_time)

# Plot the results
plt.plot(sizes, times, marker='o', linestyle='-', color='b')
plt.xlabel("Number of Elements (n)")
plt.ylabel("Time Taken (seconds)")
plt.title("Linear Search: Time vs Number of Elements")
plt.grid()
plt.show()
