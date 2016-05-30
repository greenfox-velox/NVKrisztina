def median(pool):
    return pool[int((len(pool) - 1) / 2)]
print(median([1, 2, 3, 4]))


def median(pool):
    pool.sort()
    if len(pool) % 2 != 0:
        return pool[int((len(pool) + 1)/2 - 1)]
    else:
        return (pool[int((len(pool))/2)] + pool[int(((len(pool))/2)) + 1])/2 - 1
print(median([1, 2, 3, 4]))

def is_vovel(char):
    return char in 'aeiou'
print(is_vovel('U'))


def teves(string):
    new = ''
    for char in string:
        if not is_vovel(char):
            new = new + char
        else:
            char = char + 'v' + char
            new = new + char
    return new

print(teves('koala'))
