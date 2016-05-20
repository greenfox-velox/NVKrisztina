class Stack:

    def __init__(self):
        self.contents = []

    def size(self):
        summa = 0
        for n in self.contents:
            summa = self.contents[n] + summa

    def push(self, item):
        self.contents.append(item)

    def pop(self):
        del self.contents[-1]
        print (self.contents)

stack1 = Stack()

stack1.size()
stack1.push(3)
stack1.pop()
