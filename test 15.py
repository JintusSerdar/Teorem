# 3, 11, 31, 69, 131, 223

'''
Matrix ile cozum denicem
Bu programlari anlamayi denicem
Sifre cozucu ASCII numaralari kullanilarak yapilabilir
Bu matrixin cozulebilirligi nereden biliniyor
'''

from sympy import symbols, Eq, solve

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

    # Print the pyramid
    for row in pyramid:
        print(" ".join([str(x) for x in row]).center(50))

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

# 1.0x^6 + 30.0x^5 + 150.0x^4 + -840.0x^3 + -1920.0x^2 + 7592.0x^1 + -2256.0
# 729.0, 15625.0, 117649.0, 531441.0, 1771561.0, 4826809.0, 11390625.0

def coefficient_calculation_loop(H, J, P, K, L=2):
    result = 0

    for i in range(K + 1):
        coefficient = (-1) ** (H - i) * comb(H, i)
        term = coefficient * (P + L * i) ** J
        result += term

    return result

def calculate_variables(variables, K, P):

    pivot = []
    for J in range(K, -1, -1):
        temp_list = []
        for H in range(K, -1, -1):
            r = coefficient_calculation_loop(H, J, P, K)
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

    return {f"n{i}": float(sol[symbols_tuple[i]]) for i in range(len(variables))}

# Menu
print("Welcome to the polynomial sequence finder!")
print("Please enter your sequence of numbers, separated by commas:")

sequence = input().split(",")
sequence = [float(x) for x in sequence]

print("\nYou entered the sequence:", sequence)
P = int(input("Enter the starting value: "))
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

    coefficents = calculate_variables(variables, K, P)
    print(coefficents)
    polynomial = "Key = P(x) = "
    for i in range(K):
        polynomial += "{}x^{} + ".format(coefficents['n{}'.format(i)], K - i)
    polynomial += "{}".format(coefficents['n{}'.format(K)])
    print("")
    print(polynomial)
else:
    print(result)
