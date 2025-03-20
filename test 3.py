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


variables = {'a0': 6.0, 'a1': 12.0, 'a2': 8.0, 'a3': 3.0}
P = int(input("Enter the starting value: "))
K = len(variables) - 1

pivot = []
for J in range(K, -1, -1):
    temp_list = []
    for H in range(K, -1, -1):
        r = coefficient_calculation_loop(H, J, P, K)
        temp_list.append(r)
    pivot. append(temp_list)

# Solve the equations using Gauss-Jordan elimination
for i in range(K):
    factor = pivot[i][i]
    for j in range(i+1, K+1):
        ratio = pivot[j][i] / factor
        for k in range(K+1):
            pivot[j][k] -= ratio * pivot[i][k]

x = [0] * K
for i in range(K-1, -1, -1):
    x[i] = pivot[i][K]
    for j in range(i+1, K):
        x[i] -= pivot[i][j] * x[j]
    x[i] /= pivot[i][i]

# Print the solutions
for i, key in enumerate(variables.keys()):
    print(f"{key} = {x[i]}")
