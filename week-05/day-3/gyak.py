import sys

print(sys.argv)

for arg in sys.argv:
    print (arg)



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
    if sys.argv != []:
        if sys.argv[1] == '-l':
            print (text)
    if sys.argv == []:
        print ('No todos for today! :)')

list_opener('todos_stored.txt')

if text != '':
    if sys.argv[1] == '-l':
        print (text)
else:
    print ('No todos for today! :)')
if sys.argv[1] == '-a' + str(input):
    print(text + (input))


if sys.argv[1] == []:
    return commands(sys.argv)
elif text != '':
    if sys.argv[1] == '-l':
        print (text)
else:
    print ('No todos for today! :)')
if sys.argv[1] == '-a' + str(input):
    print(text + (input))
