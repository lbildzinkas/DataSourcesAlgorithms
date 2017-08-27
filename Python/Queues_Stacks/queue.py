class Queue:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return len(self.items) == 0

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        if self.isEmpty():
            return
        ret = self.items[0]
        self.items = self.items[1:len(self.items)]
        return ret

    def size(self):
        return len(self.items)


que = Queue()
que.enqueue(1)
print(que.size())
que.enqueue(2)
print(que.size())
print(que.dequeue())
print(que.size())

