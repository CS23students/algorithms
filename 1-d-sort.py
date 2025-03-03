import time
import random
import matplotlib.pyplot as plt
import heapq

def insertion_sort(arr):
    """Sorts an array using Insertion Sort."""
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

def heap_sort(arr):
    """Sorts an array using Heap Sort."""
    heapq.heapify(arr)  # Convert list into a heap
    sorted_arr = [heapq.heappop(arr) for _ in range(len(arr))]  # Extract min elements one by one
    arr[:] = sorted_arr  # Copy back sorted elements

# List sizes for testing
sizes = [1000, 5000, 10000, 20000, 30000]
insertion_times = []
heap_times = []

for n in sizes:
    arr = [random.randint(1, 1000000) for _ in range(n)]  # Generate random list
    arr_copy = arr[:]  # Copy list for fair comparison

    # Measure time for Insertion Sort
    start = time.perf_counter()  # High precision timer
    insertion_sort(arr)
    end = time.perf_counter()
    insertion_times.append((end - start) * 1e6)  # Convert to microseconds

    # Measure time for Heap Sort
    start = time.perf_counter()
    heap_sort(arr_copy)
    end = time.perf_counter()
    heap_times.append((end - start) * 1e6)  # Convert to microseconds

# Plot the graph
plt.plot(sizes, insertion_times, marker='o', linestyle='-', color='r', label="Insertion Sort")
plt.plot(sizes, heap_times, marker='o', linestyle='-', color='b', label="Heap Sort")
plt.xlabel("Number of Elements (n)")
plt.ylabel("Time Taken (µs) (Microseconds)")
plt.title("Insertion Sort vs Heap Sort: Time vs Number of Elements")
plt.legend()
plt.grid()
plt.show()
