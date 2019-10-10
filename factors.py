import sys
# Display factors for the given number on command line
if len(sys.argv) < 2:
    print('Usage : python factors.py number')
    sys.exit(0)

n = int(sys.argv[1])

for i in range(2, n // 2 + 1):
    if n % i == 0:
        print(i)


