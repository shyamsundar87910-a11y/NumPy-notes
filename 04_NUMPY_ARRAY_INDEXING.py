```python
# ===================== 04_NUMPY_ARRAY_INDEXING.py =====================


# .........................1D Array Indexing.........................#

import numpy as np

arr = np.array([10, 20, 30, 40, 50])

print(arr[0])
print(arr[1])
print(arr[2])
print(arr[3])
print(arr[4])


# .........................Negative Indexing.........................#

print(arr[-1])
print(arr[-2])
print(arr[-3])


# .........................Access First Element.........................#

print(arr[0])


# .........................Access Last Element.........................#

print(arr[-1])


# .........................2D Array Indexing.........................#

arr = np.array([
    [10, 20, 30],
    [40, 50, 60]
])

print(arr[0, 0])
print(arr[0, 1])
print(arr[0, 2])

print(arr[1, 0])
print(arr[1, 1])
print(arr[1, 2])


# .........................Access First Row.........................#

print(arr[0])


# .........................Access Second Row.........................#

print(arr[1])


# .........................Access First Column.........................#

print(arr[:, 0])


# .........................Access Second Column.........................#

print(arr[:, 1])


# .........................Access Third Column.........................#

print(arr[:, 2])


# .........................Negative Indexing in 2D Array.........................#

print(arr[-1, -1])
print(arr[-1, -2])
print(arr[-2, -1])


# .........................3D Array Indexing.........................#

arr = np.array([
    [
        [1, 2, 3],
        [4, 5, 6]
    ],
    [
        [7, 8, 9],
        [10, 11, 12]
    ]
])

print(arr[0, 0, 0])
print(arr[0, 1, 2])
print(arr[1, 0, 1])
print(arr[1, 1, 2])


# .........................Change Array Element Using Index.........................#

arr = np.array([10, 20, 30, 40, 50])

arr[0] = 100

print(arr)


# .........................Change 2D Array Element.........................#

arr = np.array([
    [10, 20, 30],
    [40, 50, 60]
])

arr[0, 1] = 200

print(arr)


# .........................Multiple Elements Using Indexing.........................#

arr = np.array([10, 20, 30, 40, 50])

print(arr[1])
print(arr[3])


# .........................Indexing with Expression.........................#

arr = np.array([10, 20, 30, 40, 50])

print(arr[2] + arr[4])
print(arr[1] * arr[3])
```
