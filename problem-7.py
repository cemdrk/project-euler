
def prime(n):

    prime_list = [2]

    num = 3

    while n > len(prime_list):

        for p in prime_list:
            if num % p == 0:
                break
        # if for loop not break
        else:
            prime_list.append(num)

        num += 2

    return prime_list[-1]


result = prime(10_001)

print(result)