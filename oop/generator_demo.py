# Generator
def even_numbers(start, end):
    for n in range(start, end + 1):
        if n % 2 == 0:
            yield n


def reverse(data):
    for v in data[::-1]:
        yield v


for n in even_numbers(10, 20):
    print(n)

for c in reverse("Pyton"):
    print(c)


l = list(reverse('Python'))
print(l)
