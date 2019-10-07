nums = [10, -30, 11, 25, -20, 48, 57, -80]

for n in sorted(nums, key=abs):
    print(n)

names = ['Java', 'Python', 'Basic', 'C++', 'Sql', 'TypeScript']

for n in sorted(names, key=len):
    print(n)
