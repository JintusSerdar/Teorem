def comb(n, k):
    result = 1

    for i in range(1, k+1):
        result *= n - k + i
        result //= i

    return result


def coefficient_calculation_loop(H, J, P, K, L = 0):
    r1 = 0

    for i in range(K + 1):
        coefficient = (-1) ** i * comb(H + L, i)
        term = coefficient * (H + P - i) ** J
        r1 += term

    return r1

H = 6 # it goes down in the value table
P = 1 # it changes the starting value
L = 0 # we don't need this for now, but it is there for future improvements
J = 6 # it goes side in the value table
K = 6 # Repeat time and the degree of the polynomial
a = coefficient_calculation_loop(H, J, P, K, L)
print(a)

# H ve J yi K ye kadar bir library ya da array yap. 2 dimensinoal


'''
L yi bir azaltmak H yi bir azaltip P yi bir arttirmak ile ayni
'''