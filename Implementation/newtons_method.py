import numpy as np

def newtons_method(x_vals, y_vals):
    n = len(x_vals)
    divided_diff = [[0] * n for _ in range(n)]

    # Calculate divided differences
    for i in range(n):
        divided_diff[0][i] = y_vals[i]
        for j in range(1, n):
            for i in range(n - j):
                divided_diff[i][j] =  divided_diff[i][j] = (divided_diff[i+1][j-1] - divided_diff[i][j-1]) / (x_vals[i+j] - x_vals[i])

        # Build Newton polynomial
        def polynomial(x):
            result = divided_diff[0][0]
            for i in range(1, n):
                term = divided_diff[0][i]
                for j in range(i):
                    term *= (x - x_vals[j])
                    result += term
            return result
        
        return polynomial