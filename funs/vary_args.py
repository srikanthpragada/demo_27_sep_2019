def wish(*names, message='Hi'):
    for n in names:
        print(message, n)


def process(*, n1=10, n2=20):
    pass


process(10)

wish("Abc", "Xyz", message="Hello")
wish("Bill", "Larry")

print(10, 20, 30, end='...\n', sep='*')
