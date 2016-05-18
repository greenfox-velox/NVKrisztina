numbers = [7, 5, 8, -1, 2]

def minimal(input):
    minem = input[0]
    for n in input:
        if minem < n:
            pass
        else:
            minem = n
    print(minem)

minimal(numbers)


"""
def findminimum(input):
    minimum = input[0]
    for item in input:
        if item < minimum:
            minimum = item

    return minimum

print(findminimum(numbers))
"""
