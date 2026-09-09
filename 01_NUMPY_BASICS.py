
# ===================== 01_NUMPY_BASICS.py =====================


# .........................Import NumPy.........................#

import numpy as np

print("NumPy imported successfully")


# .........................Check NumPy Version.........................#

print(np.__version__)


# .........................Create NumPy Array.........................#

arr = np.array([10, 20, 30, 40, 50])

print(arr)


# .........................One Dimensional Array.........................#

arr = np.array([1, 2, 3, 4, 5])

print(arr)


# .........................Two Dimensional Array.........................#

arr = np.array([
    [1, 2, 3],
    [4, 5, 6]
])

print(arr)


# .........................Three Dimensional Array.........................#

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

print(arr)


# .........................Check Number of Dimensions.........................#

arr = np.array([10, 20, 30, 40, 50])

print(arr.ndim)


# .........................Python List.........................#

numbers = [10, 20, 30, 40, 50]

print(numbers)


# .........................NumPy Array.........................#

numbers = np.array([10, 20, 30, 40, 50])

print(numbers)


# .........................Basic Array Operations.........................#

arr = np.array([10, 20, 30, 40, 50])

print(arr + 10)
print(arr - 10)
print(arr * 2)
print(arr / 2)
```
