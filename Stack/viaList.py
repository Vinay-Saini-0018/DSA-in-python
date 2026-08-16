class Stack:
    def __init__(self):
        self.stack = []

    def get_size(self):
        return len(self.stack)

    def is_empty(self):
        return self.get_size == 0

    def display(self):
        if self.is_empty():
            print("Empty List")
            return
        else:
            for ele in self.stack[ : : -1]:
                print(ele,end=' ')
            print("\n")

    def push(self,val):
        self.stack.append(val)
        self.display()

    def pop(self):
        if self.is_empty():
            print("Empty List")
            return
        self.stack.pop()
        self.display()

    def peek(self):
        if self.is_empty():
            print("Empty List")
            return
        print(self.stack[-1])

stack = Stack()
stack.push(1)
stack.push(2)
stack.push(3)
stack.push(4)
stack.push(5)

stack.display()
print(stack.get_size())

stack.pop()
stack.pop()
stack.peek()