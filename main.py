# 3, 11, 31, 69, 131, 223

'''
Matrix ile cozum denicem
Bu programlari anlamayi denicem
Sifre cozucu ASCII numaralari kullanilarak yapilabilir
Bu matrixin cozulebilirligi nereden biliniyor

Program crashes when I give 0, 0, 0, 0, 0 !!!
'''

from sympy import symbols, Eq, solve

def pyramid_maker(sequence):
    # Define the pyramid as a list of lists
    pyramid = [sequence]
    
    # Build the pyramid with proper floating-point arithmetic
    while len(pyramid[-1]) > 1:
        current_row = pyramid[-1]
        # Use round to handle floating point precision issues
        next_row = [round(current_row[i + 1] - current_row[i], 6) for i in range(len(current_row) - 1)]
        if next_row == pyramid[-1][-len(next_row):]:
            break
        pyramid.append(next_row)

    # Print the pyramid with proper formatting
    for row in pyramid:
        formatted_row = " ".join([f"{x:8.3f}" for x in row])
        print(formatted_row.center(80))

    # Check if the bottom row of the pyramid contains only 0's
    # if not all(x == 0 for x in pyramid[-1]):
    #     return "Couldn't find the function, please provide more data"

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

def coefficient_calculation_loop(H, J, P, K, L=2):
    result = 0

    for i in range(K + 1):
        coefficient = (-1) ** i * comb(H, i)
        term = coefficient * (L * (H - i) + P) ** J
        result += term

    return result

def calculate_variables(variables, K, P, L):

    pivot = []
    for J in range(K, -1, -1):
        temp_list = []
        for H in range(K, -1, -1):
            r = coefficient_calculation_loop(H, J, P, K, L)
            temp_list.append(r)
        pivot.append(temp_list)

    symbols_str = " ".join([f"n{i}" for i in range(len(variables))])
    symbols_tuple = symbols(symbols_str)

    equations = []
    for i, (key, value) in enumerate(variables.items()):
        equation = value
        for j in range(i + 1):
            equation -= symbols_tuple[j] * pivot[j][i]
        equations.append(Eq(equation, 0))

    sol = solve(equations, symbols_tuple)

    # Round the coefficients to 6 decimal places and clean up near-zero values
    cleaned_coefficients = {}
    for i in range(len(variables)):
        value = float(sol[symbols_tuple[i]])
        # If the value is very close to a whole number, round it
        if abs(value - round(value)) < 1e-10:
            value = round(value)
        # If the value is very close to zero, make it zero
        elif abs(value) < 1e-10:
            value = 0
        else:
            value = round(value, 6)
        cleaned_coefficients[f"n{i}"] = value

    return cleaned_coefficients

# Menu
print("Welcome to the polynomial sequence finder!")
print("Please enter your sequence of numbers, separated by commas:")

sequence = input().split(",")
sequence = [float(x) for x in sequence]

print("\nYou entered the sequence:", sequence)
P = float(input("Enter the starting value: "))
L = float(input("Enter the difference interval between the values: "))
print("")

result = pyramid_maker(sequence)

if isinstance(result, tuple):
    K, variables = result
    # Construct the polynomial outline using n0, n1, n2, ...
    polynomial = "P(x) = "
    for i in range(K):
        polynomial += "n{}x^{} + ".format(i, K - i)
    polynomial += "n{}".format(K + 1)

    print("")
    print("variables =", variables)
    print("K =", K)
    print(polynomial)

    coefficents = calculate_variables(variables, K, P, L)
    print(coefficents)
    polynomial = "Key = P(x) = "
    for i in range(K):
        coeff = coefficents[f'n{i}']
        # Only add term if coefficient is not zero
        if coeff != 0:
            if coeff == 1:
                polynomial += f"x^{K-i} + "
            elif coeff == -1:
                polynomial += f"-x^{K-i} + "
            else:
                polynomial += f"{coeff}x^{K-i} + "
    polynomial += f"{coefficents[f'n{K}']}"
    print("")
    print(polynomial)
else:
    print(result)
