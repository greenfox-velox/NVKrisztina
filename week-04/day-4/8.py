# 8. Given a string, compute recursively a new string where all the 'x' chars have been removed.

def removeX(input, n):
    if n == 0:
        return ''
    elif input[n - 1] != 'x':
        return removeX(input, n - 1) + input[n - 1]
    elif input[n - 1] == 'x':
        return removeX(input, n - 1) + ''


print(removeX('pxthon', len('pxthon')))
