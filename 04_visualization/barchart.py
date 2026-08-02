"""
bar_chart.py
Creating bar charts
"""

import matplotlib.pyplot as plt

languages = ["Python", "Java", "C++", "JavaScript"]
students = [40, 25, 15, 30]

plt.bar(languages, students)

plt.title("Students by Programming Language")
plt.xlabel("Language")
plt.ylabel("Students")

plt.show()