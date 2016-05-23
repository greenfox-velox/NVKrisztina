# Create a method that decrypts the texts/duplicated_chars.txt

def decrypt(file_name):
    f = open(file_name, 'r')
    text = f.readlines()
    t = ''
    for line in text:
        for i in line.strip('\n')[::2]:
            t += i
        t += '\n'
    print (t)

decrypt('texts/duplicated_chars.txt')
