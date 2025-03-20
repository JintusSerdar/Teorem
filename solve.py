from sympy import symbols, Eq, solve
def comb(n, k):
    result = 1

    for i in range(1, k+1):
        result *= n - k + i
        result //= i

    return result


def coefficient_calculation_loop(H, J, P, K, L=0):
    r1 = 0

    for i in range(K + 1):
        coefficient = (-1) ** i * comb(H + L, i)
        term = coefficient * (H + P - i) ** J
        r1 += term

    return r1

variables = {'a0': 6.0, 'a1': 6.0, 'a2': 2.0, 'a3': 1.0}
P = int(input("Enter the starting value: "))
K = len(variables) - 1

pivot = []
for J in range(K, -1, -1):
    temp_list = []
    for H in range(K, -1, -1):
        r = coefficient_calculation_loop(H, J, P, K)
        temp_list.append(r)
    pivot.append(temp_list)


n0, n1, n2, n3 = symbols('n0 n1 n2 n3')

eq0 = Eq(variables['a0'], n0 * pivot[0][0])
eq1 = Eq(variables['a1'], n0 * pivot[0][1] + n1 * pivot[1][1])
eq2 = Eq(variables['a2'], n0 * pivot[0][2] + n1 * pivot[1][2] + n2 * pivot[2][2])
eq3 = Eq(variables['a3'], n0 * pivot[0][3] + n1 * pivot[1][3] + n2 * pivot[2][3] + n3 * pivot[3][3])
sol = solve((eq0, eq1, eq2, eq3), (n0, n1, n2, n3))

print(sol)
sol = {str(key): float(value) for key, value in sol.items()}
print(sol)

polynomial = "Key = P(x) = "
for i in range(K):
    polynomial += "{}x^{} + ".format(sol['n{}'.format(i)], K - i)
polynomial += "{}".format(sol['n{}'.format(K)])
print("")
print(polynomial)

# sol = {str(key): float(value) for key, value in sol.items()}
# print(sol)




 # [[6, 12, 7, 1], [0, 2, 3, 1], [0, 0, 1, 1], [0, 0, 0, 1]]