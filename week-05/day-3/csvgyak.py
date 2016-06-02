import csv

ifile = open('todos_done.csv', 'rt')
read = csv.reader(ifile)
for row in read:
    print(row)
