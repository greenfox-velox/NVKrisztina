y = range(101)

for x in y:
    if x % 3 == 0 and x % 5 == 0:
        x = str("Fizzbuzz")
        print(x)
    elif x % 3 == 0:
        x = str("Fizz")
        print(x)
    elif x % 5 == 0:
        x = str("Buzz")
        print(x)
    else:
        print(x)

"""
i = 0

while i <= 100:
    if i % 3 == 0:
        print("Fizz")
    else:
        print(i)
    i += 1
"""
