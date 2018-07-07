
def factorial(n):
    if n == 1:
        return 1
    return n * factorial(n - 1)


num = str(factorial(100))

result = sum(int(i) for i in num)

print(result)
