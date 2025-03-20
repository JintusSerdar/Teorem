import numpy as np
import matplotlib.pyplot as plt
from typing import List, Tuple
import re
import sys

class PolynomialEvaluator:
    def __init__(self):
        self.polynomial_pattern = re.compile(r'([-+]?\d*\.?\d*(?:e[-+]?\d+)?)?(?:x\^(\d+))?')

    def parse_polynomial(self, polynomial: str) -> Tuple[List[float], List[int]]:
        """Parse polynomial string into coefficients and exponents."""
        try:
            # Standardize the input format
            polynomial = polynomial.replace(" ", "")
            
            # Validate that only allowed characters are present
            if not re.match(r'^[-+.0-9x^e]+$', polynomial):
                raise ValueError("Invalid characters in polynomial. Use only numbers, x, ^, +, -, and decimal points.")
            
            # Handle the first term which might not have a + sign
            if not polynomial.startswith('+') and not polynomial.startswith('-'):
                polynomial = '+' + polynomial
                
            # Split terms while preserving signs
            terms = re.findall(r'[+-][^+-]+', polynomial)
            
            coefficients = []
            exponents = []
            
            for term in terms:
                # Validate each term has proper format
                if 'x' in term and not '^' in term:
                    raise ValueError("When using 'x', you must specify the power (e.g., x^1 instead of x)")
                
                match = self.polynomial_pattern.match(term)
                if not match or not term.strip('+-'):
                    raise ValueError(f"Invalid term: {term}")
                
                coef_str, exp_str = match.groups()
                
                # Handle coefficient
                if coef_str in ('+', '-', '', None):
                    coef = 1.0 if coef_str != '-' else -1.0
                else:
                    coef = float(coef_str)
                
                # Handle exponent
                exp = 0 if exp_str is None else int(exp_str)
                
                coefficients.append(coef)
                exponents.append(exp)
            
            if not coefficients:
                raise ValueError("No valid terms found in polynomial")
                
            return coefficients, exponents
        except Exception as e:
            raise ValueError(f"Invalid polynomial format: {e}")

    def evaluate_polynomial(self, polynomial: str, min_value: float, max_value: float, step: float = 1.0) -> np.ndarray:
        """Evaluate polynomial using numpy for better performance."""
        try:
            coefficients, exponents = self.parse_polynomial(polynomial)
            x_values = np.arange(min_value, max_value + step/2, step)
            y_values = np.zeros_like(x_values)
            
            for coef, exp in zip(coefficients, exponents):
                y_values += coef * np.power(x_values, exp)
                
            return np.round(y_values, decimals=6)
        except Exception as e:
            raise ValueError(f"Error evaluating polynomial: {e}")

    def plot_polynomial(self, x_values: np.ndarray, y_values: np.ndarray, polynomial: str):
        """Plot the polynomial using matplotlib."""
        plt.figure(figsize=(10, 6))
        plt.plot(x_values, y_values, 'b-', label=f'f(x) = {polynomial}')
        plt.grid(True)
        plt.xlabel('x')
        plt.ylabel('f(x)')
        plt.title('Polynomial Function')
        plt.legend()
        
        # Add points
        plt.plot(x_values, y_values, 'ro', markersize=4)
        
        plt.savefig('polynomial_plot.png')
        plt.close()

def get_validated_float_input(prompt: str) -> float:
    """Get and validate float input from user."""
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Please enter a valid number.")

def save_to_file(x_values: np.ndarray, y_values: np.ndarray, filename: str = "polynomial_values.txt"):
    """Save results to a file."""
    with open(filename, 'w') as f:
        f.write("x\t\tf(x)\n")
        f.write("-" * 30 + "\n")
        for x, y in zip(x_values, y_values):
            f.write(f"{x:.6f}\t{y:.6f}\n")

def main():
    try:
        evaluator = PolynomialEvaluator()
        
        # Get input with validation
        while True:
            polynomial = input("Enter the polynomial (e.g., 1x^2 + 2x^1 + 1): ")
            try:
                # Test parsing
                evaluator.parse_polynomial(polynomial)
                break
            except ValueError as e:
                print(f"Error: {e}")
                print("Please try again.")

        min_value = get_validated_float_input("Enter the minimum value: ")
        max_value = get_validated_float_input("Enter the maximum value: ")
        while True:
            step = get_validated_float_input("Enter the step size (e.g., 0.1): ")
            if step > 0:
                break
            print("Step size must be positive.")

        # Calculate values
        x_values = np.arange(min_value, max_value + step/2, step)
        y_values = evaluator.evaluate_polynomial(polynomial, min_value, max_value, step)

        # Print results
        print("\nResults:")
        print(y_values.tolist())

        # Save to file
        # save_to_file(x_values, y_values)
        # print("\nResults have been saved to 'polynomial_values.txt'")

        # Create plot
        # evaluator.plot_polynomial(x_values, y_values, polynomial)
        # print("Plot has been saved as 'polynomial_plot.png'")

    except Exception as e:
        print(f"An error occurred: {e}", file=sys.stderr)
        return 1

if __name__ == "__main__":
    sys.exit(main())