n = "Bela"
z = []

def char_codes(string):
    for q in string:
        z.append(ord(q))
    print (z)
char_codes(n)


o = [99, 99, 99, 99, 99]

def string(char_codes):
    p = ''
    for k in o:
        p = p + chr(k)
    print (p)
string(o)

e = ['Long', 'sentence']
def sentence(words):
    s = ''
    for j in words:
        s = " ".join(words)
    print (s)
sentence(e)
