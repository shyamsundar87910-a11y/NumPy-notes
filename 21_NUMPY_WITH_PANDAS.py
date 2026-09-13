# ===================== 21_NUMPY_WITH_PANDAS.py =====================


import numpy as np
import pandas as pd


# .........................NumPy Array to Pandas Series.........................#

arr = np.array([10, 20, 30, 40, 50])

series = pd.Series(arr)

print(series)


# .........................Pandas Series to NumPy Array.........................#

series = pd.Series([10, 20, 30, 40, 50])

arr = series.to_numpy()

print(arr)


# .........................NumPy Array to DataFrame.........................#

arr = np.array([
    [10, 20, 30],
    [40, 50, 60],
    [70, 80, 90]
])

df = pd.DataFrame(arr)

print(df)


# .........................DataFrame to NumPy Array.........................#

df = pd.DataFrame({
    "Name": ["Aman", "Rahul", "Rohit"],
    "Marks": [78, 85, 92]
})

arr = df.to_numpy()

print(arr)


# .........................NumPy Array With Column Names.........................#

arr = np.array([
    ["Aman", 78],
    ["Rahul", 85],
    ["Rohit", 92]
])

df = pd.DataFrame(arr, columns=["Name", "Marks"])

print(df)


# .........................NumPy Calculations in DataFrame.........................#

df = pd.DataFrame({
    "Name": ["Aman", "Rahul", "Rohit", "Vikas"],
    "Marks": [65, 78, 90, 55]
})

marks = df["Marks"].to_numpy()

print("Average:", np.mean(marks))

print("Highest:", np.max(marks))

print("Lowest:", np.min(marks))


# .........................Adding NumPy Calculated Column.........................#

df = pd.DataFrame({
    "Name": ["Aman", "Rahul", "Rohit"],
    "Marks": [65, 78, 90]
})

marks = df["Marks"].to_numpy()

df["Bonus"] = marks + 5

print(df)


# .........................NumPy Filtering With Pandas.........................#

df = pd.DataFrame({
    "Name": ["Aman", "Rahul", "Rohit", "Vikas"],
    "Marks": [35, 78, 90, 32]
})

marks = df["Marks"].to_numpy()

passed = df[marks >= 40]

print(passed)


# .........................NumPy Sorting With Pandas.........................#

df = pd.DataFrame({
    "Name": ["Aman", "Rahul", "Rohit", "Vikas"],
    "Marks": [65, 90, 45, 78]
})

marks = df["Marks"].to_numpy()

sorted_marks = np.sort(marks)

print(sorted_marks)


# .........................NumPy Mean for DataFrame Column.........................#

df = pd.DataFrame({
    "Product": ["Laptop", "Phone", "Tablet", "Watch"],
    "Sales": [50000, 30000, 20000, 10000]
})

sales = df["Sales"].to_numpy()

average_sales = np.mean(sales)

print("Average Sales:", average_sales)


# .........................NumPy Maximum and Minimum.........................#

df = pd.DataFrame({
    "Product": ["Laptop", "Phone", "Tablet", "Watch"],
    "Sales": [50000, 30000, 20000, 10000]
})

sales = df["Sales"].to_numpy()

print("Maximum Sales:", np.max(sales))

print("Minimum Sales:", np.min(sales))


# .........................NumPy Standard Deviation.........................#

df = pd.DataFrame({
    "Marks": [45, 67, 78, 89, 92]
})

marks = df["Marks"].to_numpy()

result = np.std(marks)

print("Standard Deviation:", result)


# .........................Practical Data Analysis Example.........................#

df = pd.DataFrame({
    "Product": ["Laptop", "Phone", "Tablet", "Watch", "Camera"],
    "Sales": [55000, 30000, 22000, 15000, 40000]
})

sales = df["Sales"].to_numpy()

df["Sales After 10% Increase"] = sales * 1.10

print(df)

print("Average Sales:", np.mean(sales))

print("Highest Sales:", np.max(sales))

print("Lowest Sales:", np.min(sales))

print("Total Sales:", np.sum(sales))
