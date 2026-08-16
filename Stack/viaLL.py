# implementing stack via LinkedList

class Node:
    def __init__(self,val):
        self.val = val
        self.next = None

class StackUsingLL:
    def __init__(self):
        self.top = None

    def is_empty(self):
        return self.top == None

    def display(self):
        if self.is_empty():
            print("Empty list")
            return
        curr = self.top
        while curr:
            print(curr.val,end=' ')
            curr = curr.next
        print("\n")

    def push(self,val):
        node = Node(val)
        node.next = self.top
        self.top = node
        self.display()

    def pop(self):
        if self.is_empty():
            print("Empty List")
            return
        popped = self.top.val
        self.top = self.top.next
        self.display()

    def peek(self):
        if self.is_empty():
            print("Empty List")
            return
        print(f"peek Element : {self.top.val}")


stack = StackUsingLL()
stack.push(1)
stack.push(2)
stack.push(3)
stack.push(4)
stack.push(5)

stack.display()

stack.pop()
stack.pop()
stack.peek()

