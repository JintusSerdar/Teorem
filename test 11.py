import time

start_time = time.perf_counter()
def pyramid_maker(sequence):

    # Define the pyramid as a list of lists
    pyramid = [sequence]

    # Build the pyramid
    while len(pyramid[-1]) > 1:
        current_row = pyramid[-1]
        next_row = [current_row[i + 1] - current_row[i] for i in range(len(current_row) - 1)]
        if next_row == pyramid[-1][-len(next_row):]:
            break
        pyramid.append(next_row)

    # Check if the bottom row of the pyramid contains only 0's
    if not all(x == 0 for x in pyramid[-1]):
        return "Couldn't find the function, please provide more data"

    # Extract the left lane numbers
    left_lane = [pyramid[i][0] for i in range(len(pyramid)) if i != len(pyramid) - 1 or pyramid[i][0] != 0]

    # Assign the left lane numbers to variables a0, a1, a2, ...
    K = len(left_lane) - 1
    variables = {}
    for i in range(K + 1):
        variables["a{}".format(i)] = left_lane[-(i + 1)]

    # Return the variables dictionary and K
    return (K, variables)

def comb(n, k):
    result = 1

    for i in range(1, k+1):
        result *= n - k + i
        result //= i

    return result

def coefficient_calculation_loop(H, J, P, K, L=0):
    result = 0

    for i in range(K + 1):
        coefficient = (-1) ** i * comb(H + L, i)
        term = coefficient * (H + P - i) ** J
        result += term

    return result

def solve_linear_system(A, b):
    n = len(A)

    # Gaussian elimination
    for i in range(n):
        pivot = A[i][i]
        for j in range(i+1, n):
            factor = A[j][i] / pivot
            for k in range(i, n):
                A[j][k] -= factor * A[i][k]
            b[j] -= factor * b[i]

    # Backward substitution
    x = [0] * n
    for i in range(n-1, -1, -1):
        x[i] = b[i]
        for j in range(i+1, n):
            x[i] -= A[i][j] * x[j]
        x[i] /= A[i][i]

    return x

def calculate_variables(variables, K, P):
    pivot = []
    for J in range(K, -1, -1):
        temp_list = []
        for H in range(K, -1, -1):
            r = coefficient_calculation_loop(H, J, P, K)
            temp_list.append(r)
        pivot.append(temp_list)

    # Construct the coefficient matrix and the constant vector
    A = []
    b = []
    for i in range(K + 1):
        temp_list = []
        for j in range(K + 1):
            temp_list.append(pivot[j][i])
        A.append(temp_list)
        b.append(variables[f'a{i}'])

    # Solve the linear system using matrix operations
    x = solve_linear_system(A, b)
    print(x)
    # Print the solution
    solution = {f'n{i}': x[i] for i in range(K + 1)}

    return solution


sequence = [1, 2, 3, 4, 5, 6]

P = 1

result = pyramid_maker(sequence)

if isinstance(result, tuple):
    K, variables = result
    # Construct the polynomial outline using n0, n1, n2, ...

    coefficents = calculate_variables(variables, K, P)
    print(coefficents)
 
end_time = time.perf_counter()

print("Execution time:", end_time - start_time)