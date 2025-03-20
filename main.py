# 3, 11, 31, 69, 131, 223
# 1, 32, 243, 1024, 3125, 7776, 16807
# 0.5, 16, 121.5, 512, 1562.5, 3888, 8403.5
# -1.5, 14, 119.5, 510, 1560.5, 3886, 8401.5
# 3, -8, -51, -144, -305
# 1, 64, 729, 4096, 15625, 46656, 117649, 262144
# 0.0, 2.0, 96.0, 972.0, 5120.0, 18750.0, 54432.0, 134456.0, 294912.0
# 0.0, 2.0, 94.0, 876.0, 4148.0, 13630.0, 35682.0, 80024.0, 160456.0 koydugumda buga giriyor
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
    if not all(x == 0 for x in pyramid[-1]):
        return "Couldn't find the function, please provide more data"

    # Extract the left lane numbers
    left_lane = [pyramid[i][0] for i in range(len(pyramid)) if pyramid[i][0] != 0]

    # Assign the left lane numbers to variables a0, a1, a2, ...
    K = len(left_lane) - 1
    variables = {}
    for i in range(K + 1):
        variables["a{}".format(i)] = left_lane[-(i + 1)]

    # Return the variables dictionary and K
    return (K, variables)

def coefficient_calculation_3(K, variables):
    """ This function can calculate up to polynomials with a maximum degree of 6
    using ready-made templates, which is a limited but easy method."""

    coefficents = {}
    for i in range(K + 1):
        coefficents["n{}".format(i)] = 0

    if K == 0:
        coefficents['n0'] = 1 * variables['a0']

    if K == 1:
        coefficents['n0'] = 1 * variables['a0']
        coefficents['n1'] = 1 * variables['a1'] - 1 * coefficents['n0']

    if K == 2:
        coefficents['n0'] = 1 * variables['a0'] / 2
        coefficents['n1'] = 1 * variables['a1'] - 3 * coefficents['n0']
        coefficents['n2'] = 1 * variables['a2'] - 1 * coefficents['n0'] - 1 * coefficents['n1']

    if K == 3:
        coefficents['n0'] = 1 * variables['a0'] / 6
        coefficents['n1'] = (1 * variables['a1'] - 12 * coefficents['n0']) / 2
        coefficents['n2'] = 1 * variables['a2'] - 7 * coefficents['n0'] - 3 * coefficents['n1']
        coefficents['n3'] = 1 * variables['a3'] - 1 * coefficents['n0'] - 1 * coefficents['n1'] - 1 * coefficents['n2']

    if K == 4:
        coefficents['n0'] = 1 * variables['a0'] / 24
        coefficents['n1'] = (1 * variables['a1'] - 60 * coefficents['n0']) / 6
        coefficents['n2'] = (1 * variables['a2'] - 50 * coefficents['n0'] - 12 * coefficents['n1']) / 2
        coefficents['n3'] = 1 * variables['a3'] - 15 * coefficents['n0'] - 7 * coefficents['n1'] - 3 * coefficents['n2']
        coefficents['n4'] = 1 * variables['a4'] - 1 * coefficents['n0'] - 1 * coefficents['n1'] - 1 * coefficents['n2'] - 1 * coefficents['n3']

    if K == 5:
        coefficents['n0'] = 1 * variables['a0'] / 120
        coefficents['n1'] = (1 * variables['a1'] - 360 * coefficents['n0']) / 24
        coefficents['n2'] = (1 * variables['a2'] - 390 * coefficents['n0'] - 60 * coefficents['n1']) / 6
        coefficents['n3'] = (1 * variables['a3'] - 180 * coefficents['n0'] - 50 * coefficents['n1'] - 12 * coefficents['n2']) / 2
        coefficents['n4'] = 1 * variables['a4'] - 31 * coefficents['n0'] - 15 * coefficents['n1'] - 7 * coefficents['n2'] - 3 * coefficents['n3']
        coefficents['n5'] = 1 * variables['a5'] - 1 * coefficents['n0'] - 1 * coefficents['n1'] - 1 * coefficents['n2'] - 1 * coefficents['n3'] - 1 * coefficents['n4']

    if K == 6:
        coefficents['n0'] = variables['a0'] / 720
        coefficents['n1'] = (variables['a1'] - 2520 * coefficents['n0']) / 120
        coefficents['n2'] = (variables['a2'] - 3360 * coefficents['n0'] - 360 * coefficents['n1']) / 24
        coefficents['n3'] = (variables['a3'] - 2100 * coefficents['n0'] - 390 * coefficents['n1'] - 60 * coefficents['n2']) / 6
        coefficents['n4'] = (variables['a4'] - 602 * coefficents['n0'] - 180 * coefficents['n1'] - 50 * coefficents['n2'] - 12 * coefficents['n3']) / 2
        coefficents['n5'] = variables['a5'] - 63 * coefficents['n0'] - 31 * coefficents['n1'] - 15 * coefficents['n2'] - 7 * coefficents['n3'] - 3 * coefficents['n4']
        coefficents['n6'] = variables['a6'] - coefficents['n0'] - coefficents['n1'] - coefficents['n2'] - coefficents['n3'] - coefficents['n4'] - coefficents['n5']

    return coefficents

# Menu
print("Welcome to the polynomial sequence finder!")
print("Please enter your sequence of numbers, separated by commas:")

sequence = input().split(",")
sequence = [float(x) for x in sequence]

print("\nYou entered the sequence:", sequence)
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

    coefficents = coefficient_calculation_3(K, variables)
    polynomial = "Key = P(x) = "
    for i in range(K):
        polynomial += "{}x^{} + ".format(coefficents['n{}'.format(i + 1)], K - i)
    polynomial += "{}".format(coefficents['n{}'.format(K)])
    print("")
    print(polynomial)
else:
    print(result)
