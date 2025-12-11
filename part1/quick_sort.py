#LAB-1 QUICK SORT
#1. Sort a given set of elements and determine the time (t) required to sort the elements.
#2. Repeat the experiment for different set of values ( n) and
#3. Plot a graph of the time taken versus n. 

import time
import random
import matplotlib.pyplot as plt

def quicksort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr)//2]
    left = [x for x in arr if x < pivot]
    mid = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quicksort(left) + mid + quicksort(right)

sizes = [1000, 2000, 5000, 10000, 20000]
times = []

for n in sizes:
    arr = [random.randint(1, 100000) for _ in range(n)]
    start = time.time()
    quicksort(arr)
    end = time.time()
    times.append(end - start)
    print(f"n={n}, t={end-start:.5f} seconds")

plt.plot(sizes, times)
plt.xlabel("Input Size (n)")
plt.ylabel("Time Taken (seconds)")
plt.title("QuickSort Performance: Time vs n")
plt.show()
