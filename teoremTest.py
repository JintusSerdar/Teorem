import numpy as np
from scipy.special import comb

def calculate_formula(n, d, s, k):
    """
    Calculate the formula: sum_{i=0}^{n} (-1)^i * C(n,i) * (d(n-i) + s)^k
    
    Parameters:
    n (int): Upper limit of summation
    d (float): Coefficient for (n-i)
    s (float): Constant term
    k (int): Power
    
    Returns:
    float: Result of the formula
    """
    result = 0
    
    for i in range(n + 1):
        # Calculate (-1)^i
        sign = (-1) ** i
        
        # Calculate binomial coefficient C(n,i)
        binomial = comb(n, i)
        
        # Calculate (d(n-i) + s)^k
        term = (d * (n - i) + s) ** k
        
        # Add to the sum
        result += sign * binomial * term
    
    return result

def main():
    # Get input from user
    try:
        n = int(input("Enter n (upper limit of summation): "))
        d = float(input("Enter d (coefficient): "))
        s = float(input("Enter s (constant term): "))
        k = int(input("Enter k (power): "))
        
        # Calculate and display result
        result = calculate_formula(n, d, s, k)
        print(f"\nResult: {result}")
        
    except ValueError:
        print("Please enter valid numbers!")

if __name__ == "__main__":
    main()
