```python
# ===================== 09_NUMPY_ARRAY_JOINING.py =====================


# .........................Join 1D Arrays.........................#

import numpy as np

arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])

result = np.concatenate((arr1, arr2))

print(result)


# .........................Join Three Arrays.........................#

arr1 = np.array([10, 20])
arr2 = np.array([30, 40])
arr3 = np.array([50, 60])

result = np.concatenate((arr1, arr2, arr3))

print(result)


# .........................Join 2D Arrays Using axis=0.........................#

arr1 = np.array([
    [1, 2],
    [3, 4]
])

arr2 = np.array([
    [5, 6],
    [7, 8]
])

result = np.concatenate((arr1, arr2), axis=0)

print(result)


# .........................Join 2D Arrays Using axis=1.........................#

arr1 = np.array([
    [1, 2],
    [3, 4]
])

arr2 = np.array([
    [5, 6],
    [7, 8]
])

result = np.concatenate((arr1, arr2), axis=1)

print(result)


# .........................Stack Arrays Using vstack().........................#

arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])

result = np.vstack((arr1, arr2))

print(result)


# .........................Stack Arrays Using hstack().........................#

arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])

result = np.hstack((arr1, arr2))

print(result)


# .........................Stack Arrays Using dstack().........................#

arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])

result = np.dstack((arr1, arr2))

print(result)


# .........................Join Arrays Using stack().........................#

arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])

result = np.stack((arr1, arr2))

print(result)


# .........................Stack Using axis=0.........................#

result = np.stack((arr1, arr2), axis=0)

print(result)


# .........................Stack Using axis=1.........................#

result = np.stack((arr1, arr2), axis=1)

print(result)


# .........................Practical Example.........................#

student1 = np.array([80, 75, 90])
student2 = np.array([85, 70, 95])

marks = np.vstack((student1, student2))

print(marks)
```
