#!/usr/bin/python3
"""
This module contains a method that calculates the fewest number of operations
needed to result in exactly n H characters in a file.
"""


def minOperations(n):
    """
    Calculate the minimum number of operations required to obtain exactly n 'H'
    characters in a text file starting with a single 'H', using only
    two operations: "Copy All" and "Paste".

    Args:
    n (int): The desired number of 'H' characters.

    Returns:
    int: The minimum number of operations required.
    Returns 0 if n is less than or equal to 1.

    Example:
    >>> minOperations(9)
    6

    Explanation:
    - Start with a single 'H'.
    - Copy All (1 operation) and Paste (1 operation): H -> HH
    - Paste (1 operation): HH -> HHH
    - Copy All (1 operation) and Paste (1 operation): HHH -> HHHHHH
    - Paste (1 operation): HHHHHH -> HHHHHHHHH (9 'H' characters)
    - Total operations: 6
    """
    if n <= 1:
        # Impossible to achieve less than or equal to 1 'H', so return 0
        return 0

    operations = 0
    # Start with the smallest prime number
    divisor = 2

    while n > 1:
        # While n is divisible by the current divisor, perform the operations
        while n % divisor == 0:
            # Add the divisor to the operation count
            operations += divisor
            # Reduce n by dividing it by the divisor
            n //= divisor
        # Move to the next potential divisor
        divisor += 1

    # Return the total number of operations
    return operations
