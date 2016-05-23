# Create a method that decrypts texts/encoded_zen_lines.txt
def decrypt(file_name):
    f = open(file_name)
    text = f.read()
    z = []
    for i in text:
        z.append(ord(i))
    e = []
    for j in z:
        j = j - 1
        e.append(j)
    p = ''
    for k in e:
        p = p + chr(k)
    print (p)


decrypt('texts/encoded_zen_lines.txt')
