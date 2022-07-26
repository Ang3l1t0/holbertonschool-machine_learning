#!/usr/bin/env python3
import numpy as np
import matplotlib.pyplot as plt
from pylab import xticks

np.random.seed(5)
student_grades = np.random.normal(68, 15, 50)

# your code here
fig = plt.figure(figsize=(13, 8), dpi=70)
plt.hist(student_grades, bins=10, edgecolor='black', align='mid')
xticks(range(0,100, 10))
plt.ylim([0, 30]) # Change range axis x
plt.title('Project A', fontsize=14)
plt.ylabel('Number of Students',  fontsize=10)
plt.xlabel('Grades',  fontsize=10)
plt.show()