#!/usr/bin/env python3
import numpy as np
import matplotlib.pyplot as plt

np.random.seed(5)
fruit = np.random.randint(0, 20, (4,3))

# your code here
fig = plt.figure(figsize=(8, 10), dpi= 70)
plt.subplots_adjust(hspace = 0.5)

x = ['Farrah', 'Fred', 'Felicia']
w= 0.5

plt.bar(x, fruit[0], w, color='red')
plt.bar(x, fruit[1], w, bottom=fruit[0], color='yellow')
plt.bar(x, fruit[2], w, bottom=fruit[0]+fruit[1], color='#ff8000')
plt.bar(x, fruit[3], w, bottom=fruit[2] + fruit[1] + fruit[0]  , color='#ffe5b4')
plt.axis([None, None, 0, 80])

plt.legend(["apples", "bananas", "oranges", "peaches"])

plt.ylabel("Quantity of Fruit")
plt.title("Number of Fruit per Person")
plt.show()