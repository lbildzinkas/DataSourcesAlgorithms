# Use 2 stacks to implement a queue

class Queue2Stacks(object):
    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    def enqueue(self, element):
        if not self.stack1:
            self.stack1.append(element)
            return

        self.stack2.append(element)

    def dequeue(self):
        out = self.stack1.pop()

        if not self.stack2 == []:

            for i in range(len(self.stack2)-1):
                self.stack1.append(self.stack2.pop())

            temp = self.stack2.pop()

            for i in range(len(self.stack1)):
                self.stack2.append(self.stack1.pop())

            self.stack1.append(temp)

        return out


queue = Queue2Stacks()

queue.enqueue(1)

queue.enqueue(2)

queue.enqueue(3)

queue.enqueue(4)

queue.enqueue(5)

print(queue.dequeue())

print(queue.dequeue())

print(queue.dequeue())

print(queue.dequeue())

print(queue.dequeue())
