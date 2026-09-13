# ===================== 24_NUMPY_PRACTICE_QUESTIONS.py =====================


import numpy as np


# .........................Question 1: Create an Array.........................#

arr = np.array([10, 20, 30, 40, 50])

print(arr)


# .........................Question 2: Find Array Dimension.........................#

arr = np.array([
    [10, 20, 30],
    [40, 50, 60]
])

print(arr.ndim)


# .........................Question 3: Find Shape.........................#

arr = np.array([
    [10, 20, 30],
    [40, 50, 60]
])

print(arr.shape)


# .........................Question 4: Find Size.........................#

arr = np.array([10, 20, 30, 40, 50])

print(arr.size)


# .........................Question 5: Find Data Type.........................#

arr = np.array([10, 20, 30, 40])

print(arr.dtype)


# .........................Question 6: Find Maximum Value.........................#

arr = np.array([10, 50, 30, 80, 20])

print(np.max(arr))


# .........................Question 7: Find Minimum Value.........................#

arr = np.array([10, 50, 30, 80, 20])

print(np.min(arr))


# .........................Question 8: Find Average.........................#

marks = np.array([60, 70, 80, 90, 100])

print(np.mean(marks))


# .........................Question 9: Find Even Numbers.........................#

arr = np.array([10, 15, 20, 25, 30, 35])

even_numbers = arr[arr % 2 == 0]

print(even_numbers)


# .........................Question 10: Find Odd Numbers.........................#

arr = np.array([10, 15, 20, 25, 30, 35])

odd_numbers = arr[arr % 2 != 0]

print(odd_numbers)


# .........................Question 11: Find Values Greater Than 50.........................#

arr = np.array([20, 40, 60, 80, 100])

result = arr[arr > 50]

print(result)


# .........................Question 12: Sort an Array.........................#

arr = np.array([50, 20, 40, 10, 30])

result = np.sort(arr)

print(result)


# .........................Question 13: Reverse an Array.........................#

arr = np.array([10, 20, 30, 40, 50])

result = arr[::-1]

print(result)


# .........................Question 14: Calculate Total.........................#

arr = np.array([10, 20, 30, 40, 50])

print(np.sum(arr))


# .........................Question 15: Calculate Standard Deviation.........................#

marks = np.array([50, 60, 70, 80, 90])

print(np.std(marks))


# .........................Question 16: Reshape Array.........................#

arr = np.arange(1, 13)

result = arr.reshape(3, 4)

print(result)


# .........................Question 17: Create Zeros Array.........................#

result = np.zeros(5)

print(result)


# .........................Question 18: Create Ones Array.........................#

result = np.ones(5)

print(result)


# .........................Question 19: Generate Random Numbers.........................#

result = np.random.randint(1, 100, 5)

print(result)


# .........................Question 20: Find Highest Marks Position.........................#

marks = np.array([65, 78, 90, 55, 88])

position = np.argmax(marks)

print(position)


# .........................Question 21: Find Lowest Marks Position.........................#

marks = np.array([65, 78, 90, 55, 88])

position = np.argmin(marks)

print(position)


# .........................Question 22: Calculate Percentage.........................#

marks = np.array([80, 75, 90, 85, 70])

total = np.sum(marks)

percentage = (total / 500) * 100

print(percentage)


# .........................Question 23: Filter Passing Marks.........................#

marks = np.array([35, 45, 67, 30, 78, 90, 25])

passed = marks[marks >= 40]

print(passed)


# .........................Question 24: Filter Failed Marks.........................#

marks = np.array([35, 45, 67, 30, 78, 90, 25])

failed = marks[marks < 40]

print(failed)


# .........................Question 25: Sales Analysis.........................#

sales = np.array([1200, 2500, 1800, 3200, 4500])

print("Total Sales:", np.sum(sales))

print("Average Sales:", np.mean(sales))

print("Highest Sales:", np.max(sales))

print("Lowest Sales:", np.min(sales))


# .........................Question 26: Sales Above Average.........................#

sales = np.array([1200, 2500, 1800, 3200, 4500])

average = np.mean(sales)

result = sales[sales > average]

print(result)


# .........................Question 27: Matrix Addition.........................#

matrix1 = np.array([
    [1, 2],
    [3, 4]
])

matrix2 = np.array([
    [5, 6],
    [7, 8]
])

result = matrix1 + matrix2

print(result)


# .........................Question 28: Matrix Multiplication.........................#

matrix1 = np.array([
    [1, 2],
    [3, 4]
])

matrix2 = np.array([
    [5, 6],
    [7, 8]
])

result = matrix1 @ matrix2

print(result)


# .........................Question 29: Find Square Root.........................#

arr = np.array([4, 9, 16, 25])

result = np.sqrt(arr)

print(result)


# .........................Question 30: Practical Data Analysis.........................#

data = np.array([45, 67, 89, 32, 76, 90, 55, 82])

average = np.mean(data)

above_average = data[data > average]

print("Data:", data)

print("Average:", average)

print("Highest:", np.max(data))

print("Lowest:", np.min(data))

print("Above Average:", above_average)

print("Sorted Data:", np.sort(data))
