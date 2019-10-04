# Unique names in sorted order

names = set()   # Empty set

while True:
    name = input("Enter name [end to stop] : ")
    if name == "end":
        break

    names.add(name)


for n in sorted(names):
    print(n)


