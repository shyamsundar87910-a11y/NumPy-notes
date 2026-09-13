# ===================== 12_NUMPY_ARRAY_SORTING.py =====================


import numpy as np


# .........................Basic Sorting.........................#

arr = np.array([50, 20, 40, 10, 30])

result = np.sort(arr)

print(result)


# .........................Sorting in Descending Order.........................#

arr = np.array([50, 20, 40, 10, 30])

result = np.sort(arr)[::-1]

print(result)


# .........................Sorting Strings.........................#

arr = np.array(["Python", "Java", "C", "SQL"])

result = np.sort(arr)

print(result)


# .........................Sorting Boolean Values.........................#

arr = np.array([True, False, True, False])

result = np.sort(arr)

print(result)


# .........................Sorting 2D Array.........................#

arr = np.array([
    [30, 10, 20],
    [60, 40, 50]
])

result = np.sort(arr)

print(result)


# .........................Sorting Along Axis 0.........................#

arr = np.array([
    [30, 10, 20],
    [60, 40, 50]
])

result = np.sort(arr, axis=0)

print(result)


# .........................Sorting Along Axis 1.........................#

arr = np.array([
    [30, 10, 20],
    [60, 40, 50]
])

result = np.sort(arr, axis=1)

print(result)


# .........................Finding Sorted Index Positions.........................#

arr = np.array([50, 20, 40, 10, 30])

result = np.argsort(arr)

print(result)


# .........................Descending Order Using argsort.........................#

arr = np.array([50, 20, 40, 10, 30])

result = np.argsort(arr)[::-1]

print(result)


# .........................Sorting Student Marks.........................#

marks = np.array([65, 90, 45, 78, 88])

sorted_marks = np.sort(marks)

print("Sorted Marks:", sorted_marks)


# .........................Highest Marks First.........................#

marks = np.array([65, 90, 45, 78, 88])

highest_first = np.sort(marks)[::-1]

print("Highest First:", highest_first)


# .........................Practical Example.........................#

sales = np.array([5000, 2500, 8000, 3500, 7000])

sorted_sales = np.sort(sales)

print("Sales:", sales)

print("Sorted Sales:", sorted_sales)

print("Highest Sales:", sorted_sales[-1])

print("Lowest Sales:", sorted_sales[0])
