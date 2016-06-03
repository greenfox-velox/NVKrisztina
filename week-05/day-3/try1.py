import sys
import csv

class ToDo:

    def __init__(self, filename, this_filename, s):
        self.filename = filename
        self.this_filename = this_filename
        self.s = s
        self.text = self.textopen()

    def use(self):
        if len(self.this_filename) == 1:
            print('Python Todo application\n'
            '=======================\n'

            'Command line arguments:\n'
             '-l   Lists all the tasks\n'
             '-a   Adds a new task\n'
             '-r   Removes a task\n'
             '-c   Completes a task\n')

    def textopen(self):
        try:
            ifile = open(self.filename)
            text1 = csv.reader(ifile)
            self.text = []
            for i in text1:
                self.text = self.text + [i[2]]
            return self.text
        except FileNotFoundError:
            k = open(self.filename, 'w')
            k.write('')
            k.close()
            return ''

    def text_open2(filename):
            array = []
            ifile = open(filename, 'r')
            nextLine = ifile.readline()
            while nextLine != "":
                array.append(nextLine.split(','))
                nextLine = ifile.readline()
            ifile.close()
            return array


    def text_open1(self, s):
            ifile = open(self.filename, 'w')
            text = csv.writer(ifile)
            text.writerows(s)

    def list_print(self):
        text = self.textopen()
        if text != '':
            if self.this_filename[1] == '-l':
                for i in range(len(text)):
                    print ((str(i + 1) + ' ' + text[i]).rstrip())
        else:
            print ('No todos for today! :)')

    def list_append(self):
        if self.this_filename[1] == '-a':
            try:
                if self.this_filename[2]:
                    self.text.append(self.this_filename[2])
                    self.text_open1(s)
            except:
                print ('Unable to add: No task is provided')

    def list_remove(self):
        print (self.text)
        s2 = ''
        if self.this_filename[1] == '-r':
            if len(self.this_filename) == 3:
                try:
                    if int(self.this_filename[2]):
                        if len(self.text) >= int(self.this_filename[2]):
                            for n in range(0, len(self.text) -1):
                                if int(self.this_filename[2]) - 1 == n:
                                    print (self.text)
                                    cica = self.text
                                    print (n)
                                    print (cica[n])
                                    cica.remove(cica[n])
                                    s2 = s2 + str(cica)
                                    print (s2)
                            self.text_open1(s2)
                        else:
                            print ('3 Unable to remove: Index is out of bound')
                except:
                    print ('2 Unable to remove: Index is not a number')
            else:
                print ('1 Unable to remove: No index is provided')

    def text_open_aslist(self):
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

    def list_check(self):
        if self.this_filename[1] == '-c':
            if len(self.this_filename) == 3:
                try:
                    if int(self.this_filename[2]):
                        if len(self.text) >= int(self.this_filename[2]):
                            for n in range(len(self.text)):
                                if int(self.this_filename[2]) - 1 == int(n):
                                    self.text[n][1] = 'True'
                                    self.text_open1(s)
                                print (self.text[n])
                        else:
                            print ('Unable to check: Index is out of bound')
                except FileNotFoundError:
                    print ('Unable to check: Index is not a number')
            else:
                print ('Unable to check: No index is provided')

    def list_ignore(self):
        text = self.textopen()
        if self.this_filename[1] != '-l':
            if self.this_filename[1] != '-a':
                if self.this_filename[1] != '-r':
                    if self.this_filename[1] != '-c':
                        print ('Unsupported argument')
                        return self.use()

    def execute(self):
        if len(sys.argv) == 1:
            return self.use()
        elif self.this_filename[1] == '-l':
            self.list_print()
        elif self.this_filename[1] == '-a':
            self.list_append()
        elif self.this_filename[1] == '-r':
            self.list_remove()
        elif self.this_filename[1] == '-c':
            self.list_check()
        else:
            self.list_ignore()

this_toDo = ToDo('list.csv', sys.argv, '')

this_toDo.execute()
