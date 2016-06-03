import csv

def text_open(filename):
        array = []
        ifile = open(filename, 'r')
        nextLine = ifile.readline()
        while nextLine != "":
            array.append(nextLine.split(','))
            nextLine = ifile.readline()
        ifile.close()
        return array

print(text_open('new_csv.csv'))
