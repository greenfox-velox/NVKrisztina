import sys, getopt

def commands(this_filename):
    print('Python Todo application\n'
    '=======================\n'

    'Command line arguments:\n'
     '-l   Lists all the tasks\n'
     '-a   Adds a new task\n'
     '-r   Removes a task\n'
     '-c   Completes a task\n')


def list_opener(filename):
    f = open(filename)
    text = f.read()
    f.close()
    if len(sys.argv) == 1:
        return commands(sys.argv)
    if text != '':
        if sys.argv[1] == '-l':
            print (text)
    else:
        print ('No todos for today! :)')
    if sys.argv[1] == '-a':
        if sys.argv[2]:
            print(text + sys.argv[2])

list_opener('todos_stored.txt')
