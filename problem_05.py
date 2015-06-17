import math
from collections import Counter


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
    return Counter(factors)


largest = {}
factors = list(map(find_primes, range(1, 21)))
print(factors)
for primes in factors:
    for prime, count in primes.most_common():
        if largest.get(prime, 0) < count:
            largest[prime] = count

print(largest)
lcf = 1
for prime, count in largest.items():
    res = prime ** count
    lcf = lcf * res
    print(lcf)

