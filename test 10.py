import time

start_time = time.time()

import numpy as np

# Ask user for starting term and sequence
start = 0
seq = [1, 3, 8, 10]

# Calculate forward differences
diff = seq
fdiffs = []
while len(diff) > 1:
    fdiff = [diff[i+1]-diff[i] for i in range(len(diff)-1)]
    fdiffs.append(fdiff)
    diff = fdiff

# Determine order of polynomial
order = len(fdiffs) + 1

A = np.zeros((order, order))
B = np.zeros((order, 1))
for i in range(order):
    for j in range(order):
        A[i][j] = (i+start)**j
    B[i] = seq[i]

X = np.linalg.inv(A).dot(B)
coeffs = X.ravel()


poly = "Pn = "
for i in range(order):
    if i == 0:
        poly += str(round(coeffs[i], 2))
    else:
        poly += f" + {round(coeffs[i], 2)}*n^{i}"
print(poly)

end_time = time.time()

print("Execution time:", end_time - start_time)