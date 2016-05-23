# 1. Create a method that reads all contents of a file when its name given as param
def readfile(file_name):
    fr = open(file_name)
    x = fr.read()
    fr.close()
    return x
readfile('texts/duplicated_chars.txt')

# 2. Create a method that gets a file_name and a number as param and reads the numberth line of the file
def readline(file_name, number):
    f = open(file_name)
    for i in range(number):
        y = f.readline()
    f.close()
    return y.rstrip()
readline('texts/duplicated_chars.txt', 3)

# 3. Create a method that gets a long sentence as param and gives back the contained words in a list
l = "Long sentence"

def words(sentence):
    e = sentence.split()
    b = e[-1]
    b = b[:-1]
    e[-1] = b
    return e
words(l)



# 4. Create a method that gets a list of words and creates a sentence with the words separated by spaces
e = ['Long', 'sentence']

def sentence(words):
    s = ''
    s = " ".join(words)
    s = s + '.'
    return s
sentence(e)

# 5. Create a method that gets a string and gives back the character codes in a list
n = "Bela"

def char_codes(string):
    z = []
    for q in string:
        z.append(ord(q))
    return z
char_codes(n)

# 6. Create a method that gets a list of integers and gives back a string which characters are created from the numbers used as character codes
o = [99, 99, 99, 99, 99]

def string(char_codes):
    p = ''
    for k in char_codes:
        p = p + chr(k)
    return p
string(o)
