# print all prime numbers from 1 to 100
for num in range(1, 101):
    for i in range(2, num // 2 + 1):
        if num % i == 0:
            break
    else:
        print(num)
