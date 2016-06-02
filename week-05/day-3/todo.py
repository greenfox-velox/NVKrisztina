import sys
import csv

class ToDo:

    def __init__(self, filename, this_filename):
        self.filename = filename
        self.this_filename = this_filename

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
            text = []
            for i in text1:
                text = text + [i[2]]
            return (text)
        except FileNotFoundError:
            k = open(self.filename, 'w')
            k.write('')
            k.close()
            return ''

    def list_print(self):
        text = self.text_open()
        if text != '':
            if self.this_filename[1] == '-l':
                for i in range(len(text)):
                    print ((str(i + 1) + ' ' + text[i]).rstrip())
        else:
            print ('No todos for today! :)')

    def list_append(self):
        text = self.text_open()
        if self.this_filename[1] == '-a':
            try:
                if self.this_filename[2]:
                    text.append(self.this_filename[2])
                    print (text)
            except:
                print ('Unable to add: No task is provided')

    def list_remove(self):
        text = self.text_open()
        if self.this_filename[1] == '-r':
            if len(self.this_filename) == 3:
                try:
                    if int(self.this_filename[2]):
                        if len(text) >= int(self.this_filename[2]):
                            for n in range(len(text)):
                                if int(self.this_filename[2]) - 1 == int(n):
                                    text.remove(text[n])
                                    print (text)
                        else:
                            print ('Unable to remove: Index is out of bound')
                except:
                    print ('Unable to remove: Index is not a number')
            else:
                print ('Unable to remove: No index is provided')

    def list_check(self):
        text = self.text_open()
        if self.this_filename[1] == '-c':
            if len(self.this_filename) == 3:
                try:
                    if int(self.this_filename[2]):
                        if len(text) >= int(self.this_filename[2]):
                            for n in range(len(text)):
                                if int(self.this_filename[2]) - 1 == int(n):
                                    n = (str(n + 1) + ' ' + chr(91) + 'x' + chr(93) + ' ' + text[n]).rstrip()
                                print (n)    
                        else:
                            print ('Unable to check: Index is out of bound')
                except:
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

    def execute(self):
        if len(sys.argv) == 1:
            return self.use()
        self.list_print()
        self.list_append()
        self.list_remove()
        self.list_ignore()
        self.list_check()

this_toDo = ToDo('todos_done.csv', sys.argv)

this_toDo.execute()
