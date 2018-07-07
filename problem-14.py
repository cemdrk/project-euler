
cache = {1: 1}

def chain(n):
    global cache

    count = cache.get(n, 0)

    if count == 0:
        cache[n] = 1 + chain(n // 2) if n % 2 == 0 else 1 + chain(3 * n + 1)

    return cache[n]


max_chain = 0
num = 0
for i in range(1, 1_000_000):
    c = chain(i)
    if c > max_chain:
        max_chain = c
        num = i

print(num)
