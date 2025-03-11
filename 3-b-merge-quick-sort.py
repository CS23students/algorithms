import time
import random
import matplotlib.pyplot as plt

# -----------------------------
# Merge Sort Function
def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        L = arr[:mid]
        R = arr[mid:]
        merge_sort(L)
        merge_sort(R)
        i = j = k = 0
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1
        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1
        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1

# -----------------------------
# Quick Sort Function
def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[0]
        less = [x for x in arr[1:] if x <= pivot]
        greater = [x for x in arr[1:] if x > pivot]
        return quick_sort(less) + [pivot] + quick_sort(greater)

# -----------------------------
# Arrays to store results for plotting
n_values = []
merge_sort_times = []
quick_sort_times = []

# -----------------------------
# Main processing for different n
for n in range(1000, 6001, 1000):  # n = 1000 to 6000
    arr = random.sample(range(1, 10000), n)  # Random array of size n

    print(f"\n\n=== Number of Elements: {n} ===")
    print("Original array (first 4 elements):", arr[:4])  # Show first 4 elements before sorting

    # --------- Merge Sort ---------
    arr_merge = arr.copy()
    start_time = time.time()
    merge_sort(arr_merge)
    end_time = time.time()
    merge_time = end_time - start_time
    merge_sort_times.append(merge_time)
    print("After Merge Sort (first 4 elements):", arr_merge[:4])
    print(f"Time taken by Merge Sort: {merge_time:.6f} seconds")

    # --------- Quick Sort ---------
    arr_quick = arr.copy()
    start_time = time.time()
    quick_sorted = quick_sort(arr_quick)
    end_time = time.time()
    quick_time = end_time - start_time
    quick_sort_times.append(quick_time)
    print("After Quick Sort (first 4 elements):", quick_sorted[:4])
    print(f"Time taken by Quick Sort: {quick_time:.6f} seconds")

    # --------- Storing n value ---------
    n_values.append(n)

# -----------------------------
# Plotting Graph
plt.plot(n_values, merge_sort_times, label='Merge Sort', marker='o', color='blue')
plt.plot(n_values, quick_sort_times, label='Quick Sort', marker='s', color='green')
plt.xlabel('Number of Elements (n)')
plt.ylabel('Time Taken (seconds)')
plt.title('Sorting Time vs Number of Elements')
plt.legend()
plt.grid(True)
plt.show()
