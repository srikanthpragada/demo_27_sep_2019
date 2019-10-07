def last_digit(n):
    return n % 10


nums = [10, 30, 11, 25, 24, 48, 57, 83]

for n in sorted(nums, key=last_digit):
    print(n, end=' ')

for n in sorted(nums, key=lambda n: n // 10):
    print(n, end=' ')
