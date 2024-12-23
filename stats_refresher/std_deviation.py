"""Playing around with standard deviation and variance."""

import numpy as np
import matplotlib.pyplot as plt

incomes = np.random.normal(100.0, 20.0, 10000)

print("Standard Deviation:", incomes.std())
print("Variance:", incomes.var())

plt.hist(incomes, 50)
plt.show()