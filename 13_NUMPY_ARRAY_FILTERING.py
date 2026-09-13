# ===================== 13_NUMPY_ARRAY_FILTERING.py =====================


import numpy as np


# .........................Basic Filtering.........................#

arr = np.array([10, 20, 30, 40, 50])

filtered = arr[arr > 25]

print(filtered)


# .........................Filter Even Numbers.........................#

arr = np.array([10, 15, 20, 25, 30, 35])

even_numbers = arr[arr % 2 == 0]

print(even_numbers)


# .........................Filter Odd Numbers.........................#

arr = np.array([10, 15, 20, 25, 30, 35])

odd_numbers = arr[arr % 2 != 0]

print(odd_numbers)


# .........................Filter Greater Than.........................#

arr = np.array([10, 20, 30, 40, 50])

result = arr[arr > 30]

print(result)


# .........................Filter Less Than.........................#

arr = np.array([10, 20, 30, 40, 50])

result = arr[arr < 30]

print(result)


# .........................Filter Between Two Values.........................#

arr = np.array([10, 20, 30, 40, 50, 60])

result = arr[(arr >= 20) & (arr <= 50)]

print(result)


# .........................Filter Using OR Condition.........................#

arr = np.array([10, 20, 30, 40, 50])

result = arr[(arr < 20) | (arr > 40)]

print(result)


# .........................Filter Positive Numbers.........................#

arr = np.array([-10, 20, -30, 40, -50, 60])

positive = arr[arr > 0]

print(positive)


# .........................Filter Negative Numbers.........................#

arr = np.array([-10, 20, -30, 40, -50, 60])

negative = arr[arr < 0]

print(negative)


# .........................Filter 2D Array.........................#

arr = np.array([
    [10, 20, 30],
    [40, 50, 60]
])

result = arr[arr > 30]

print(result)


# .........................Filter Student Marks.........................#

marks = np.array([35, 78, 45, 90, 32, 65, 88])

passed = marks[marks >= 40]

print("Passed Marks:", passed)


# .........................Filter Failed Students.........................#

marks = np.array([35, 78, 45, 90, 32, 65, 88])

failed = marks[marks < 40]

print("Failed Marks:", failed)


# .........................Filter High Scores.........................#

scores = np.array([45, 82, 67, 91, 55, 76, 95])

high_scores = scores[scores >= 80]

print("High Scores:", high_scores)


# .........................Practical Data Analysis Example.........................#

sales = np.array([1200, 4500, 2300, 6700, 3200, 8900])

high_sales = sales[sales > 3000]

print("Sales Greater Than 3000:", high_sales)
