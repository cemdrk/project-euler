
def gcd(m, n):
    while n:
        m, n = n, m % n

    return m


def smallest_multiple(n):
    """ smallest multiple number from 1 to n"""

    smallest = 1

    for i in range(1, n):
        smallest *= i // gcd(smallest, i)

    return smallest


result = smallest_multiple(20)

print(result)