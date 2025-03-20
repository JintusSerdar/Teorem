# 3, 11, 31, 69, 131, 223
# 1, 32, 243, 1024, 3125, 7776, 16807
# 0.5, 16, 121.5, 512, 1562.5, 3888, 8403.5
# -1.5, 14, 119.5, 510, 1560.5, 3886, 8401.5
# 3, -8, -51, -144, -305
# 1, 64, 729, 4096, 15625, 46656, 117649, 262144
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

    # Print the pyramid
    for row in pyramid:
        print(" ".join([str(x) for x in row]).center(50))

    # Extract the left lane numbers
    left_lane = [pyramid[i][0] for i in range(len(pyramid)) if pyramid[i][0] != 0]

    # Assign the left lane numbers to variables a1, a2, a3, ...
    K = len(left_lane) - 1
    variables = {}
    for i in range(K + 1):
        variables["a{}".format(i + 1)] = left_lane[-(i + 1)]

    # Return the variables dictionary and K
    return (K, variables)

def coefficient_calculation_3(K, variables):
    """ This function can calculate up to polynomials with a maximum degree of 6
    using ready-made templates, which is a limited but easy method."""
    print(variables)
    coefficients = {}
    for i in range(K + 1):
        coefficients[f"n{i + 1}"] = 0

    # Seperates n's from library
    for i in range(K + 1):
        exec("n{} = coefficients['n{}']".format(i + 1, i + 1))
    a1 = variables['a1']
    a2 = variables['a2']
    a3 = variables['a3']
    a4 = variables['a4']
    new_variables = {k: locals()[k] for k in variables}
    print("\n")
    print(new_variables)

    if K == 1:
        n1 = a1
        n2 = a2 - n1

    if K == 2:
        n1 = a1 / 2
        n2 = a2 - 3 * n1
        n3 = a3 - n1 - n2

    if K == 3:
        n1 = a1 / 6
        n2 = (a2 - 12 * n1) / 2
        n3 = a3 - 7 * n1 - 3 * n2
        n4 = a4 - n1 - n2 - n3

    if K == 4:
        n1 = variables['a1'] / 24
        n2 = (variables['a2'] - 60 * n1) / 6
        n3 = (variables['a3'] - 50 * n1 - 12 * n2) / 2
        n4 = variables['a4'] - 15 * n1 - 7 * n2 - 3 * n3
        n5 = variables['a5'] - n1 - n2 - n3 - n4

    if K == 5:
        n1 = variables['a1'] / 120
        n2 = (variables['a2'] - 360 * n1) / 24
        n3 = (variables['a3'] - 390 * n1 - 60 * n2) / 6
        n4 = (variables['a4'] - 180 * n1 - 50 * n2 - 12 * n3) / 2
        n5 = variables['a5'] - 31 * n1 - 15 * n2 - 7 * n3 - 3 * n4
        n6 = variables['a6'] - n1 - n2 - n3 - n4 - n5

    if K == 6:
        n1 = variables['a1'] / 720
        n2 = (variables['a2'] - 2520 * n1) / 120
        n3 = (variables['a3'] - 3360 * n1 - 360 * n2) / 24
        n4 = (variables['a4'] - 2100 * n1 - 390 * n2 - 60 * n3) / 6
        n5 = (variables['a5'] - 602 * n1 - 180 * n2 - 50 * n3 - 12 * n4) / 2
        n6 = variables['a6'] - 63 * n1 - 31 * n2 - 15 * n3 - 7 * n4 - 3 * n5
        n7 = variables['a7'] - n1 - n2 - n3 - n4 - n5 - n6


    # if K == 7
    #     n1 = variables['a1'] / 5040
    #     n2 = (variables['a2'] / 720
    #     n3 = (variables['a3'] - 2520 * n2) / 120
    #     n4 = (variables['a4'] - 3360 * n2 - 360 * n3) / 24
    #     n5 = (variables['a5'] - 2100 * n2 - 390 * n3 - 60 * n4) / 6
    #     n6 = (variables['a6'] - 602 * n2 - 180 * n3 - 50 * n4 - 12 * n5) / 2
    #     n7 = variables['a7'] - 63 * n2 - 31 * n3 - 15 * n4 - 7 * n5 - 3 * n6
    #     n8 = variables['a8'] - n2 - n3 - n4 - n5 - n6 - n7

    # Gathers n's to library
    for i in range(K + 1):
        exec("coefficients['n{}'] = n{}".format(i + 1, i + 1))

    return coefficients

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
    # Construct the polynomial outline using n1, n2, n3, ...
    polynomial = "P(x) = "
    for i in range(K):
        polynomial += "n{}x^{} + ".format(i + 1, K - i)
    polynomial += "n{}".format(K + 1)

    print("")
    print("variables =", variables)
    print("K =", K)
    print(polynomial)

    coefficents = coefficient_calculation_3(K, variables)
    polynomial = "Key = P(x) = "
    for i in range(K):
        polynomial += "{}x^{} + ".format(coefficents['n{}'.format(i + 1)], K - i)
    polynomial += "{}".format(coefficents['n{}'.format(K + 1)])
    print("")
    print(polynomial)
else:
    print(result)