__author__ = 'Tiger'


def gen_primes():
    sieve = {}
    prime = 2

    while True:
        if prime not in sieve:
            yield prime
            sieve[prime * prime] = [prime]
        else:
            for composite in sieve[prime]:
                sieve.setdefault(composite + prime, []).append(composite)
            del sieve[prime]
        prime += 1

generator = gen_primes()
count = 1
for prime in generator:
    print(prime)
    print(count)
    if count == 10001:
        break
    count += 1


