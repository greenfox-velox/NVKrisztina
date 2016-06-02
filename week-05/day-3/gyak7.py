import sys

def use(this_filename):
    print('Python Todo application\n'
    '=======================\n'

    'Command line arguments:\n'
     '-l   Lists all the tasks\n'
     '-a   Adds a new task\n'
     '-r   Removes a task\n'
     '-c   Completes a task\n')

def text_open(filename):
    try:
        ifile = open('todos_done.csv', 'rt')
        text = csv.reader(ifile)
        return text
    except FileNotFoundError:
        k = open('new_file.csv', 'w')
        k.write('')
        k.close()
        return ''

def list_print(filename):
    ifile = open('todos_done.csv', 'rt')
    read = csv.reader(ifile)
    if read != '':
        if sys.argv[1] == '-l':
            for row in read:
                print(row)
    else:
        print ('No todos for today! :)')

def list_append(filename):
    text=text_open(filename)
    if sys.argv[1] == '-a':
        try:
            if sys.argv[2]:
                text.append(sys.argv[2])
                print (text)
        except:
            print ('Unable to add: No task is provided')

def list_remove(filename):
    text=text_open(filename)
    if sys.argv[1] == '-r':
        if len(sys.argv) == 3:
            try:
                if int(sys.argv[2]):
                    if len(text) >= int(sys.argv[2]):
                        for n in range(len(text)):
                            if int(sys.argv[2]) - 1 == int(n):
                                text.remove(text[n])
                                print (text)
                    else:
                        print ('Unable to remove: Index is out of bound')
            except:
                print ('Unable to remove: Index is not a number')
        else:
            print ('Unable to remove: No index is provided')

def list_ignore(filename):
    text=text_open(filename)
    if sys.argv[1] != '-l':
        if sys.argv[1] != '-a':
            if sys.argv[1] != '-r':
                print ('Unsupported argument')
                return use(sys.argv)

def execute(filename):
    if len(sys.argv) == 1:
        return use(sys.argv)
    list_print(filename)
    list_append(filename)
    list_remove(filename)
    list_ignore(filename)
execute('todos_stored.txt')
