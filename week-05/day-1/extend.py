# Adds a and b, returns as result
def add(a, b):
    summa = a + b
    return summa

# Returns the highest value from the three given params
def max_of_three(a, b, c):
    if a > b and a > c:
        return a
    elif b > a and b > c:
        return b
    else:
        return c

# Returns the median value of a list given as param
def median(pool):
    pool.sort()
    if len(pool) % 2 != 0:
        return pool[int((len(pool) + 1)/2 - 1)]
    else:
        return (pool[int((len(pool))/2)] + pool[int(((len(pool))/2)) + 1])/2 - 1
print(median([1, 2, 3, 4]))


# Returns true if the param is a vovel
def is_vovel(char):
    return char.lower() in 'aeiouáéúűőóüöí'

# Create a method that translates hungarian into the teve language
def translate(string):
    new = ''
    for char in string:
        if not is_vovel(char):
            new = new + char
        else:
            char = char + 'v' + char
            new = new + char
    return new

print(translate('koala'))
