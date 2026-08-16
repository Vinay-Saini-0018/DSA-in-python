# implementing queue using List

class QueueUsingList:
    def __init__(self):
        self.queue = []

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
        self.queue.pop(0)
        self.display()

    def frontpeek(self):
        if self.is_empty():
            print("Empty queue")
            return
        front = self.queue[0]
        print(front)

    def rearpeek(self):
        if self.is_empty():
            print("Empty queue")
            return
        rear = self.queue[-1]
        print(rear)

queue = QueueUsingList()
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
