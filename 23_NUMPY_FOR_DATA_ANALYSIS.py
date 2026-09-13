# ===================== 23_NUMPY_FOR_DATA_ANALYSIS.py =====================


import numpy as np


# .........................Create Sales Data.........................#

sales = np.array([1200, 2500, 1800, 3200, 4500, 2100, 5000])

print("Sales:", sales)


# .........................Total Sales.........................#

total_sales = np.sum(sales)

print("Total Sales:", total_sales)


# .........................Average Sales.........................#

average_sales = np.mean(sales)

print("Average Sales:", average_sales)


# .........................Highest Sales.........................#

highest_sales = np.max(sales)

print("Highest Sales:", highest_sales)


# .........................Lowest Sales.........................#

lowest_sales = np.min(sales)

print("Lowest Sales:", lowest_sales)


# .........................Sales Above Average.........................#

above_average = sales[sales > average_sales]

print("Above Average Sales:", above_average)


# .........................Sales Below Average.........................#

below_average = sales[sales < average_sales]

print("Below Average Sales:", below_average)


# .........................Count Sales Values.........................#

count = sales.size

print("Number of Sales:", count)


# .........................Sort Sales.........................#

sorted_sales = np.sort(sales)

print("Sorted Sales:", sorted_sales)


# .........................Highest Sales Position.........................#

highest_position = np.argmax(sales)

print("Highest Sales Position:", highest_position)


# .........................Lowest Sales Position.........................#

lowest_position = np.argmin(sales)

print("Lowest Sales Position:", lowest_position)


# .........................Sales Difference.........................#

difference = np.max(sales) - np.min(sales)

print("Sales Difference:", difference)


# .........................Percentage Calculation.........................#

target = 30000

percentage = (total_sales / target) * 100

print("Target Achievement:", percentage, "%")


# .........................Student Marks Analysis.........................#

marks = np.array([45, 67, 78, 89, 92, 55, 73, 88])

average_marks = np.mean(marks)

passed = marks[marks >= 40]

failed = marks[marks < 40]

highest_marks = np.max(marks)

lowest_marks = np.min(marks)

print("Average Marks:", average_marks)

print("Passed Marks:", passed)

print("Failed Marks:", failed)

print("Highest Marks:", highest_marks)

print("Lowest Marks:", lowest_marks)


# .........................Employee Salary Analysis.........................#

salary = np.array([25000, 30000, 28000, 40000, 35000, 45000])

average_salary = np.mean(salary)

high_salary = salary[salary > average_salary]

print("Average Salary:", average_salary)

print("Above Average Salary:", high_salary)


# .........................Monthly Sales Analysis.........................#

monthly_sales = np.array([
    12000,
    15000,
    18000,
    14000,
    22000,
    25000,
    20000,
    28000,
    30000,
    27000,
    32000,
    35000
])

print("Total Yearly Sales:", np.sum(monthly_sales))

print("Average Monthly Sales:", np.mean(monthly_sales))

print("Highest Monthly Sales:", np.max(monthly_sales))

print("Lowest Monthly Sales:", np.min(monthly_sales))


# .........................Find Months Above Average.........................#

average_sales = np.mean(monthly_sales)

above_average = monthly_sales[monthly_sales > average_sales]

print("Months Above Average:", above_average)


# .........................Practical Data Analysis Example.........................#

data = np.array([
    [100, 200, 300],
    [150, 250, 350],
    [200, 300, 400]
])

print("Data:")

print(data)

print("Total:", np.sum(data))

print("Average:", np.mean(data))

print("Maximum:", np.max(data))

print("Minimum:", np.min(data))
