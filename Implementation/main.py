from newtons_method import newtons_method
import numpy as np

# Define some data points
x_values = np.array([1, 2, 3, 4])
y_values = np.array([1, 4, 9, 16])

# Choose an interpolation method
interpolator = newtons_method(x_values, y_values)

# Evaluate the interpolated polynomial at x = 2.5
result = interpolator(2.5)
print(f'Interpolated value at x = 2.5: {result}')