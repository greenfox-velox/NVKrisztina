import sys

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
                text.append(sys.argv[2])
                print (text)
        except:
            print ('Unable to add: No task is provided')
    if sys.argv[1] == '-r' and len(sys.argv) == 3:
        if len(text) >= int(sys.argv[2]):
            for n in range(len(text)):
                if int(sys.argv[2]) - 1 == int(n):
                    text.remove(text[n])
                    print (text)
        else:
            print ('Unable to remove: Index is out of bound')
    else:
        print ('Unable to remove: No index is provided')

list_opener('todos_stored.txt')
