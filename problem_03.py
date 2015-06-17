import math


def find_primes(n):
    while n % 2 == 0:
        print(2)
        n /= 2

    i = 3
    while i <= math.sqrt(n):
        while n % i == 0:
            print(i)
            n /= i
        i += 2

    if n > 2:
        print(n)


find_primes(600851475143)
