def evaluate_polynomial(polynomial, min_value, max_value):
    terms = polynomial.split(" + ")
    coefficients = [float(term.split("x^")[0]) if "x^" in term else float(term) for term in terms]
    exponents = [int(term.split("x^")[1]) if "x^" in term else 0 for term in terms]
    values = []
    for i in range(min_value, max_value+1):
        value = 0
        for j in range(len(terms)):
            if "x^" in terms[j]:
                coefficient, exponent = terms[j].split("x^")
                coefficient = float(coefficient)
                exponent = int(exponent)
            else:
                coefficient = float(terms[j])
                exponent = 0
            value += coefficient * (i ** exponent)
        values.append(value)
    return values


polynomial = input("Enter the polynomial: ")
min_value = int(input("Enter the minimum value: "))
max_value = int(input("Enter the maximum value: "))
result = evaluate_polynomial(polynomial, min_value, max_value)
print(result)