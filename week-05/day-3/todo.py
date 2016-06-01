import sys, getopt

def use(this_filename):
    print('Python Todo application\n'
    '=======================\n'

    'Command line arguments:\n'
     '-l   Lists all the tasks\n'
     '-a   Adds a new task\n'
     '-r   Removes a task\n'
     '-c   Completes a task\n')

def text_open(filename):
    f = open(filename)
    text = f.readlines()
    f.close()

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
    f = open(filename)
    text = f.readlines()
    f.close()
    if sys.argv[1] == '-a':
        try:
            if sys.argv[2]:
                text.append(sys.argv[2])
                print (text)
        except:
            print ('Unable to add: No task is provided')

def list_remove(filename):
    f = open(filename)
    text = f.readlines()
    f.close()
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

def execute(filename):
    text_open('todos_stored.txt')
    if len(sys.argv) == 1:
        return use(sys.argv)
    list_print('todos_stored.txt')
    list_append('todos_stored.txt')
    list_remove('todos_stored.txt')
execute('todos_stored.txt')
