word = 'pxthon'

def changeChar(length):
    if word[length - 1] == 'x':
        return 'y' + changeChar(length - 1)
    else:
        return word[length - changeChar(length - 1)]


changeChar(len(word))
