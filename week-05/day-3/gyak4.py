def text_open(filename):
    import os.path
    os.path.exists(filename)
    try:
        f = open(filename)
        text = f.readlines()
        f.close()
    except FileNotFoundError:
        k = open('new_file.txt', 'w')
        text = k.write('jifojweio')
        k.close()
text_open('todos_stored.txt')
