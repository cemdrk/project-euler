
def triplet_product(limit):
    for a in range(1, limit//2):
        for b in range(a, limit//2):
            c = limit - (a+b)
            if a ** 2 + b ** 2 == c ** 2:
                return a*b*c


result = triplet_product(1000)

print(result)
