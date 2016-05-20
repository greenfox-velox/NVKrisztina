word = 'dog goat dad duck doodle never'

def palindrome(word):
    empty = []
    for n in range(len(word)):
        for i in range(len(word)):
            a = word[n: n + i + 3]
            if a == a[::-1] and len(a) >= 3:
                empty.append(a)
    print (empty)

palindrome(word)
