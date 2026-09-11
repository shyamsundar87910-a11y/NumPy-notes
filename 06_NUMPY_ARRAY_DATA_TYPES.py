```python
# ===================== 06_NUMPY_ARRAY_DATA_TYPES.py =====================


# .........................Integer Data Type.........................#

import numpy as np

arr = np.array([10, 20, 30, 40])

print(arr)
print(arr.dtype)


# .........................Float Data Type.........................#

arr = np.array([10.5, 20.5, 30.5])

print(arr)
print(arr.dtype)


# .........................String Data Type.........................#

arr = np.array(["Apple", "Banana", "Mango"])

print(arr)
print(arr.dtype)


# .........................Boolean Data Type.........................#

arr = np.array([True, False, True, False])

print(arr)
print(arr.dtype)


# .........................Create Integer Array Using dtype.........................#

arr = np.array([10, 20, 30], dtype="int32")

print(arr)
print(arr.dtype)


# .........................Create Float Array Using dtype.........................#

arr = np.array([10, 20, 30], dtype="float64")

print(arr)
print(arr.dtype)


# .........................Create String Array Using dtype.........................#

arr = np.array([10, 20, 30], dtype="str")

print(arr)
print(arr.dtype)


# .........................Convert Integer to Float.........................#

arr = np.array([10, 20, 30])

new_arr = arr.astype(float)

print(arr)
print(new_arr)
print(new_arr.dtype)


# .........................Convert Float to Integer.........................#

arr = np.array([10.5, 20.5, 30.5])

new_arr = arr.astype(int)

print(arr)
print(new_arr)
print(new_arr.dtype)


# .........................Convert Integer to String.........................#

arr = np.array([10, 20, 30])

new_arr = arr.astype(str)

print(new_arr)
print(new_arr.dtype)


# .........................Convert Integer to Boolean.........................#

arr = np.array([0, 1, 2, 3])

new_arr = arr.astype(bool)

print(new_arr)
print(new_arr.dtype)


# .........................Check Data Type.........................#

arr = np.array([10, 20, 30])

print("Data Type:", arr.dtype)


# .........................Change Data Type.........................#

arr = np.array([10, 20, 30])

arr = arr.astype(float)

print(arr)
print(arr.dtype)
```
