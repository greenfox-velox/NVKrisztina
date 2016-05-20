
x = ""
word = input("Write a word!")
x = word
for n in range(len(word)):
    x = x + word[len(word) - (n + 1)]
print (x)


x = ""
word = input("Write a word!")
for n in range(len(word)):
    x = word
    x = x + word[len(word) - (n + 1)]
print (x)





"""
x = ""
word = input("Write a word!")
for n in range(len(word)):
    word = word + word[len(word) - ((n + 1) * 2) - 3]
print (word)
"""
