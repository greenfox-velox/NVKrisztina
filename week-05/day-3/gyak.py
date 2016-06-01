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


if sys.argv[1] == '-r 2':
    print(sys.argv)



def list_opener(filename):
    f = open(filename)
    text = f.readlines()
    if len(sys.argv) == 1:
        return commands(sys.argv)
    if text != '':
        if sys.argv[1] == '-l':
            for i in range(len(text)):
                print (str(i + 1) + text[i])
    else:
        print ('No todos for today! :)')
    if sys.argv[1] == '-a':
        try:
            if sys.argv[2]:
                print(text + sys.argv[2])
        except:
            raise ValueError('Unable to add: No task is provided')
    if sys.argv[1] == '-r':
        try:
            if sys.argv[2] == int(2):
                print(sys.argv)
        except:
            pass




if sys.argv[1] == '-r':
    try:
        for n in range(len(text)):
            if int(sys.argv[2]) - 1 == int(n):
                text.remove(text[n])
        print (text)
    except:
        print ('Unable to remove: No index is provided')



if sys.argv[1] == '-a':
    try:
        if sys.argv[2]:
            text.append(sys.argv[2])
            print (text)
    except:
        print ('Unable to add: No task is provided')
if sys.argv[1] == '-r' and len(sys.argv) == 3:
    for n in range(len(text)):
        try:
            if int(sys.argv[2]) - 1 == int(n):
                text.remove(text[n])
                print (text)
        except:
            print('Unable to remove: Index is out of bound')
else:
    print ('Unable to remove: No index is provided')
