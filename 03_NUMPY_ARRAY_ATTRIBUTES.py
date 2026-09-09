```python
# ===================== 03_NUMPY_ARRAY_ATTRIBUTES.py =====================


# .........................Create NumPy Array.........................#

import numpy as np

arr = np.array([
    [10, 20, 30],
    [40, 50, 60]
])

print(arr)


# .........................ndim — Number of Dimensions.........................#

print(arr.ndim)


# .........................shape — Rows and Columns.........................#

print(arr.shape)


# .........................size — Total Number of Elements.........................#

print(arr.size)


# .........................dtype — Data Type of Elements.........................#

print(arr.dtype)


# .........................itemsize — Size of Each Element in Bytes.........................#

print(arr.itemsize)


# .........................nbytes — Total Bytes Consumed.........................#

print(arr.nbytes)


# .........................Attributes Together.........................#

print("Dimensions:", arr.ndim)
print("Shape:", arr.shape)
print("Size:", arr.size)
print("Data Type:", arr.dtype)
print("Item Size:", arr.itemsize)
print("Total Bytes:", arr.nbytes)


# .........................Attributes with 1D Array.........................#

arr = np.array([10, 20, 30, 40, 50])

print("Dimensions:", arr.ndim)
print("Shape:", arr.shape)
print("Size:", arr.size)
print("Data Type:", arr.dtype)


# .........................Attributes with 3D Array.........................#

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

print("Dimensions:", arr.ndim)
print("Shape:", arr.shape)
print("Size:", arr.size)
print("Data Type:", arr.dtype)
```
