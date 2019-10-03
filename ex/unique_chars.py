# Unique chars of a given string

st = input("Enter a string : ")

chars = []

for c in st:
    if c not in chars:
        chars.append(c)


for c in chars:
    print(c)