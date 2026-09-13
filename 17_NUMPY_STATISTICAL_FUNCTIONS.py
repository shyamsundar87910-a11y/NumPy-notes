# ===================== 17_NUMPY_STATISTICAL_FUNCTIONS.py =====================


import numpy as np


# .........................Mean.........................#

arr = np.array([10, 20, 30, 40, 50])

result = np.mean(arr)

print(result)


# .........................Median.........................#

arr = np.array([10, 20, 30, 40, 50])

result = np.median(arr)

print(result)


# .........................Standard Deviation.........................#

arr = np.array([10, 20, 30, 40, 50])

result = np.std(arr)

print(result)


# .........................Variance.........................#

arr = np.array([10, 20, 30, 40, 50])

result = np.var(arr)

print(result)


# .........................Minimum Value.........................#

arr = np.array([10, 50, 30, 80, 20])

result = np.min(arr)

print(result)


# .........................Maximum Value.........................#

arr = np.array([10, 50, 30, 80, 20])

result = np.max(arr)

print(result)


# .........................Sum.........................#

arr = np.array([10, 20, 30, 40, 50])

result = np.sum(arr)

print(result)


# .........................Cumulative Sum.........................#

arr = np.array([10, 20, 30, 40])

result = np.cumsum(arr)

print(result)


# .........................Product.........................#

arr = np.array([2, 3, 4, 5])

result = np.prod(arr)

print(result)


# .........................Cumulative Product.........................#

arr = np.array([2, 3, 4])

result = np.cumprod(arr)

print(result)


# .........................Percentile.........................#

arr = np.array([10, 20, 30, 40, 50])

result = np.percentile(arr, 50)

print(result)


# .........................Percentile 25.........................#

arr = np.array([10, 20, 30, 40, 50])

result = np.percentile(arr, 25)

print(result)


# .........................Percentile 75.........................#

arr = np.array([10, 20, 30, 40, 50])

result = np.percentile(arr, 75)

print(result)


# .........................Correlation Coefficient.........................#

x = np.array([10, 20, 30, 40, 50])

y = np.array([20, 40, 60, 80, 100])

result = np.corrcoef(x, y)

print(result)


# .........................Statistics on 2D Array.........................#

arr = np.array([
    [10, 20, 30],
    [40, 50, 60]
])

print("Mean:", np.mean(arr))

print("Median:", np.median(arr))

print("Minimum:", np.min(arr))

print("Maximum:", np.max(arr))

print("Sum:", np.sum(arr))


# .........................Mean Along Axis 0.........................#

arr = np.array([
    [10, 20, 30],
    [40, 50, 60]
])

result = np.mean(arr, axis=0)

print(result)


# .........................Mean Along Axis 1.........................#

arr = np.array([
    [10, 20, 30],
    [40, 50, 60]
])

result = np.mean(arr, axis=1)

print(result)


# .........................Practical Student Marks Example.........................#

marks = np.array([45, 67, 78, 89, 92, 55, 73])

print("Marks:", marks)

print("Average Marks:", np.mean(marks))

print("Median Marks:", np.median(marks))

print("Highest Marks:", np.max(marks))

print("Lowest Marks:", np.min(marks))

print("Total Marks:", np.sum(marks))

print("Standard Deviation:", np.std(marks))


# .........................Practical Sales Example.........................#

sales = np.array([1200, 2500, 1800, 3200, 4500, 2100])

average_sales = np.mean(sales)

highest_sales = np.max(sales)

lowest_sales = np.min(sales)

total_sales = np.sum(sales)

print("Average Sales:", average_sales)

print("Highest Sales:", highest_sales)

print("Lowest Sales:", lowest_sales)

print("Total Sales:", total_sales)
