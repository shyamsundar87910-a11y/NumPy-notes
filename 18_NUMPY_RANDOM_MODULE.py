# ===================== 18_NUMPY_RANDOM_MODULE.py =====================


import numpy as np


# .........................Random Number.........................#

result = np.random.rand()

print(result)


# .........................Random Numbers.........................#

result = np.random.rand(5)

print(result)


# .........................Random 2D Array.........................#

result = np.random.rand(2, 3)

print(result)


# .........................Random Integer.........................#

result = np.random.randint(10)

print(result)


# .........................Random Integers.........................#

result = np.random.randint(1, 100, 5)

print(result)


# .........................Random Integer 2D Array.........................#

result = np.random.randint(1, 100, size=(3, 4))

print(result)


# .........................Random Choice.........................#

arr = np.array([10, 20, 30, 40, 50])

result = np.random.choice(arr)

print(result)


# .........................Multiple Random Choices.........................#

arr = np.array([10, 20, 30, 40, 50])

result = np.random.choice(arr, size=3)

print(result)


# .........................Random Choice Without Replacement.........................#

arr = np.array([10, 20, 30, 40, 50])

result = np.random.choice(arr, size=3, replace=False)

print(result)


# .........................Random Shuffle.........................#

arr = np.array([10, 20, 30, 40, 50])

np.random.shuffle(arr)

print(arr)


# .........................Random Seed.........................#

np.random.seed(10)

result = np.random.randint(1, 100, 5)

print(result)


# .........................Random Seed Same Result.........................#

np.random.seed(10)

arr1 = np.random.randint(1, 100, 5)

np.random.seed(10)

arr2 = np.random.randint(1, 100, 5)

print(arr1)

print(arr2)


# .........................Random Normal Distribution.........................#

result = np.random.normal(size=5)

print(result)


# .........................Normal Distribution With Mean and Standard Deviation.........................#

result = np.random.normal(50, 10, 5)

print(result)


# .........................Random 0 and 1 Values.........................#

result = np.random.randint(0, 2, 10)

print(result)


# .........................Random Student Marks.........................#

marks = np.random.randint(30, 101, 10)

print("Random Marks:", marks)


# .........................Random Sales Data.........................#

sales = np.random.randint(1000, 10000, 10)

print("Random Sales:", sales)


# .........................Random Data for Practice.........................#

data = np.random.randint(1, 100, size=(5, 3))

print("Random Data:")

print(data)


# .........................Practical Example.........................#

students = np.array(["Aman", "Rahul", "Rohit", "Vikas", "Ankit"])

random_student = np.random.choice(students)

print("Selected Student:", random_student)
