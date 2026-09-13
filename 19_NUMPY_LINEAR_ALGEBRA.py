# ===================== 19_NUMPY_LINEAR_ALGEBRA.py =====================


import numpy as np


# .........................Matrix Creation.........................#

matrix = np.array([
    [1, 2],
    [3, 4]
])

print(matrix)


# .........................Matrix Addition.........................#

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


# .........................Matrix Subtraction.........................#

matrix1 = np.array([
    [5, 6],
    [7, 8]
])

matrix2 = np.array([
    [1, 2],
    [3, 4]
])

result = matrix1 - matrix2

print(result)


# .........................Matrix Multiplication.........................#

matrix1 = np.array([
    [1, 2],
    [3, 4]
])

matrix2 = np.array([
    [5, 6],
    [7, 8]
])

result = np.matmul(matrix1, matrix2)

print(result)


# .........................Matrix Multiplication Using @.........................#

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


# .........................Transpose.........................#

matrix = np.array([
    [1, 2, 3],
    [4, 5, 6]
])

result = np.transpose(matrix)

print(result)


# .........................Transpose Using .T.........................#

matrix = np.array([
    [1, 2, 3],
    [4, 5, 6]
])

result = matrix.T

print(result)


# .........................Determinant.........................#

matrix = np.array([
    [1, 2],
    [3, 4]
])

result = np.linalg.det(matrix)

print(result)


# .........................Inverse of Matrix.........................#

matrix = np.array([
    [1, 2],
    [3, 4]
])

result = np.linalg.inv(matrix)

print(result)


# .........................Identity Matrix.........................#

result = np.eye(3)

print(result)


# .........................Diagonal Matrix.........................#

matrix = np.array([
    [10, 20, 30],
    [40, 50, 60],
    [70, 80, 90]
])

result = np.diag(matrix)

print(result)


# .........................Trace of Matrix.........................#

matrix = np.array([
    [1, 2],
    [3, 4]
])

result = np.trace(matrix)

print(result)


# .........................Dot Product.........................#

arr1 = np.array([1, 2, 3])

arr2 = np.array([4, 5, 6])

result = np.dot(arr1, arr2)

print(result)


# .........................Solve Linear Equations.........................#

A = np.array([
    [2, 1],
    [1, 3]
])

B = np.array([5, 6])

result = np.linalg.solve(A, B)

print(result)


# .........................Eigenvalues.........................#

matrix = np.array([
    [1, 2],
    [2, 1]
])

values = np.linalg.eigvals(matrix)

print(values)


# .........................Matrix Rank.........................#

matrix = np.array([
    [1, 2],
    [3, 4]
])

result = np.linalg.matrix_rank(matrix)

print(result)


# .........................Practical Example.........................#

sales = np.array([
    [100, 200],
    [300, 400]
])

prices = np.array([
    [10, 20],
    [30, 40]
])

result = sales * prices

print("Sales:")
print(sales)

print("Prices:")
print(prices)

print("Total Values:")
print(result)
