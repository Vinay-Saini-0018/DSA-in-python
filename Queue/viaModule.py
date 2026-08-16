# Implementing queue via collections Module

from collections import deque

class QueueUsingCollections:
    def __init__(self):
        self.queue = deque()

    def is_empty(self):
        return len(self.queue) == 0

    def display(self):
        if self.is_empty():
            print("Empty queue")
            return
        print(self.queue)

    def enqueue(self,val):
        self.queue.append(val)
        self.display()

    def dequeue(self):
        if self.is_empty():
            print("Empty queue")
            return
        self.queue.popleft()
        self.display()

    def frontpeek(self):
        if self.is_empty():
            print('Empty queue')
            return
        else:
            print(self.queue[0])

    def rearpeek(self):
        if self.is_empty():
            print('Empty queue')
            return
        else:
            print(self.queue[-1])

queue = QueueUsingCollections()
queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)
queue.enqueue(4)
queue.enqueue(5)

print(queue.is_empty())

queue.dequeue()
queue.dequeue()

queue.rearpeek()   # insertion side
queue.frontpeek()   # deletion side