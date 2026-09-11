```python
# ===================== 08_NUMPY_ARRAY_ITERATION.py =====================


# .........................Iterate 1D Array.........................#

import numpy as np

arr = np.array([10, 20, 30, 40, 50])

for value in arr:
    print(value)


# .........................Iterate 2D Array.........................#

arr = np.array([
    [1, 2, 3],
    [4, 5, 6]
])

for row in arr:
    print(row)


# .........................Iterate Each Element of 2D Array.........................#

for row in arr:
    for value in row:
        print(value)


# .........................Iterate 3D Array.........................#

arr = np.array([
    [
        [1, 2],
        [3, 4]
    ],
    [
        [5, 6],
        [7, 8]
    ]
])

for block in arr:
    print(block)


# .........................Iterate Each Element of 3D Array.........................#

for block in arr:
    for row in block:
        for value in row:
            print(value)


# .........................Using nditer().........................#

arr = np.array([
    [10, 20, 30],
    [40, 50, 60]
])

for value in np.nditer(arr):
    print(value)


# .........................nditer() with Data Type.........................#

arr = np.array([1, 2, 3, 4, 5])

for value in np.nditer(arr, flags=["buffered"], op_dtypes=["float64"]):
    print(value)


# .........................Iterate with Index Using enumerate().........................#

arr = np.array([10, 20, 30, 40, 50])

for index, value in enumerate(arr):
    print("Index:", index, "Value:", value)


# .........................Iterate with Index in 2D Array.........................#

arr = np.array([
    [10, 20, 30],
    [40, 50, 60]
])

for index, row in enumerate(arr):
    print("Index:", index, "Row:", row)


# .........................Iterate Using ndenumerate().........................#

arr = np.array([
    [10, 20, 30],
    [40, 50, 60]
])

for index, value in np.ndenumerate(arr):
    print("Index:", index, "Value:", value)


# .........................Modify Array Using Loop.........................#

arr = np.array([10, 20, 30, 40, 50])

for i in range(len(arr)):
    arr[i] = arr[i] + 10

print(arr)


# .........................Print Even Numbers.........................#

arr = np.array([10, 15, 20, 25, 30, 35])

for value in arr:
    if value % 2 == 0:
        print(value)


# .........................Print Values Greater Than 20.........................#

arr = np.array([10, 25, 15, 40, 30, 5])

for value in arr:
    if value > 20:
        print(value)
```
