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
    import os.path
    os.path.exists(filename)
    try:
        f = open(filename)
        text = f.readlines()
        f.close()
        return text
    except FileNotFoundError:
        k = open('new_file.txt', 'w')
        text = k.write('jifojweio')
        k.close()
        return text

def list_print(filename):
    f = open(filename)
    text = f.readlines()
    f.close()
    if text != '':
        if sys.argv[1] == '-l':
            for i in range(len(text)):
                print ((str(i + 1) + ' ' + text[i]).rstrip())
    else:
        print ('No todos for today! :)')

def list_append(filename):
    text_open(filename)
    if sys.argv[1] == '-a':
        try:
            if sys.argv[2]:
                text.append(sys.argv[2])
                print (text)
        except:
            print ('Unable to add: No task is provided')

def list_remove(filename):
    text_open(filename)
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
    text_open(filename)
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
