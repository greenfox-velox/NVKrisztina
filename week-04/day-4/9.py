# 9. Given a string, compute recursively a new string where all the
# adjacent chars are now separated by a "*".

def removeX(input, n):
    if n == 0:
        return ''
    elif input[n - 1] != 'x':
        return removeX(input, n - 1) + input[n - 1] + '*'
    elif input[n - 1] == 'x':
        return removeX(input, n - 1) + input[n - 1] + '*'


print(removeX('pxthon', len('pxthon')))
