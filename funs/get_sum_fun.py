def get_sum(nums):
    total = 0
    for n in nums:
        total += abs(n)

    return total


nums = [10, 20, 30, -10]
print(sum(nums))
print(get_sum(nums))
