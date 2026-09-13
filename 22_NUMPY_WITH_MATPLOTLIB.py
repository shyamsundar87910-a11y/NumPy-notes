# ===================== 22_NUMPY_WITH_MATPLOTLIB.py =====================


import numpy as np
import matplotlib.pyplot as plt


# .........................Basic NumPy Data With Matplotlib.........................#

arr = np.array([10, 20, 30, 40, 50])

plt.plot(arr)

plt.show()


# .........................X and Y Values.........................#

x = np.array([1, 2, 3, 4, 5])

y = np.array([10, 20, 30, 40, 50])

plt.plot(x, y)

plt.show()


# .........................Line Graph.........................#

months = np.array([1, 2, 3, 4, 5, 6])

sales = np.array([1000, 1500, 1200, 1800, 2200, 2500])

plt.plot(months, sales)

plt.xlabel("Month")

plt.ylabel("Sales")

plt.title("Monthly Sales")

plt.show()


# .........................Bar Chart.........................#

products = np.array(["Laptop", "Phone", "Tablet", "Watch"])

sales = np.array([50000, 30000, 20000, 10000])

plt.bar(products, sales)

plt.xlabel("Products")

plt.ylabel("Sales")

plt.title("Product Sales")

plt.show()


# .........................Scatter Plot.........................#

hours = np.array([1, 2, 3, 4, 5, 6])

marks = np.array([40, 50, 60, 70, 80, 90])

plt.scatter(hours, marks)

plt.xlabel("Study Hours")

plt.ylabel("Marks")

plt.title("Study Hours vs Marks")

plt.show()


# .........................Histogram.........................#

marks = np.array([45, 50, 55, 60, 65, 70, 75, 80, 85, 90])

plt.hist(marks)

plt.xlabel("Marks")

plt.ylabel("Students")

plt.title("Marks Distribution")

plt.show()


# .........................Random Data Graph.........................#

x = np.arange(1, 11)

y = np.random.randint(10, 100, 10)

plt.plot(x, y)

plt.xlabel("X Values")

plt.ylabel("Random Values")

plt.title("Random Data")

plt.show()


# .........................NumPy Mathematical Function Graph.........................#

x = np.linspace(0, 10, 100)

y = np.sin(x)

plt.plot(x, y)

plt.xlabel("X")

plt.ylabel("Sin(X)")

plt.title("Sine Wave")

plt.show()


# .........................Multiple Data Points.........................#

x = np.array([1, 2, 3, 4, 5])

sales = np.array([20, 35, 30, 45, 50])

profit = np.array([5, 10, 8, 15, 20])

plt.plot(x, sales, label="Sales")

plt.plot(x, profit, label="Profit")

plt.xlabel("Month")

plt.ylabel("Amount")

plt.title("Sales and Profit")

plt.legend()

plt.show()


# .........................Practical Data Analysis Example.........................#

days = np.array([1, 2, 3, 4, 5, 6, 7])

website_visitors = np.array([120, 180, 150, 220, 300, 280, 350])

plt.plot(days, website_visitors)

plt.xlabel("Days")

plt.ylabel("Visitors")

plt.title("Website Visitors")

plt.show()
