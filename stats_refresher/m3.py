"""Playing around with Mean, Median, and Mode with NumPy."""

import numpy as np
from scipy import stats

# Create a fake dataset of 10,000 peoples' salaries
incomes = np.random.normal(27000, 15000, 10000)

# Mean should be about $27k
mean_of_incomes = np.mean(incomes)
print("Mean (before):", mean_of_incomes)

# Median should be about $27k
median_of_incomes = np.median(incomes)
print("Median (before):", median_of_incomes)

# Add an outlier...
incomes = np.append(incomes, [1000000000])

print()
print("Mean (after):", np.mean(incomes))
print("Median (after):", np.median(incomes))

# Create a fake dataset of ages for 500 people
ages = np.random.randint(18, high=90, size=500)
print("Mode:", stats.mode(ages))