# 7. Given a string, compute recursively (no loops) a new string where all the
# lowercase 'x' chars have been changed to 'y' chars.

def removeX(input, n):
    if n == 0:
        return ''
    elif input[n - 1] != 'x':
        return removeX(input, n - 1) + input[n - 1]
    elif input[n - 1] == 'x':
        return removeX(input, n - 1) + 'y'


print(removeX('pxthon', len('pxthon')))
