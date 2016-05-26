# 1. write a recursive function
# that takes one parameter: n
# and counts down from n

n = 10

def downCount(input):
    for i in range(input):
        summa = 10
        summa = summa - i
        print (summa)

downCount(n)

def recursiveDownCount(number):
    if number <= 0:
        pass
    else:
        print (number)
        recursiveDownCount (number - 1)

recursiveDownCount(10)


def sum(n):
    output = ''
    if n <= 0:
        return output
    else:
        return output + sum (n - 1)

sum(10)


def concat(n):
    if n <= 0:
        return []
    else:
        concat(n-1) + [n]


"""
prevstep = concat(n-1)
prevstep.append(n)
return prevstep
"""
