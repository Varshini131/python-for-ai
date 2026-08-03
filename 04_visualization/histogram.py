"""
histogram.py
Creating histograms
"""

import matplotlib.pyplot as plt
import numpy as np

marks = np.random.randint(40, 100, 100)

plt.hist(marks, bins=10)

plt.title("Marks Distribution")
plt.xlabel("Marks")
plt.ylabel("Frequency")

plt.show()