import os, sys
# print(sys.path)
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from tools import Timer

timer = Timer()
timer.start()


def quicksort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quicksort(left) + middle + quicksort(right)


# py 1.47s，pypy 0.97s
for i in range(100):
    quicksort(range(10000, 0, -1))

print(quicksort([3, 6, 8, 10, 1, 2, 1]))

print(f'{timer.stop():.6f} sec')
