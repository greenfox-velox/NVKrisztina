
g = 5

def factorial(input):
    z = []
    while input > 0:
        z.append(input)
        input = input - 1
    summa = 1
    for n in z:
        summa = summa * n
    print(summa)
factorial(g)

"""
def factorial(input_number):
    factorta = 1
    for i in range(1,input_number+1):
        factorta *= i
    return factorta

print(factrial(5))

"""
