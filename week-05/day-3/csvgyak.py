import csv
"""
def text_open(filename):
    try:
        ifile = open(filename)
        text = csv.reader(ifile)
        y = []
        for i in text:
            y = y + i
        return (y)
    except FileNotFoundError:
        k = open(filename, 'w')
        k.write('')
        k.close()
        return ''
print(text_open('todos_done.csv'))
"""
def text_open_aslist(filename):
    try:
        ifile = open(filename)
        text = csv.reader(ifile)
        l = []
        for i in text:
            l = l + [i]
        return l
    except FileNotFoundError:
        k = open(filename, 'w')
        k.write('')
        k.close()
        return ''
text_open_aslist('new_csv.csv')

def x(filename):
    l = text_open(filename)
    for j in l:
        if j[1] == 'True':
            print ('[x]')
        else:
            print ('[ ]')

x('new_csv.csv')
