import psutil


def matrix_multiply(A, B):
    m = len(A)
    n = len(B[0])
    p = len(B)
    C = [[0 for j in range(n)] for i in range(m)]
    for i in range(m):
        for j in range(n):
            for k in range(p):
                C[i][j] += A[i][k] * B[k][j]
    return C

def matrix_inverse(A):
    n = len(A)
    A_aug = [row[:] + [int(i==j) for i in range(n)] for j,row in enumerate(A)]
    for i in range(n):
        factor = 1.0 / A_aug[i][i]
        for j in range(2*n):
            A_aug[i][j] *= factor
        for j in range(n):
            if i != j:
                factor = A_aug[j][i]
                for k in range(2*n):
                    A_aug[j][k] -= factor * A_aug[i][k]
    return [row[n:] for row in A_aug]

# Ask user for starting term and sequence
start = 1
seq = [1, 2, 3, 4, 5, 6]

# Calculate forward differences
diff = seq
fdiffs = []
while len(diff) > 1:
    fdiff = [diff[i+1]-diff[i] for i in range(len(diff)-1)]
    fdiffs.append(fdiff)
    diff = fdiff

# Determine order of polynomial
order = len(fdiffs) + 1

# Calculate coefficients of polynomial
A = [[(i+start)**j for j in range(order)] for i in range(order)]
B = [[seq[i]] for i in range(order)]
A_inv = matrix_inverse(A)
X = matrix_multiply(A_inv, B)
coeffs = [x[0] for x in X]

# Print polynomial equation
poly = "Pn = "
for i in range(order):
    if i == 0:
        poly += str(round(coeffs[i], 2))
    else:
        poly += f" + {round(coeffs[i], 2)}*n^{i}"
print(poly)

process = psutil.Process()
print("Memory usage:", process.memory_info().rss / 1024 / 1024, "MB")
