import sys

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
        import os.path
        os.path.exists(self.filename)
        try:
            f = open(self.filename)
            text = f.readlines()
            f.close()
            return text
        except FileNotFoundError:
            k = open('new_file.txt', 'w')
            text = k.write('')
            k.close()
            return text

    def list_print(self):
        f = open(self.filename)
        text = f.readlines()
        f.close()
        if text != '':
            if self.this_filename[1] == '-l':
                for i in range(len(text)):
                    print ((str(i + 1) + ' ' + text[i]).rstrip())
        else:
            print ('No todos for today! :)')

    def list_append(self):
        f = open(self.filename)
        text = f.readlines()
        f.close()
        if self.this_filename[1] == '-a':
            try:
                if self.this_filename[2]:
                    text.append(self.this_filename[2])
                    print (text)
            except:
                print ('Unable to add: No task is provided')

    def list_remove(self):
        f = open(self.filename)
        text = f.readlines()
        f.close()
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

    def list_ignore(self):
        f = open(self.filename)
        text = f.readlines()
        f.close()
        if self.this_filename[1] != '-l':
            if self.this_filename[1] != '-a':
                if self.this_filename[1] != '-r':
                    print ('Unsupported argument')
                    # return use(self.this_filename)

this_toDo = ToDo('todos_stored.txt', 'sys.argv')

this_toDo.list_print()
this_toDo.list_append()
this_toDo.list_remove()
this_toDo.list_ignore()
