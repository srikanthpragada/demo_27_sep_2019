def swap(n1, n2):
    print(id(n1))
    n1, n2 = n2, n1
    print(id(n1), id(n2))

a = 10
print(id(a))
b = 20
swap(a, b)

print(f"{a},{b}")


def addfirst(lst, v):
    lst.insert(0, v)

l = [10, 20]
addfirst(l, 5)
print(l)


def zero(v):
    print(id(v))
    v = 0
    print(id(v))

a = 10
zero(a)
print(a)



