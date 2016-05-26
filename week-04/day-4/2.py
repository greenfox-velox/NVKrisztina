# 2. write a recursive function
# that takes one parameter: n
# and adds numbers from 1 to n


def addNumber(input):
    if input < 1:
        return 0
    else:
        summa = input + addNumber(input - 1)
        return summa

print(addNumber(4))
