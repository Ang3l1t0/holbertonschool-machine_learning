#!/usr/bin/env python3
import numpy as np
import matplotlib.pyplot as plt

x = np.arange(0, 21000, 1000)
r = np.log(0.5)
t1 = 5730
t2 = 1600
y1 = np.exp((r / t1) * x)
y2 = np.exp((r / t2) * x)

# your code here
fig = plt.figure(figsize=(15, 8))
plt.plot(x, y1, color="red", linestyle="--", label="C-14")
plt.plot(x, y2, color="green", linestyle="-", label="Ra-226")
plt.xlim([0, 20000]) # Change range axis x
plt.ylim([0, 1]) # Change range axis x
plt.title('Exponential Decay of Radioactive Elements', fontsize=14)
plt.xlabel('Time (years)', fontsize=10)
plt.ylabel('Fraction Remaining', fontsize=10)
plt.legend(loc="best", fontsize="small")
plt.show()