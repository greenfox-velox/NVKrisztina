# write a function that takes a filename and returns the number of lines the
# file consists. It should return zero if the file not exists.

def count_lines(filename):
    try:
        f = open(filename)
        text = f.read()
        f.close()
        return len(text)
    except FileNotFoundError:
        return 0

print(count_lines('liba.txt'))
