a = 10

def f1():
    b = 20
    def f2():
        nonlocal b
        global  a
        a = 1
        b = 2
        c = 30
        print(a,b,c)

    f2()
    print(b)

f1()
print(a)