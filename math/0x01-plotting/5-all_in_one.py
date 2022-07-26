#!/usr/bin/env python3
import numpy as np
import matplotlib.pyplot as plt

y0 = np.arange(0, 11) ** 3

mean = [69, 0]
cov = [[15, 8], [8, 15]]
np.random.seed(5)
x1, y1 = np.random.multivariate_normal(mean, cov, 2000).T
y1 += 180

x2 = np.arange(0, 28651, 5730)
r2 = np.log(0.5)
t2 = 5730
y2 = np.exp((r2 / t2) * x2)

x3 = np.arange(0, 21000, 1000)
r3 = np.log(0.5)
t31 = 5730
t32 = 1600
y31 = np.exp((r3 / t31) * x3)
y32 = np.exp((r3 / t32) * x3)

np.random.seed(5)
student_grades = np.random.normal(68, 15, 50)

# your code here
figure, axis = plt.subplots(3,2,figsize=(20, 10))
figure.tight_layout(pad=4)
x= np.arange(0, 11)

axis[0, 0].plot(x, y0, color='red')

# For scatter men Height vs Weight
axis[0, 1].scatter(x1, y1)
axis[0, 1].set_title("Men\'s Height vs Weight")
axis[0, 1].set_xlabel("Height (in)")
axis[0, 1].set_ylabel("Weight (lbs)")

# Line - logarithmically scaled
axis[1, 0].plot(x2, y2)
axis[1, 0].set_title("Exponential Decay of C-14")
axis[1, 0].set_xlabel("Time (years)")
axis[1, 0].set_ylabel("Fraction Remaining")
  

# For Exponential Decay of Radioactive Elements
axis[1, 1].plot(x3, y31, color="red", linestyle="--", label="C-14")
axis[1, 1].plot(x3, y32, color="green", linestyle="-", label="Ra-226")
axis[1, 1].set_title("Exponential Decay of Radioactive Elements")
axis[1, 1].set_xlabel("Time (years)")
axis[1, 1].set_ylabel("Fraction Remaining")
axis[1, 1].axis(xmin=0,xmax=20000)
axis[1, 1].axis(ymin=0,ymax=1)
axis[1, 1].legend(loc="best", fontsize="small")


axis[2, 0].hist(student_grades, bins=10, edgecolor='black', align='mid')
axis[2, 0].set_title("Project A")
axis[2, 0].set_xlabel("Grades")
axis[2, 0].set_ylabel("Number of Students")

axis[2, 1].set_visible(False)

plt.show()