import sys
import csv

class ToDo:

    def __init__(self, filename, this_filename, s):
        self.filename = filename
        self.this_filename = this_filename
        self.s = s
        self.text = self.text_open()

    def use(self):
        if len(self.this_filename) == 1:
            print('Python Todo application\n'
            '=======================\n'

            'Command line arguments:\n'
             '-l   Lists all the tasks\n'
             '-a   Adds a new task\n'
             '-r   Removes a task\n'
             '-c   Completes a task\n')

    def text_open(self):
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

    def text_open1(self, s):
            ifile = open(self.filename, 'w')
            text = csv.writer(ifile)
            text.writerows(s)

    def list_print(self):
        text = self.text_open()
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
        s = ''
        if self.this_filename[1] == '-r':
            if len(self.this_filename) == 3:
                try:
                    if int(self.this_filename[2]):
                        if len(self.text) >= int(self.this_filename[2]):
                            for n in range(len(self.text)):
                                if int(self.this_filename[2]) - 1 == int(n):
                                    s = s + str(self.text.remove(self.text[n]))
                                    self.text_open1(s)
                        else:
                            print ('Unable to remove: Index is out of bound')
                except FileNotFoundError:
                    print ('Unable to remove: Index is not a number')
            else:
                print ('Unable to remove: No index is provided')

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
        text = self.text_open()
        if self.this_filename[1] != '-l':
            if self.this_filename[1] != '-a':
                if self.this_filename[1] != '-r':
                    if self.this_filename[1] != '-c':
                        print ('Unsupported argument')
                        return self.use()

    def list_write(self):
        self.text_open1(self.s)
        print (self.s)


    def execute(self):
        if len(sys.argv) == 1:
            return self.use()
        self.list_print()
        self.list_append()
        self.list_remove()
        self.list_ignore()
        self.list_check()
        self.list_write()

this_toDo = ToDo('list.csv', sys.argv, '')

this_toDo.execute()
