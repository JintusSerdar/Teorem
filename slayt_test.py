from decimal import Decimal, getcontext

def comb(n, k):

    result = 1

    for i in range(1, k+1):
        result *= n - k + i
        result //= i

    return result


def coefficient_calculation_loop2(k, s, p, d):
    result = 0

    for i in range(k + 1):
        coefficient = (-1) ** (k - i) * comb(k, k - i)
        term = coefficient * (s + d * i) ** p
        result += term

    return result

def coefficient_calculation_loop1(k, s, p, d):
    result = 0

    for i in range(k + 1):
        coefficient = (-1) ** (i) * comb(k, i)
        term = coefficient * (d * (k - i) + s) ** p
        result += term

    return result

def coefficient_calculation_loop3(k, s, p, d):
    result = Decimal('0')
    getcontext().prec = 28  # Set precision as needed

    for i in range(k + 1):
        coefficient = (-1) ** i * Decimal(comb(k, i))
        term = coefficient * (Decimal(d) * (k - i) + Decimal(s)) ** p
        result += term

    result_str = result.quantize(Decimal('1e-10')).normalize().to_eng_string()
    return result_str

def coefficient_calculation_loop4(k, s, p, d):
    result = Decimal('0')
    getcontext().prec = 10  # Set precision as needed

    for i in range(k + 1):
        coefficient = (-1) ** (k - i) * Decimal(comb(k, k - i))
        term = coefficient * (Decimal(d) * i + Decimal(s)) ** p
        result += term

    return result

# s represents the starting value for the polynomial.
# When s = 1, it means that the user should enter P(1), P(1 + d), P(1 + 2*d), and so on.
s = 0

# d represents the difference interval between the values for the polynomial.
# For example, if the user enters d = 0.1, they should enter P(s + 0*0.1), P(s + 1*0.1), P(s + 2*0.1), and so on, with intervals of 0.1.
d = 1

degree = 5

table1 = []
table2 = []
for k in range(degree + 1):
    # k represents the degree of the polynomial.
    # It ranges from 0 to the specified 'degree' value.
    # k = 0 corresponds to a constant polynomial, k = 1 to a linear polynomial, and so on.
    table1.append([])
    table2.append([])
    for p in range(degree + 1):
        # p represents the power of terms in the polynomial equation.
        # It ranges from 0 to degree, where p = 0 corresponds to the constant term,
        # p = 1 to the linear term, and so on.
        table1[k].append(coefficient_calculation_loop1(k, s, p, d))
        table2[k].append(coefficient_calculation_loop2(k, s, p, d))


print("Table 1:")
for row in table1:
    print(row)

print("Table 2:")
for row in table2:
    print(row)
