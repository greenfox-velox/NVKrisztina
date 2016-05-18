numbers = [3, 4, 5, 6, 7]

def filter(item):
    for n in item:
        if n % 2 != 0:
            del(n)
        else:
            print(n)

filter(numbers)

"""
def filter(item):
    evens = []
    for item in input:
        if item % 2 == 0:
            evens += [item]
    return evens

print(filter(numbers))

"""
