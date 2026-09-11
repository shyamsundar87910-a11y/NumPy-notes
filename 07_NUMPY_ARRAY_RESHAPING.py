```python
# ===================== 07_NUMPY_ARRAY_RESHAPING.py =====================


# .........................1D to 2D Array.........................#

import numpy as np

arr = np.array([1, 2, 3, 4, 5, 6])

new_arr = arr.reshape(2, 3)

print(new_arr)


# .........................1D to 3D Array.........................#

arr = np.array([1, 2, 3, 4, 5, 6, 7, 8])

new_arr = arr.reshape(2, 2, 2)

print(new_arr)


# .........................Reshape into Rows and Columns.........................#

arr = np.arange(1, 13)

new_arr = arr.reshape(3, 4)

print(new_arr)


# .........................Reshape into 4 Rows.........................#

arr = np.arange(1, 13)

new_arr = arr.reshape(4, 3)

print(new_arr)


# .........................Using -1 in Reshape.........................#

arr = np.array([1, 2, 3, 4, 5, 6])

new_arr = arr.reshape(2, -1)

print(new_arr)


# .........................Flatten Array.........................#

arr = np.array([
    [1, 2, 3],
    [4, 5, 6]
])

new_arr = arr.reshape(-1)

print(new_arr)


# .........................Flatten Using flatten().........................#

arr = np.array([
    [1, 2, 3],
    [4, 5, 6]
])

new_arr = arr.flatten()

print(new_arr)


# .........................Flatten Using ravel().........................#

arr = np.array([
    [1, 2, 3],
    [4, 5, 6]
])

new_arr = arr.ravel()

print(new_arr)


# .........................Check Shape Before Reshape.........................#

arr = np.arange(1, 13)

print("Before:", arr.shape)

new_arr = arr.reshape(3, 4)

print("After:", new_arr.shape)


# .........................Reshape 2D Array.........................#

arr = np.array([
    [1, 2, 3],
    [4, 5, 6]
])

new_arr = arr.reshape(3, 2)

print(new_arr)


# .........................Reshape with Different Dimensions.........................#

arr = np.arange(1, 25)

new_arr = arr.reshape(2, 3, 4)

print(new_arr)


# .........................Invalid Reshape.........................#

arr = np.array([1, 2, 3, 4, 5, 6])

# This will give an error because
# 6 elements cannot be reshaped into 4 rows and 2 columns.

# new_arr = arr.reshape(4, 2)
# print(new_arr)
```
