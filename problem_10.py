from itertools import islice

__author__ = 'Tiger'


def gen_primes():
    sieve = {}
    p = 2

    while p < 2000000:
        if p not in sieve:
            yield p
            sieve[p * p] = [p]
        else:
            for composite in sieve[p]:
                sieve.setdefault(composite + p, []).append(composite)
            del sieve[p]
        p += 1

result = sum(gen_primes())
print(result)