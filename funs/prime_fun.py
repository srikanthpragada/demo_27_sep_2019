def isprime(num):
    for i in range(2, num // 2 + 1):
        if num % i == 0:
            return False

    return True


print(isprime(17), isprime(255), isprime(3934341))
