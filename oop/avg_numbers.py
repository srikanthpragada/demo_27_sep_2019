count = sum = 0

while True:
    try:
        num = int(input("Enter a number [0 to stop] :"))
        if num == 0:
            break

        sum += num
        count += 1
    except ValueError:
        print("Sorry! Invalid number. Please try again!")

print("Average : ", sum // count)
