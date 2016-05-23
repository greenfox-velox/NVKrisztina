# Create a method that decrypts texts/reversed_zen_order.txt
def decrypt(file_name):
    f = open(file_name)
    text = f.readlines()
    l = text[::-1]
    s = ''
    s = " ".join(l)
    s = s + '.'
    print (s)

decrypt('texts/reversed_zen_order.txt')
