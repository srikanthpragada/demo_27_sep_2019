def iseven(n):
    # print(n)
    return n % 2 == 0


nums = [10, 11, 20, 48, 57, 80]

enums = filter(iseven, nums)
print(enums)
for n in enums:
    print(n)

for c in filter(str.isupper,"AbcDEf"):
    print(c)