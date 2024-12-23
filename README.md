# Gaussian Elimination - Numerical Methods Project

## Table of Contents
- [Project Description](#project-description)
- [Tools and Technologies](#tools-and-technologies)
- [Key Concepts](#key-concepts)
- [Kanban Board](#kanban-board)
- [Installation](#installation)
- [Diagrams](#diagrams)
- [Known Issues](#known-issues)
- [To-Do Items](#to-do-items)

## Project Description
This project implements the **Gaussian Elimination** algorithm for solving systems of linear equations in **Python**, **C++**, and **MATLAB**. It includes modules for core functionality, matrix manipulation, input validation, and optional visualization of matrix transformations. The project is designed to provide a clear and efficient implementation of the algorithm while allowing for easy comparison of results and performance across different programming languages.

Key features:
- **Core algorithm**: Gaussian Elimination with forward elimination and back substitution.
- **Helper functions**: Matrix creation, validation, and singularity check.
- **Visualization**: Optional module for visualizing matrix transformations.
- **Unit testing**: Comprehensive test suite to validate correctness and handle edge cases.
- **Multi-language implementation**: Code re-implemented in Python, C++, and MATLAB for cross-platform comparisons.
- **Software Development**: Agile methodology used for iterative development and improvement.

## Project Objectives

- Implement the Gaussian Elimination algorithm in Python, C++, and MATLAB to solve systems of linear equations.
- Compare the performance and accuracy of the implementations across different programming languages.
- Use numerical analysis techniques to enhance the robustness of the algorithm, including pivoting, error handling, and matrix validation.
- Incorporate visualization tools to help better understand the matrix transformations and system behavior.

## Tools and Technologies

- **Python**: Main programming language used for this project.
- **C++**: For a low-level implementation to compare performance with Python.
- **MATLAB**: Used for symbolic math, solving linear equations, and visualizations.
- **Anaconda**: Environment management and package distribution for Python.
- **MATLAB IDE**: For coding and running MATLAB-specific implementations.
- **Unit Test Frameworks**: Used in Python and C++ to ensure correctness.

## Key Concepts

- **Gaussian Elimination**: A method for solving systems of linear equations using forward elimination and back substitution.
  
- **Pivoting**: A technique used to reduce numerical instability when solving linear systems.

- **Matrix Operations**: Understanding how to manipulate matrices (e.g., row operations, determinant calculation) is essential to Gaussian Elimination.

- **Numerical Analysis**: Techniques to handle error propagation, matrix singularity, and optimization of the algorithm for large systems.

- **Visualization**: Use of visual tools to understand the behavior of the system and transformations during Gaussian elimination.

## Installation

1. **Install Anaconda**: Download and install [Anaconda](https://www.anaconda.com/products/distribution) for the Python environment management and package distribution.
2. **Install MATLAB**: Download and install [MATLAB](https://www.mathworks.com/products/matlab.html) to compare and implement MATLAB-specific functionalities.
3. **Install necessary Python libraries**:
   ```bash
   conda install numpy scipy matplotlib
   ```
Or if using Pip:
  ```bash
  pip install numpy scipy matplotlib
  ```
4. **Install a C++ compiler (for C++ implementation)**:
  - **Windows**: Install MinGW or Visual Studio Build Tools.
  - **Linux**: GCC or Clang.
  - **macOS**: Xcode command line tools.

## Diagrams

### UML Use Case Diagram

```bash
+-----------------------------------+
|      Gaussian Elimination System  |
+-----------------------------------+
|                                   |
|  +-----------------------------+  |
|  |      User Interface          |  |
|  +-----------------------------+  |
|           /           \           |
|          /             \          |
|   +-------------+  +-------------+ |
|   | Input Matrix|  | View Output | |
|   | and Options |  |   Results   | |
|   +-------------+  +-------------+ |
|                                   |
+-----------------------------------+
```
### UML Class Diagram

```bash
+----------------------------+
|     GaussianElimination    |
+----------------------------+
| - matrix: list             |
| - num_rows: int            |
| - num_cols: int            |
+----------------------------+
| + __init__()               |
| + validate_matrix()        |
| + gaussian_elimination()   |
| + back_substitution()      |
| + check_singularity()      |
| + visualize()              |
| + save_results()           |
+----------------------------+
```

### UML Sequence Diagram

```bash
User              System                GaussianElimination
 |                   |                           |
 |--- Input Matrix ->|                           |
 |                   |--- validate_matrix()      |
 |                   |--- gaussian_elimination() |
 |                   |--- back_substitution()    |
 |                   |--- check_singularity()    |
 |                   |                           |
 |--- View Results ->|--- visualize()            |
 |                   |--- save_results()         |
 |                   |                           |

```
## Known Issues

  - Floating-point precision: Numerical instability may occur for poorly conditioned systems, leading to inaccurate results.
  - MATLAB Integration: MATLAB integration with Python might cause compatibility issues. Integration is optional but recommended for comparison.
  - Large Systems: For very large systems, performance might degrade, and memory limits may be reached.
    
## To-Do Items

  1. Re-implement code into MATLAB for a comparison of results.
  2. Implement and refine the visualization module to graphically represent matrix transformations.
  3. Implement unit and integration testing for the Python code and C++ implementations.
  4. Optimize the algorithm to handle larger systems efficiently.

## Credits
Troy Chin (Project Lead/Developer)

## License
This project is free to use under the GNU GPLv3 License: [https://www.gnu.org/licenses/gpl-3.0.en.html]([url](https://www.gnu.org/licenses/gpl-3.0.en.html))
