#!/usr/bin/env python3
import numpy as np
import matplotlib.pyplot as plt

mean = [69, 0]
cov = [[15, 8], [8, 15]]
np.random.seed(5)
x, y = np.random.multivariate_normal(mean, cov, 2000).T
y += 180

# your code here
fig = plt.figure(figsize=(8, 8))
plt.scatter(x, y, color='purple')
plt.title('Men\'s Height vs Weight', fontsize=14)
plt.xlabel('Height (in)', fontsize=10)
plt.ylabel('Weight (lbs)', fontsize=10)
plt.show()