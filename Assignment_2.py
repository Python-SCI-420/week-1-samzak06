# PYTHON420 Week 1 Assignment 2
# Samuel Zakutney
# 5/29/20

import matplotlib.pyplot as plt
import numpy as np


# Line Graph
years = np.linspace(1950,2000,5)
cancer = 200
stroke = 200 - 3*(years - 1950)
heart_disease = 600 - 6*(years - 1950)
error = np.random.normal(size = years.shape)

fig, ax = plt.subplots()
ax.plot(years, heart_disease + 8*error, '--', label = 'Heart Disease')
ax.plot(years, cancer + 4*error, 'ro-', label = 'Cancer')
ax.plot(years, stroke + 3*error, 'g*-', label = 'Stroke')
ax.set_title('Death Rates from Various Causes in America, 1950-2000')
ax.set_xlabel('years')
ax.set_ylabel('Deaths per 100k')
ax.grid(True)
ax.legend(loc='upper right')
plt.show()

# Bar Graph
domain1 = ('Biomedical','Chemical','Civil','Computer','Electrical')
domain2 = ('Environmental','Geological/Mining','Material Sciences','Mechanical','Surveying')
domains = domain1 + domain2
y_axis = np.arange(len(domains))
salary = [95.09,114.47,93.72,117.84,101.6,92.64,98.42,96.93,92.8,66.44]
plt.barh(domains,salary,align = 'center',color = 'blue')
plt.xlabel('Salary (k$/year)')
plt.title('Mean Salary Across Engineering Fields in 2020')
plt.show()

# Scatter Plot
x,y = np.random.normal(size=(2,300))
plt.plot(x,y,'ro')
plt.xlabel('Position (nm)')
plt.ylabel('Position (nm)')
plt.title('White Blood Cell Distribution Across Hemocytometer')
plt.grid(True)
plt.show()