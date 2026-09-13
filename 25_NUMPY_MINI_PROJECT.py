# ===================== 25_NUMPY_MINI_PROJECT.py =====================


import numpy as np


# .........................Student Data.........................#

students = np.array([
    "Aman",
    "Rahul",
    "Rohit",
    "Vikas",
    "Ankit",
    "Priya",
    "Neha",
    "Pooja"
])

marks = np.array([
    65,
    78,
    92,
    35,
    88,
    72,
    45,
    96
])


# .........................Display Data.........................#

print("Students:", students)

print("Marks:", marks)


# .........................Total Students.........................#

total_students = students.size

print("Total Students:", total_students)


# .........................Total Marks.........................#

total_marks = np.sum(marks)

print("Total Marks:", total_marks)


# .........................Average Marks.........................#

average_marks = np.mean(marks)

print("Average Marks:", average_marks)


# .........................Highest Marks.........................#

highest_marks = np.max(marks)

print("Highest Marks:", highest_marks)


# .........................Lowest Marks.........................#

lowest_marks = np.min(marks)

print("Lowest Marks:", lowest_marks)


# .........................Highest Marks Student.........................#

highest_position = np.argmax(marks)

print("Top Student:", students[highest_position])

print("Top Marks:", marks[highest_position])


# .........................Lowest Marks Student.........................#

lowest_position = np.argmin(marks)

print("Lowest Student:", students[lowest_position])

print("Lowest Marks:", marks[lowest_position])


# .........................Passed Students.........................#

passed = marks >= 40

print("Passed Students:", students[passed])

print("Passed Marks:", marks[passed])


# .........................Failed Students.........................#

failed = marks < 40

print("Failed Students:", students[failed])

print("Failed Marks:", marks[failed])


# .........................Above Average Students.........................#

above_average = marks > average_marks

print("Above Average Students:", students[above_average])

print("Above Average Marks:", marks[above_average])


# .........................Below Average Students.........................#

below_average = marks < average_marks

print("Below Average Students:", students[below_average])

print("Below Average Marks:", marks[below_average])


# .........................Sort Marks.........................#

sorted_marks = np.sort(marks)

print("Sorted Marks:", sorted_marks)


# .........................Descending Marks.........................#

descending_marks = np.sort(marks)[::-1]

print("Descending Marks:", descending_marks)


# .........................Median Marks.........................#

median_marks = np.median(marks)

print("Median Marks:", median_marks)


# .........................Standard Deviation.........................#

standard_deviation = np.std(marks)

print("Standard Deviation:", standard_deviation)


# .........................Percentage Calculation.........................#

percentage = (marks / 100) * 100

print("Percentage:", percentage)


# .........................Grade Calculation.........................#

grades = np.where(
    marks >= 90, "A",
    np.where(
        marks >= 75, "B",
        np.where(
            marks >= 60, "C",
            np.where(marks >= 40, "D", "F")
        )
    )
)

print("Grades:", grades)


# .........................Student Report.........................#

print("\nStudent Report")

for i in range(total_students):

    print(
        students[i],
        "- Marks:",
        marks[i],
        "- Grade:",
        grades[i]
    )


# .........................Class Performance.........................#

pass_count = np.sum(marks >= 40)

fail_count = np.sum(marks < 40)

print("\nClass Performance")

print("Passed:", pass_count)

print("Failed:", fail_count)

print("Pass Percentage:", (pass_count / total_students) * 100)


# .........................Final Analysis.........................#

print("\nFinal Analysis")

print("Total Students:", total_students)

print("Average Marks:", average_marks)

print("Highest Marks:", highest_marks)

print("Lowest Marks:", lowest_marks)

print("Median Marks:", median_marks)

print("Standard Deviation:", standard_deviation)

print("Top Student:", students[highest_position])

print("Lowest Student:", students[lowest_position])
