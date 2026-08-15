class Node:
    def __init__(self,val):
        self.val = val
        self.next = None

class CircularSinglyLinkedList:
    def __init__(self):
        self.head = None
        self.length = 0

    def is_empty(self):
        return self.head is None

    def display(self):
        if self.is_empty():
            print("Empty List")
        else:
            curr = self.head
            while True:
                print(curr.val,end = ' ')
                curr = curr.next
                if curr == self.head:
                    break
            print('\n')

    #  ----------  Insertion  -----------

    def insert_at_beginning(self,value):
        node = Node(value)
        if self.is_empty():
            self.head = node
            node.next = self.head

        else:
            curr = self.head
            while curr.next != self.head:
                curr = curr.next
            curr.next = node
            node.next = self.head
            self.head = node
        self.length += 1
        self.display()

    def insert_at_end(self,value):
        node = Node(value)
        if self.is_empty():
            self.head = node
            node.next = self.head

        else :
            curr = self.head
            while curr.next != self.head:
                curr = curr.next
            curr.next = node
            node.next = self.head
        self.length += 1
        self.display()

    def insert_in_middle(self,pos,value):
        n = self.length
        if (pos < 0) or (pos > n):
            print("Invalide Position")
        elif pos == 0:
            self.insert_at_beginning(value)
        elif pos == n:
            self.insert_at_end(value)
        else:
            node = Node(value)
            curr = self.head
            for _ in range(pos-1):
                curr = curr.next
            node.next = curr.next
            curr.next = node
            self.length += 1
            self.display()

    # -------- Searching ---------

    def search(self,key):
        if self.is_empty():
            print("Empty List")

        pos = 0
        curr = self.head
        # while curr != self.head:     if we do this then loop ends in the starting
        while True:
            if curr.val == key:
                print(f"{key} found at pos {pos}")
                return
            pos += 1
            curr = curr.next
            if curr == self.head:
                print(f"{key} not found")
                break

    # --------- deletion ----------

    def delete_at_beginning(self):
        if self.is_empty():
            print('Empty List')
        if self.length == 1:
            self.head = None
        else:
            curr = self.head
            while curr.next != self.head:
                curr = curr.next
            self.head = self.head.next
            curr.next = self.head

        self.length -= 1
        self.display()

    def delete_at_end(self):
        if self.is_empty():
            print("Empty List")

        if self.length == 1:
            self.head = None
        else:
            q = None
            p = self.head
            while p.next != self.head:
                q = p
                p = p.next
            q.next = self.head
            p.next = None

        self.length -= 1
        self.display()


    def delete_in_middle(self,pos):
        n = self.length
        if self.is_empty():
            print("Empty List")

        if (pos < 0) or (pos > n):
            print("Invalid Position")
        elif pos == 0:
            self.delete_at_beginning()
        elif pos == n-1:
            self.delete_at_end()
        else:
            q = None
            p = self.head

            for _ in range(pos):
                q = p
                p = p.next
            q.next = p.next
            p.next = None
        self.length -= 1
        self.display()

# Function calling
sll = CircularSinglyLinkedList()
sll.insert_at_beginning(5)
sll.insert_at_beginning(4)
sll.insert_at_beginning(3)
sll.insert_at_end(7)
sll.insert_at_end(8)
sll.insert_at_end(9)
sll.insert_in_middle(3,6)

sll.search(7)

sll.delete_at_beginning()
sll.delete_at_end()
sll.delete_in_middle(1)


