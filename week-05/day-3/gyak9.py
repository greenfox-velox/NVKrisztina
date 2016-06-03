import csv

def text_open1(filename):
        ifile = open(filename, 'w')
        text = csv.writer(ifile)
        text.writerows(s)
        print (text)
test_open1('new_csv.csv')
