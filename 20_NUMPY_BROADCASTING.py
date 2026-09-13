# ===================== 20_NUMPY_BROADCASTING.py =====================


import numpy as np


# .........................Basic Broadcasting.........................#

arr = np.array([10, 20, 30, 40])

result = arr + 5

print(result)


# .........................Broadcasting With Multiplication.........................#

arr = np.array([10, 20, 30, 40])

result = arr * 2

print(result)


# .........................Broadcasting With 2D Array.........................#

arr = np.array([
    [10, 20, 30],
    [40, 50, 60]
])

result = arr + 10

print(result)


# .........................Broadcasting With Row Array.........................#

arr = np.array([
    [10, 20, 30],
    [40, 50, 60]
])

row = np.array([1, 2, 3])

result = arr + row

print(result)


# .........................Broadcasting With Column Array.........................#

arr = np.array([
    [10, 20, 30],
    [40, 50, 60]
])

column = np.array([
    [1],
    [2]
])

result = arr + column

print(result)


# .........................Broadcasting Subtraction.........................#

arr = np.array([
    [10, 20, 30],
    [40, 50, 60]
])

result = arr - 5

print(result)


# .........................Broadcasting Multiplication.........................#

arr = np.array([
    [10, 20, 30],
    [40, 50, 60]
])

result = arr * 2

print(result)


# .........................Broadcasting Division.........................#

arr = np.array([
    [10, 20, 30],
    [40, 50, 60]
])

result = arr / 10

print(result)


# .........................Broadcasting With Different Arrays.........................#

arr1 = np.array([
    [10, 20, 30],
    [40, 50, 60]
])

arr2 = np.array([1, 2, 3])

result = arr1 + arr2

print(result)


# .........................Broadcasting With Column Values.........................#

arr = np.array([
    [100, 200, 300],
    [400, 500, 600]
])

discount = np.array([
    [10],
    [20]
])

result = arr - discount

print(result)


# .........................Broadcasting and Shape.........................#

arr = np.array([
    [10, 20, 30],
    [40, 50, 60]
])

print("Shape:", arr.shape)

row = np.array([1, 2, 3])

print("Row Shape:", row.shape)

result = arr + row

print(result)


# .........................Practical Marks Example.........................#

marks = np.array([
    [60, 70, 80],
    [50, 65, 75],
    [80, 85, 90]
])

bonus = 5

new_marks = marks + bonus

print("Original Marks:")
print(marks)

print("After Bonus:")
print(new_marks)


# .........................Practical Sales Example.........................#

sales = np.array([
    [1000, 2000, 3000],
    [1500, 2500, 3500]
])

tax = np.array([100, 200, 300])

final_sales = sales + tax

print("Sales:")
print(sales)

print("After Tax:")
print(final_sales)


# .........................Broadcasting Example.........................#

prices = np.array([
    [100, 200, 300],
    [400, 500, 600]
])

discount = 10

discount_amount = prices * discount / 100

final_price = prices - discount_amount

print("Prices:")
print(prices)

print("Final Prices:")
print(final_price)
