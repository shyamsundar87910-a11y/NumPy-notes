# ===================== 14_NUMPY_COPY_AND_VIEW.py =====================


import numpy as np


# .........................Basic Copy.........................#

arr = np.array([10, 20, 30, 40])

copy_arr = arr.copy()

print("Original:", arr)
print("Copy:", copy_arr)


# .........................Changing Copy.........................#

arr = np.array([10, 20, 30, 40])

copy_arr = arr.copy()

copy_arr[0] = 100

print("Original:", arr)
print("Copy:", copy_arr)


# .........................Basic View.........................#

arr = np.array([10, 20, 30, 40])

view_arr = arr.view()

print("Original:", arr)
print("View:", view_arr)


# .........................Changing View.........................#

arr = np.array([10, 20, 30, 40])

view_arr = arr.view()

view_arr[0] = 100

print("Original:", arr)
print("View:", view_arr)


# .........................Copy Does Not Affect Original.........................#

arr = np.array([10, 20, 30])

copy_arr = arr.copy()

copy_arr[1] = 200

print("Original:", arr)
print("Copy:", copy_arr)


# .........................View Affects Original.........................#

arr = np.array([10, 20, 30])

view_arr = arr.view()

view_arr[1] = 200

print("Original:", arr)
print("View:", view_arr)


# .........................Check Base of Copy.........................#

arr = np.array([10, 20, 30])

copy_arr = arr.copy()

print(copy_arr.base)


# .........................Check Base of View.........................#

arr = np.array([10, 20, 30])

view_arr = arr.view()

print(view_arr.base)


# .........................Changing Original After Copy.........................#

arr = np.array([10, 20, 30])

copy_arr = arr.copy()

arr[0] = 500

print("Original:", arr)
print("Copy:", copy_arr)


# .........................Changing Original After View.........................#

arr = np.array([10, 20, 30])

view_arr = arr.view()

arr[0] = 500

print("Original:", arr)
print("View:", view_arr)


# .........................2D Array Copy.........................#

arr = np.array([
    [10, 20],
    [30, 40]
])

copy_arr = arr.copy()

copy_arr[0, 0] = 100

print("Original:")
print(arr)

print("Copy:")
print(copy_arr)


# .........................2D Array View.........................#

arr = np.array([
    [10, 20],
    [30, 40]
])

view_arr = arr.view()

view_arr[0, 0] = 100

print("Original:")
print(arr)

print("View:")
print(view_arr)


# .........................Practical Example.........................#

marks = np.array([65, 78, 90, 55, 88])

backup_marks = marks.copy()

backup_marks[0] = 100

print("Original Marks:", marks)
print("Backup Marks:", backup_marks)
