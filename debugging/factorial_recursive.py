#!/usr/bin/python3
import sys

def factorial(n):
    """
    Calculate the factorial of a given number using recursion.

    Parameters:
    - n (int): The number whose factorial is to be calculated.

    Returns:
    - int: The factorial of the given number.
    """
    if n == 0:
        return 1
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers.")
    return n * factorial(n-1)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <number>")
    else:
        try:
            num = int(sys.argv[1])
            print(factorial(num))
        except ValueError as e:
            print("Error:", e)
