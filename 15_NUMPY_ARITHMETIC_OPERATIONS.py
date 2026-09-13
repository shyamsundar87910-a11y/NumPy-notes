# ===================== 15_NUMPY_ARITHMETIC_OPERATIONS.py =====================


import numpy as np


# .........................Addition.........................#

arr = np.array([10, 20, 30, 40])

result = arr + 5

print(result)


# .........................Subtraction.........................#

arr = np.array([10, 20, 30, 40])

result = arr - 5

print(result)


# .........................Multiplication.........................#

arr = np.array([10, 20, 30, 40])

result = arr * 2

print(result)


# .........................Division.........................#

arr = np.array([10, 20, 30, 40])

result = arr / 2

print(result)


# .........................Power.........................#

arr = np.array([2, 3, 4, 5])

result = arr ** 2

print(result)


# .........................Modulus.........................#

arr = np.array([10, 15, 20, 25])

result = arr % 3

print(result)


# .........................Addition of Two Arrays.........................#

arr1 = np.array([10, 20, 30])

arr2 = np.array([5, 10, 15])

result = arr1 + arr2

print(result)


# .........................Subtraction of Two Arrays.........................#

arr1 = np.array([10, 20, 30])

arr2 = np.array([5, 10, 15])

result = arr1 - arr2

print(result)


# .........................Multiplication of Two Arrays.........................#

arr1 = np.array([10, 20, 30])

arr2 = np.array([2, 3, 4])

result = arr1 * arr2

print(result)


# .........................Division of Two Arrays.........................#

arr1 = np.array([10, 20, 30])

arr2 = np.array([2, 4, 5])

result = arr1 / arr2

print(result)


# .........................Addition Using np.add().........................#

arr1 = np.array([10, 20, 30])

arr2 = np.array([5, 10, 15])

result = np.add(arr1, arr2)

print(result)


# .........................Subtraction Using np.subtract().........................#

arr1 = np.array([10, 20, 30])

arr2 = np.array([5, 10, 15])

result = np.subtract(arr1, arr2)

print(result)


# .........................Multiplication Using np.multiply().........................#

arr1 = np.array([10, 20, 30])

arr2 = np.array([2, 3, 4])

result = np.multiply(arr1, arr2)

print(result)


# .........................Division Using np.divide().........................#

arr1 = np.array([10, 20, 30])

arr2 = np.array([2, 4, 5])

result = np.divide(arr1, arr2)

print(result)


# .........................Absolute Value.........................#

arr = np.array([-10, -20, 30, -40])

result = np.abs(arr)

print(result)


# .........................Remainder.........................#

arr = np.array([10, 20, 30, 40])

result = np.remainder(arr, 3)

print(result)


# .........................2D Array Arithmetic.........................#

arr1 = np.array([
    [10, 20],
    [30, 40]
])

arr2 = np.array([
    [1, 2],
    [3, 4]
])

print("Addition:")
print(arr1 + arr2)

print("Subtraction:")
print(arr1 - arr2)

print("Multiplication:")
print(arr1 * arr2)

print("Division:")
print(arr1 / arr2)


# .........................Practical Example.........................#

prices = np.array([100, 200, 300, 400])

discount = 10

discount_amount = prices * discount / 100

final_price = prices - discount_amount

print("Prices:", prices)

print("Discount:", discount_amount)

print("Final Prices:", final_price)
