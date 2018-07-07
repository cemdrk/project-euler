
# fibonacci sequence starting 1 and 2 not exceed n
def fibo(n):
    a, b = 1, 2
    while n > a:
        yield a
        a, b = b, a+b


# even valued terms
evens = [i for i in fibo(4_000_000) if i%2 == 0]

result = sum(evens)

print(result)