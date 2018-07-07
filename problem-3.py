
def largest_prime(n):
    i = 2
    while i ** 2 <= n:
        if n % i:
            i += 1
        else:
            n //= i
    return n


result = largest_prime(600851475143)

print(result)