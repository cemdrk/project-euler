
def primes(limit):
    """ sieve of eratosthenes """
    prime_list = [True] * (limit-1)

    prime_list[0:1] = [False, False]

    for (p, isprime) in enumerate(prime_list):
        if isprime:
            yield p
            for n in range(p ** 2, limit, p):
                prime_list[n] = False


result = sum(primes(2_000_000))

print(result)
