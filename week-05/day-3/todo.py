
print('Python Todo application\n'
'=======================\n'

'Command line arguments:\n'
 '-l   Lists all the tasks\n'
 '-a   Adds a new task\n'
 '-r   Removes an task\n'
 '-c   Completes an task\n')

import sys

def list_opener(filename):
    f = open(filename)
    text = f.read()
    f.close()
    if sys.argv[1] == '-l':
        print (text)



list_opener('todos_stored.txt')
