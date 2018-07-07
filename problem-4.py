
def is_palindrome(n):
    return str(n) == str(n)[::-1]

max_palindrome = 0

for i in range(100,1000):
    for j in range(i, 1000):
        prod = i * j

        if is_palindrome(prod):
            max_palindrome = max(max_palindrome, prod)


print(max_palindrome)
