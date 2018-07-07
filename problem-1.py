
# numbers below 1000
nums = [i for i in range(1000)]

result = sum([i for i in nums if i % 3 == 0 or i % 5 == 0])

print(result)
