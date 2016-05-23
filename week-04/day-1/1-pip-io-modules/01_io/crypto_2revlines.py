# Create a method that decrypts texts/reversed_zen_lines.txt
def decrypt(file_name):
    f = open(file_name)
    text = f.read()
    print (text[::-1])



decrypt('texts/reversed_zen_lines.txt')
