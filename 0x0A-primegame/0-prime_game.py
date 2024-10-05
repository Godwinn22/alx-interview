#!/usr/bin/python3
"""Prime Game Module"""


def isWinner(x, nums):
    """Function to get who has won in prime game"""
    if x < 1 or not nums:
        return None

    # Determine the maximum value of n in nums
    max_n = max(nums)

    # Create a list to mark whether numbers are prime up to max_n
    sieve = [True] * (max_n + 1)
    sieve[0] = sieve[1] = False  # 0 and 1 are not prime numbers

    # Sieve of Eratosthenes to find all prime numbers up to max_n
    p = 2
    while (p * p <= max_n):
        if sieve[p]:
            for i in range(p * p, max_n + 1, p):
                sieve[i] = False
        p += 1

    # Precompute the number of primes up to each number i
    prime_count = [0] * (max_n + 1)
    for i in range(1, max_n + 1):
        prime_count[i] = prime_count[i - 1]
        if sieve[i]:
            prime_count[i] += 1

    # Determine the winner for each round
    maria_wins = 0
    ben_wins = 0

    for n in nums:
        if prime_count[n] % 2 == 0:
            ben_wins += 1
        else:
            maria_wins += 1

    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None
