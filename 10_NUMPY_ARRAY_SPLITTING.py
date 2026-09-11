```python
# ===================== 10_NUMPY_ARRAY_SPLITTING.py =====================


# .........................Split 1D Array.........................#

import numpy as np

arr = np.array([10, 20, 30, 40, 50, 60])

result = np.array_split(arr, 3)

print(result)


# .........................Split Array into 2 Parts.........................#

arr = np.array([1, 2, 3, 4, 5, 6])

result = np.array_split(arr, 2)

print(result)


# .........................Split Array into 3 Parts.........................#

arr = np.array([10, 20, 30, 40, 50, 60, 70, 80, 90])

result = np.array_split(arr, 3)

print(result)


# .........................Access Split Arrays.........................#

arr = np.array([10, 20, 30, 40, 50, 60])

result = np.array_split(arr, 3)

print(result[0])
print(result[1])
print(result[2])


# .........................Split 2D Array Using axis=0.........................#

arr = np.array([
    [1, 2],
    [3, 4],
    [5, 6],
    [7, 8]
])

result = np.array_split(arr, 2, axis=0)

print(result)


# .........................Split 2D Array Using axis=1.........................#

arr = np.array([
    [1, 2, 3, 4],
    [5, 6, 7, 8]
])

result = np.array_split(arr, 2, axis=1)

print(result)


# .........................Split Rows.........................#

arr = np.array([
    [10, 20],
    [30, 40],
    [50, 60],
    [70, 80]
])

result = np.array_split(arr, 2)

print(result)


# .........................Split Columns.........................#

arr = np.array([
    [10, 20, 30, 40],
    [50, 60, 70, 80]
])

result = np.array_split(arr, 2, axis=1)

print(result)


# .........................Using hsplit().........................#

arr = np.array([
    [1, 2, 3, 4],
    [5, 6, 7, 8]
])

result = np.hsplit(arr, 2)

print(result)


# .........................Using vsplit().........................#

arr = np.array([
    [1, 2],
    [3, 4],
    [5, 6],
    [7, 8]
])

result = np.vsplit(arr, 2)

print(result)


# .........................Practical Example.........................#

marks = np.array([80, 75, 90, 85, 70, 95])

result = np.array_split(marks, 2)

print("Group 1:", result[0])
print("Group 2:", result[1])
```
