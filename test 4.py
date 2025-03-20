import numpy as np

# Ask user for starting term and sequence
start = int(input("Enter the starting term of the sequence: "))
seq = input("Enter the sequence separated by commas: ").split(',')
seq = [int(x) for x in seq]

# Calculate forward differences
diff = seq
fdiffs = []
while len(diff) > 1:
    fdiff = [diff[i+1]-diff[i] for i in range(len(diff)-1)]
    fdiffs.append(fdiff)
    diff = fdiff

# Determine order of polynomial
order = len(fdiffs) + 1
if order == 1:
    print("The sequence is a first order polynomial.")
elif order == 2:
    print("The sequence is a second order polynomial.")
elif order == 3:
    print("The sequence is a third order polynomial.")
else:
    print(f"The sequence is a {order}th order polynomial.")

# Calculate coefficients of polynomial
A = np.zeros((order, order))
B = np.zeros((order, 1))
for i in range(order):
    for j in range(order):
        A[i][j] = (i+start)**j
    B[i] = seq[i]

X = np.linalg.inv(A).dot(B)
coeffs = X.ravel()

# Print polynomial equation
poly = "Pn = "
for i in range(order):
    if i == 0:
        poly += str(round(coeffs[i], 2))
    else:
        poly += f" + {round(coeffs[i], 2)}*n^{i}"
print(poly)
