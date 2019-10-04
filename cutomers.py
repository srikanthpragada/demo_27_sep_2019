
customers = {}
while True:
    name = input("Enter customer name[end to stop] : ")
    if name == "end":
        break

    email = input("Enter email addresss : ")
    customers[name] = email

for n,e in sorted(customers.items()):
    print(f"{n:20s} {e}")


