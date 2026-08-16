# Implementing queue using Linked List

class Node:
    def __init__(self,value):
        self.val = value
        self.next = None

class QueueUsingLL:
    def __init__(self):
        self.front = self.rear = None

    def is_empty(self):
        return self.front == None

    def display(self):
        if self.is_empty():
            print("Empty queue")
            return
        curr = self.front
        while curr:
            print(curr.val,end=' ')
            curr = curr.next
        print("\n")

    def enqueue(self,val):
        node = Node(val)
        if self.is_empty():
            self.front = self.rear = node
        else:
            self.rear.next = node
            self.rear = node
        self.display()

    def dequeue(self):
        if self.is_empty():
            print("Empty queue")
            return
        else:
            self.front = self.front.next

            if not self.front:
                self.rear = None
        self.display()

    def frontpeek(self):
        if self.is_empty():
            print("Empty queue")
            return
        print(self.front.val)

    
    def rearpeek(self):
        if self.is_empty():
            print("Empty queue")
            return
        print(self.rear.val)

            
queue = QueueUsingLL()
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