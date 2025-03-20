import numpy as np

def calculate_coefficients(sequence):
    n = len(sequence)
    forward_diff = np.zeros((n, n))
    forward_diff[0] = sequence

    for i in range(1, n):
        for j in range(n-i):
            forward_diff[i][j] = forward_diff[i-1][j+1] - forward_diff[i-1][j]

    for i in range(n-1):
        if np.unique(forward_diff[i+1]).size == 1:
            order = i+1
            break

    A = np.zeros((order, order))
    B = np.zeros((order, 1))
    for i in range(order):
        for j in range(order):
            A[i][j] = (i+1)**j
        B[i][0] = sequence[i]

    X = np.linalg.solve(A, B)
    coefficients = X.flatten()

    return coefficients[::-1]

sequence = [1, 3, 11, 31, 69, 131, 223]
coefficients = calculate_coefficients(sequence)
print(coefficients)