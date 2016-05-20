word = input("Write a word!")

def palindrome(word):
    empty = []
    for n in range(len(word)):
        empty.append(word[len(word) - (n + 1)])
    new_word = ""
    for char in empty:
        new_word = new_word + char
    print (word + new_word)

palindrome(word)


x = ""
word = input("Write a word!")
x = word
for n in range(len(word)):
    x = x + word[len(word) - (n + 1)]
print (x)
