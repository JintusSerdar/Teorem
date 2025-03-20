
# To use "-" in polynomial include "+" as well. For example instead of 1.0x^3 + 0.0x^2 + 1.0x^1 - 1.0 use this 1.0x^3 + 0.0x^2 + 1.0x^1 + -1.0
def evaluate_polynomial(polynomial, min_value, max_value):
    # Split the polynomial into terms and extract coefficients and exponents
    terms = polynomial.split(" + ")
    coefficients = [float(term.split("x^")[0]) if "x^" in term else float(term) for term in terms]
    exponents = [int(term.split("x^")[1]) if "x^" in term else 0 for term in terms]

    # Compute the values of the polynomial for the given range of inputs
    values = []
    for x in range(min_value, max_value+1):
        value = sum(coefficient * (x ** exponent) for coefficient, exponent in zip(coefficients, exponents))
        values.append(value)
    return values

polynomial = input("Enter the polynomial: ")
min_value = int(input("Enter the minimum value: "))
max_value = int(input("Enter the maximum value: "))
result = evaluate_polynomial(polynomial, min_value, max_value)
print(result)
# 10x^10 + 6x^6 + -8x^2 + -9x^5 + 9
# 10519433, 596988, 10889, 26, 9, 8, 10313, 592614, 10501001, 97721684, 604871433, 2825306738, 10738695689
# 4x^7 + 3x^3 + -7x^1 + 9
# 9.0, 531.0, 8817.0, 65709.0, 312849.0, 1120359.0, 3295161.0, 8390097.0, 19134009.0, 40002939.0
# 112.0x^6 + -1288.0x^5 + 7840.0x^4 + -27073.0x^3 + 52528.0x^2 + -52279.0x^1 + 20169.0
# 9.0, 531.0, 8817.0, 65709.0, 312849.0, 1120359.0, 3295161.0, 8369937.0, 18972729.0, 39277179.0

# 1 + 1x^1 + 9.303188e-15x^2 + 1x^3

# 1x^10 + 1x^4
# 0.0, 2.0, 1040.0, 59130.0, 1048832.0, 9766250.0, 60467472.0, 282477650.0, 1073745920.0, 3486790962.0, 10000010000.0

# 179487.0x^5 + -2445574.0x^4 + 12934845.0x^3 + -32595024.0x^2 + 38361708.0x^1 + -16435440.0
# -16435440.0, 2.0, 1040.0, 59130.0, 1048832.0, 9766250.0, 60467472.0, 236407010.0, 691376240.0, 1671241842.0, 3535484240.0

# 1x^10
# 0.0, 1.0, 1024.0, 59049.0, 1048576.0, 9765625.0, 60466176.0, 282475249.0, 1073741824.0, 3486784401.0, 10000000000.0
# 179487.0x^5 + -2445575.0x^4 + 12934845.0x^3 + -32595024.0x^2 + 38361708.0x^1 + -16435440.0
# -16435440.0, 1.0, 1024.0, 59049.0, 1048576.0, 9765625.0, 60466176.0, 236404609.0, 691372144.0, 1671235281.0, 3535474240.0
