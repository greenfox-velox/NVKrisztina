import csv

def text_open(filename):
    try:
        ifile = open(filename)
        text = csv.reader(ifile)
        y = []
        for i in text:
            y = y + [i]
        return (y)
    except FileNotFoundError:
        k = open(filename, 'w')
        k.write('')
        k.close()
        return ''
print(text_open('todos_done.csv'))
