
def square_diff(n):

    nums = [i for i in range(n+1)]

    sum_of_squares = sum(i ** 2 for i in nums)

    square_of_sums = sum(nums) ** 2

    return square_of_sums - sum_of_squares


result = square_diff(100)

print(result)