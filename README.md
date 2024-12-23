# Numerical Integration Lab

## Table of Contents
- [Project Description](#project-description)
- [Tools and Technologies](#tools-and-technologies)
- [Key Concepts](#key-concepts)
- [Installation](#installation)
- [Implementation in MATLAB and C++](#implementation-in-matlab-and-c++)
- [Known Issues](#known-issues)
- [To-Do Items](#to-do-items)

---

## Project Description

This lab focuses on implementing and analyzing various numerical integration methods, such as Taylor Series approximations, Simpson's Rule, Monte Carlo Integration, Trapezoidal Rule, Romberg Integration, Midpoint Rule, and Gaussian Quadrature. The project demonstrates the application of these techniques in Python, MATLAB, and C++, enabling comparisons between the performance and accuracy of each language's implementation. 

## Tools and Technologies

- **Python**: Primary language for prototyping and testing integration algorithms.
- **MATLAB**: Used for numerical computation, visualization, and symbolic math capabilities.
- **C++**: Offers a high-performance implementation for numerical methods, especially useful for large-scale computations.
- **Anaconda**: For Python environment management and library installation.
- **Spyder**: IDE for Python development, particularly useful for scientific computing.
- **Visual Studio**: IDE for C++ development and debugging.
- **MATLAB R2023b**: For numerical and symbolic computation.

---

## Key Concepts

- **Taylor Series Approximations**: Expanding functions into infinite series to approximate definite integrals.
- **Simpson's Rule**: Utilizing parabolic segments to achieve accurate integral approximations.
- **Monte Carlo Integration**: A probabilistic method that estimates integrals using random sampling.
- **Trapezoidal Rule**: Approximating the region under the curve with trapezoids.
- **Romberg Integration**: Combining Trapezoidal Rule with Richardson extrapolation for higher accuracy.
- **Midpoint Rule**: Using the midpoint of intervals for integral approximation.
- **Gaussian Quadrature**: Leveraging orthogonal polynomials to achieve precision with fewer evaluations.

---

## Installation

1. **Python**:
   - Install [Anaconda](https://www.anaconda.com/products/distribution).
   - Install required Python libraries:
     ```bash
     conda install numpy scipy matplotlib
     ```

2. **MATLAB**:
   - Install [MATLAB](https://www.mathworks.com/products/matlab.html).
   - Use built-in functions such as `integral`, or implement custom scripts for numerical methods.

3. **C++**:
   - Install [Visual Studio](https://visualstudio.microsoft.com/visual-cpp/) or a preferred C++ compiler.
   - Use libraries like **Eigen** or **Boost.Math** for numerical computation if necessary.

---

## Implementation in MATLAB and C++

### MATLAB
MATLAB will include scripts/functions for:
- Simpson's Rule: Using loops and symbolic math to automate segment calculations.
- Monte Carlo Integration: Generating random points and estimating integral values.
- Gaussian Quadrature: Implementing predefined weights and nodes for various polynomial degrees.

### C++
C++ implementation focuses on high-performance calculations:
- **Simpson’s Rule**: Loop-based integration using arrays and precision tuning.
- **Monte Carlo Integration**: Efficient random number generation with libraries like `<random>`.
- **Gaussian Quadrature**: Manual calculation or leveraging numerical libraries like Boost.

Code in Python will serve as a prototype, and each method will be translated to MATLAB and C++ for consistency and performance comparison.

---

## File Structure

- Python:

```bash
numerical_integration_lab/
│
├── main.py                # Entry point of the project
├── integration_methods.py # Core implementations of integration methods
├── utils.py               # Helper utilities and error calculators
├── visualization.py       # Visualization functions
├── benchmarks.py          # Benchmarking performance and accuracy
├── tests.py               # Unit tests for the project
├── README.md              # Project documentation
├── requirements.txt       # Python dependencies
├── data/                  # Directory for sample data (if applicable)
└── outputs/               # Directory for results and visualizations
```

- MATLAB:
  
```bash
numerical_integration_lab/
│
├── main.m                 # Main script to drive the project
├── taylor_series.m        # Taylor Series implementation
├── simpsons_rule.m        # Simpson's Rule implementation
├── monte_carlo.m          # Monte Carlo integration implementation
├── trapezoidal_rule.m     # Trapezoidal Rule implementation
├── romberg_integration.m  # Romberg integration implementation
├── midpoint_rule.m        # Midpoint Rule implementation
├── gaussian_quadrature.m  # Gaussian Quadrature implementation
├── utils.m                # Utility functions
├── benchmarks.m           # Benchmarking functions
├── test_integration.m     # Unit tests for all methods
└── data/                  # Directory for input or sample data (if needed)
```

- C++:
  
```bash
numerical_integration_lab/
│
├── main.cpp                # Entry point of the program
├── integration_methods.h   # Header file for integration methods
├── integration_methods.cpp # Implementation of integration methods
├── utils.h                 # Header file for utility functions
├── utils.cpp               # Implementation of utility functions
├── benchmarks.cpp          # Benchmarking and performance evaluation
├── tests.cpp               # Unit tests for validation
├── CMakeLists.txt          # Build configuration file (if using CMake)
└── data/                   # Directory for sample data (if applicable)
```
---

## Known Issues

- **MATLAB-Python Integration**: Users might face challenges integrating MATLAB scripts with Python projects. Standalone execution is recommended.
- **Floating-Point Errors**: Precision issues may arise in C++ for methods with highly iterative calculations like Romberg or Gaussian Quadrature.

---

## To-Do Items

- **Implement unit tests** for Python, MATLAB, and C++ implementations to validate results across all methods.
- Compare performance metrics (e.g., execution time, accuracy) across the three languages.
- Add advanced numerical methods such as **adaptive quadrature** for further exploration.
- Refactor code for clarity and reusability, ensuring that Python functions can be translated to MATLAB and C++ easily.
- Document the differences in implementation approach and performance for Python, MATLAB, and C++.

---

#### Credits
Troy Chin (Project Lead & Developer)

##### License
This project is free for academic and research purposes. Distributed under the [GNU General Public License v3.0](https://www.gnu.org/licenses/gpl-3.0.en.html).
