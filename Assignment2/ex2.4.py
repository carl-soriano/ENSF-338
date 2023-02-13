import sys
import json
import time
import matplotlib.pyplot as plt
from time import perf_counter

sys.setrecursionlimit(20000)

def iterative_quick_sort(arr, low, high):
    stack = [(low, high)]
    while stack:
        low, high = stack.pop()
        if low >= high:
            continue
        pivot = partition(arr, low, high)
        stack.append((low, pivot - 1))
        stack.append((pivot + 1, high))

def partition(arr, low, high):
    pivot = arr[low]
    i = low + 1
    j = high
    while True:
        while i <= j and arr[i] <= pivot:
            i += 1
        while i <= j and arr[j] >= pivot:
            j -= 1
        if i <= j:
            arr[i], arr[j] = arr[j], arr[i]
        else:
            break
    arr[low], arr[j] = arr[j], arr[low]
    return j

with open('Assignment2/numbers.json', 'r') as f:
    data = json.load(f)

if __name__ == "__main__":
    times = []
    records = []
    for record in data:
        start_time = perf_counter()
        iterative_quick_sort(record, 0, len(record) - 1)
        end_time = perf_counter()
        time_each = end_time - start_time
        times.append(time_each)
        records.append(data.index(record) + 1)

    plt.plot(times)
    plt.title("Plot Time for Optimized Quick Sort")
    plt.xlabel("Elements")
    plt.ylabel("Seconds")
    plt.xticks(records)
    plt.show()
