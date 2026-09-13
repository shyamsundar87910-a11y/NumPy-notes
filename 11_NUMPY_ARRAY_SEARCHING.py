# ===================== 11_NUMPY_ARRAY_SEARCHING.py =====================


import numpy as np


# .........................Search in Array.........................#

arr = np.array([10, 20, 30, 40, 50])

result = np.where(arr == 30)

print(result)


# .........................Search for Multiple Values.........................#

arr = np.array([10, 20, 30, 40, 50])

result = np.where(arr > 30)

print(result)


# .........................Search for Even Numbers.........................#

arr = np.array([10, 15, 20, 25, 30, 35])

result = np.where(arr % 2 == 0)

print(result)


# .........................Search for Odd Numbers.........................#

arr = np.array([10, 15, 20, 25, 30, 35])

result = np.where(arr % 2 != 0)

print(result)


# .........................Search in 2D Array.........................#

arr = np.array([
    [10, 20, 30],
    [40, 50, 60]
])

result = np.where(arr == 50)

print(result)


# .........................Search Values Greater Than.........................#

arr = np.array([10, 20, 30, 40, 50])

result = np.where(arr > 25)

print(result)


# .........................Search Values Less Than.........................#

arr = np.array([10, 20, 30, 40, 50])

result = np.where(arr < 35)

print(result)


# .........................Search Between Two Values.........................#

arr = np.array([10, 20, 30, 40, 50, 60])

result = np.where((arr >= 20) & (arr <= 50))

print(result)


# .........................Search Maximum Value Position.........................#

arr = np.array([10, 50, 30, 80, 20])

result = np.argmax(arr)

print(result)


# .........................Search Minimum Value Position.........................#

arr = np.array([10, 50, 30, 80, 20])

result = np.argmin(arr)

print(result)


# .........................Find Maximum Value.........................#

arr = np.array([10, 50, 30, 80, 20])

print(np.max(arr))


# .........................Find Minimum Value.........................#

arr = np.array([10, 50, 30, 80, 20])

print(np.min(arr))


# .........................Practical Example.........................#

marks = np.array([45, 78, 90, 32, 65, 88, 55])

passed_students = np.where(marks >= 40)

print("Passed Students:", passed_students)

highest_student = np.argmax(marks)

print("Highest Marks Position:", highest_student)

print("Highest Marks:", np.max(marks))
