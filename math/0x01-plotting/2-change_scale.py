#!/usr/bin/env python3
import numpy as np
import matplotlib.pyplot as plt

x = np.arange(0, 28651, 5730)
r = np.log(0.5)
t = 5730
y = np.exp((r / t) * x)

# your code here
fig = plt.figure(figsize=(8, 8))
plt.plot(x, y)
plt.yscale("log") # logarithmically scaled
plt.xlim([0, 28650]) # Change range axis x
plt.title('Exponential Decay of C-14', fontsize=14)
plt.xlabel('Time (years)', fontsize=10)
plt.ylabel('Fraction Remaining', fontsize=10)
plt.show()