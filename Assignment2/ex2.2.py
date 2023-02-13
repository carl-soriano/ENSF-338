import sys
import json
import threading
import time
import matplotlib.pyplot as plt
from time import perf_counter
threading.stack_size(33554432)

sys.setrecursionlimit(20000)

def func1(array, low, high):
  if low >= high:
    return

  pi = func2(array, low, high)
  func1(array, low, pi-1)
  func1(array, pi + 1, high)

def func2(array, start, end):
  p = array[start]
  low = start + 1
  high = end
  
  while True:
    while low <= high and array[high] >= p:
      high = high - 1
    while low <= high and array[low] <= p:
      low = low + 1
    if low <= high:
      array[low], array[high] = array[high], array[low]
    else:
      break
  array[start], array[high] = array[high], array[start]
  return high

with open('Assignment2/numbers.json', 'r') as f:
    data = json.load(f)

flat_data = [item for sublist in data for item in sublist]

if __name__ == "__main__":
    times = []
    records = []
    for record in data:
        start_time = perf_counter()
        func1(record, 0, len(record) - 1)
        end_time = perf_counter()
        time_each = end_time - start_time
        times.append(time_each)
        records.append(data.index(record) + 1)

    plt.plot(times)
    plt.title("Plot Time for Original Quick Sort")
    plt.xlabel("Elements")
    plt.ylabel("Seconds")
    plt.xticks(records)
    plt.show()
