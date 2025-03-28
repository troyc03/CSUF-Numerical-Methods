# Polynomial Interpolation Algorithms

This project implements various polynomial interpolation algorithms, including:

- Newton's Method
- Lagrange's Method
- Cubic Spline Interpolation
- Linear Interpolation

Each method provides a way to estimate the value of a function at points between known data points. The project also includes Python implementations of these algorithms and a simple usage guide to help you get started.

## Table of Contents

- [Introduction](#introduction)
- [Algorithms](#algorithms)
  - [Newton's Method](#newtons-method)
  - [Lagrange's Method](#lagranges-method)
  - [Cubic Spline Interpolation](#cubic-spline-interpolation)
  - [Linear Interpolation](#linear-interpolation)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)

## Introduction

Interpolation is a fundamental technique used in numerical analysis and data science for estimating unknown values of a function based on known values. This project implements four common methods for polynomial interpolation and provides functions to evaluate the interpolated polynomials at new points.

## Algorithms

### Newton's Method

Newton’s method constructs the interpolation polynomial incrementally using divided differences. It is efficient when adding new data points without recalculating the entire polynomial.

### Lagrange's Method

Lagrange's method builds the interpolation polynomial using Lagrange basis polynomials. It is simple and works well for small datasets but can be inefficient for large datasets due to its time complexity.

### Cubic Spline Interpolation

Cubic spline interpolation fits piecewise cubic polynomials between data points while ensuring smoothness at the boundaries and at the data points. It is especially useful for smoothing noisy data and providing a smooth curve.

### Linear Interpolation

Linear interpolation connects the data points with straight lines, making it the simplest form of interpolation. While it is fast and easy, it may not be accurate for more complex datasets.

## Usage

You can use the provided interpolation methods to estimate values at new points. Below is an example of how to use each method.

### Example

```python
# Import the interpolation functions
from interpolation import newton_interpolation, lagrange_interpolation, cubic_spline_interpolation, linear_interpolation

# Define some data points
x_values = [1, 2, 3, 4]
y_values = [1, 4, 9, 16]

# Choose an interpolation method
interpolator = newton_interpolation(x_values, y_values)

# Evaluate the interpolated polynomial at x = 2.5
result = interpolator(2.5)
print(f'Interpolated value at x = 2.5: {result}')
```

### Dependencies
To run the code, you may need to install the required Python dependencies.
```
pip install numpy
```
