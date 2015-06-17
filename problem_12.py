from functools import reduce
from math import factorial
import math
import itertools

__author__ = 'Tiger'


def find_primes(n):
    factors = []
    while n % 2 == 0:
        factors.append(2)
        n /= 2

    i = 3
    while i <= math.sqrt(n):
        while n % i == 0:
            factors.append(int(i))
            n /= i
        i += 2

    if n > 2:
        factors.append(int(n))
    return factors


def n_choose_k(n, k):
    return itertools.combinations(n, k)


def generate_factors():
    factors = {1}
    triangle_number = 1
    nth_number = 1
    while len(factors) < 500:
        nth_number += 1
        triangle_number += nth_number
        print(nth_number, "th triangle number ", triangle_number)
        primes = find_primes(triangle_number)
        print(primes)
        # i is the number of factors to multiply together
        factors = {1}
        for i in range(1, len(primes) + 1):
            combinations = list(n_choose_k(primes, i))
            print(str(len(primes)), "choose " + str(i))
            print(combinations)
            for combo in combinations:
                factors.add(reduce(lambda x, y: x * y, combo))
        print(factors)
    print(triangle_number)

generate_factors()
