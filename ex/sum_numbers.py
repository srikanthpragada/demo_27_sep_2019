total = 0
count = 0
while True:
    n = int(input("Enter a number :"))
    if n == 0:
        break

    total += n
    count += 1

print("Average =", total//count)
