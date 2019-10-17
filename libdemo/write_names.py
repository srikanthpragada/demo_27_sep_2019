names = set()

while True:
    name = input("Enter name [end to stop] :")
    if name == "end":
        break

    names.add(name)

with open("names.txt", "wt") as f:
    for n in sorted(names):
        f.write(n + "\n")
