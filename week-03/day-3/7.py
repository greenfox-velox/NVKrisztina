list = [1, 2, 3, 4]

def double(input):
    newlist = []
    n = 0
    for n in input:
        n = n * 2
        newlist.append(n)
    print (newlist)

double(list)
