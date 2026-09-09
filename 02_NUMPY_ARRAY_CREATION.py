```python
# ===================== 02_NUMPY_ARRAY_CREATION.py =====================


# .........................Create Array Using List.........................#

import numpy as np

arr = np.array([10, 20, 30, 40, 50])

print(arr)


# .........................Create Array Using Tuple.........................#

arr = np.array((10, 20, 30, 40, 50))

print(arr)


# .........................Create 2D Array.........................#

arr = np.array([
    [1, 2, 3],
    [4, 5, 6]
])

print(arr)


# .........................Create 3D Array.........................#

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

print(arr)


# .........................Create Array Using arange().........................#

arr = np.arange(1, 11)

print(arr)


# .........................Create Array Using arange() with Step.........................#

arr = np.arange(0, 20, 2)

print(arr)


# .........................Create Array of Zeros.........................#

arr = np.zeros(5)

print(arr)


# .........................Create 2D Array of Zeros.........................#

arr = np.zeros((2, 3))

print(arr)


# .........................Create Array of Ones.........................#

arr = np.ones(5)

print(arr)


# .........................Create 2D Array of Ones.........................#

arr = np.ones((2, 3))

print(arr)


# .........................Create Array with Full Value.........................#

arr = np.full(5, 10)

print(arr)


# .........................Create 2D Array with Full Value.........................#

arr = np.full((2, 3), 7)

print(arr)


# .........................Create Identity Matrix.........................#

arr = np.eye(3)

print(arr)


# .........................Create Even Numbers.........................#

arr = np.arange(2, 21, 2)

print(arr)


# .........................Create Odd Numbers.........................#

arr = np.arange(1, 20, 2)

print(arr)
```
