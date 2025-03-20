import psutil


from sympy import symbols, Eq, solve

def pyramid_maker(sequence):

    pyramid = [sequence]

    while len(pyramid[-1]) > 1:
        current_row = pyramid[-1]
        next_row = [current_row[i + 1] - current_row[i] for i in range(len(current_row) - 1)]
        if next_row == pyramid[-1][-len(next_row):]:
            break
        pyramid.append(next_row)

    left_lane = [pyramid[i][0] for i in range(len(pyramid)) if i != len(pyramid) - 1 or pyramid[i][0] != 0]

    K = len(left_lane) - 1
    variables = {}
    for i in range(K + 1):
        variables["a{}".format(i)] = left_lane[-(i + 1)]

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


sequence = [1, 3, 8, 10]

P = 3

result = pyramid_maker(sequence)

if isinstance(result, tuple):
    K, variables = result
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

process = psutil.Process()
print("Memory usage:", process.memory_info().rss / 1024 / 1024, "MB")
