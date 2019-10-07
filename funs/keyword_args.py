def print_details(**details):
    print(type(details))
    for k,v in details.items():
        print(k,v)


print_details(a=10, b=20, c=30)
print_details(n1=10, n2=20)
