# ===================== 16_NUMPY_MATHEMATICAL_FUNCTIONS.py =====================


import numpy as np


# .........................Square Root.........................#

arr = np.array([4, 9, 16, 25])

result = np.sqrt(arr)

print(result)


# .........................Power.........................#

arr = np.array([2, 3, 4, 5])

result = np.power(arr, 2)

print(result)


# .........................Absolute Value.........................#

arr = np.array([-10, -20, 30, -40])

result = np.abs(arr)

print(result)


# .........................Round.........................#

arr = np.array([2.4, 3.6, 4.5, 5.8])

result = np.round(arr)

print(result)


# .........................Floor.........................#

arr = np.array([2.4, 3.6, 4.9, 5.2])

result = np.floor(arr)

print(result)


# .........................Ceil.........................#

arr = np.array([2.4, 3.6, 4.1, 5.2])

result = np.ceil(arr)

print(result)


# .........................Exponential.........................#

arr = np.array([1, 2, 3, 4])

result = np.exp(arr)

print(result)


# .........................Logarithm.........................#

arr = np.array([1, 10, 100, 1000])

result = np.log(arr)

print(result)


# .........................Log Base 10.........................#

arr = np.array([1, 10, 100, 1000])

result = np.log10(arr)

print(result)


# .........................Maximum Between Arrays.........................#

arr1 = np.array([10, 50, 30, 80])

arr2 = np.array([20, 40, 60, 70])

result = np.maximum(arr1, arr2)

print(result)


# .........................Minimum Between Arrays.........................#

arr1 = np.array([10, 50, 30, 80])

arr2 = np.array([20, 40, 60, 70])

result = np.minimum(arr1, arr2)

print(result)


# .........................Trigonometric Functions.........................#

arr = np.array([0, 30, 45, 60, 90])

result = np.sin(np.deg2rad(arr))

print(result)


# .........................Cosine Function.........................#

arr = np.array([0, 30, 45, 60, 90])

result = np.cos(np.deg2rad(arr))

print(result)


# .........................Tangent Function.........................#

arr = np.array([0, 30, 45, 60])

result = np.tan(np.deg2rad(arr))

print(result)


# .........................Degree to Radian.........................#

degrees = np.array([0, 30, 45, 90])

radians = np.deg2rad(degrees)

print(radians)


# .........................Radian to Degree.........................#

radians = np.array([0, np.pi / 6, np.pi / 4, np.pi / 2])

degrees = np.rad2deg(radians)

print(degrees)


# .........................Practical Example.........................#

sales = np.array([100, 225, 400, 625])

result = np.sqrt(sales)

print("Sales:", sales)

print("Square Root:", result)


# .........................Practical Data Example.........................#

marks = np.array([45.6, 67.3, 78.8, 89.4, 92.7])

rounded_marks = np.round(marks)

print("Original Marks:", marks)

print("Rounded Marks:", rounded_marks)
