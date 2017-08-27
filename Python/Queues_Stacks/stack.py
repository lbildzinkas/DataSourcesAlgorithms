# Stack implementation in Python

class Stack(object):
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return len(self.items) == 0

    def push(self, item):
        self.items.append(item)

    def pop(self):
        self.items.pop()

    def peek(self):
        return self.items[len(self.items)-1]

    def length(self):
        return len(self.items)


stk = Stack()

stk.push(9)
print(stk.peek())
print(stk.length())
stk.push(8)
print(stk.peek())
print(stk.length())
stk.pop()
print(stk.peek())
print(stk.length())
