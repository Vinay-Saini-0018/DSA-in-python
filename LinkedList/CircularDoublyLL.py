class Node:
    def __init__(self,val):
        self.val = val
        self.prev = None
        self.next = None

class CircularDoublyLL:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def is_empty(self):
        return self.head is None

    def display_forward(self):
        if self.is_empty():
            print("Empty List")
            return
        else:
            curr = self.head
            while True:
                print(curr.val,end=' ')
                curr = curr.next
                if curr == self.head:
                    break
            print('\n')

    def display_backward(self):
        if self.is_empty():
            print("Empty List")
            return
        else:
            curr = self.tail
            while True:
                print(curr.val,end=' ')
                curr = curr.prev
                if curr == self.tail:
                    break
            print('\n')

    # --------- insertion ---------

    def insert_at_beginning(self,val):
        node = Node(val)
        if self.is_empty():
            self.head = self.tail = node
            node.next = node.prev = node
        else:
            node.next = self.head
            node.prev = self.tail
            self.tail.next = node
            self.head.prev = node
            self.head = node

        self.length += 1
        self.display_forward()

    def insert_at_end(self,val):
        node = Node(val)
        if self.is_empty():
            self.head = self.tail = node
            node.next = node.prev = node
        else:
            node.next = self.head
            node.prev = self.tail
            self.tail.next = node
            self.head.prev = node
            self.tail = node

        self.length += 1
        self.display_forward()

    def insert_in_middle(self,pos,val):
        node = Node(val)
        n = self.length
        if (pos<0) or (pos>n):
            print("Invalid position")
            return
        elif pos == 0:
            self.insert_at_beginning()
        elif pos == 1:
            self.insert_at_end()
        else:
            node = Node(val)
            p = self.head
            for _ in range(pos):
                p = p.next
            q = p.prev
            q.next = node
            p.prev = node
            node.prev = q
            node.next = p

            self.length += 1
            self.display_forward()

    # --------- Searching ----------
    
    def search(self,key):
        if self.is_empty():
            print("Empty list")
            return
        curr = self.head
        pos = 0

        while True:
            if curr.val == key:
                print(f"{key} found at pos {pos}")
                return
            curr = curr.next
            pos += 1

            if curr == self.head:
                print(f"{key} not found")
                break

    # ---------- Deletion -------------

    def delete_at_beginning(self):
        if self.is_empty():
            print("Empty list")
            return
        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            curr = self.head
            self.head = curr.next
            self.head.prev = self.tail
            self.tail.next = self.head
            
        self.length -= 1
        self.display_forward()

    def delete_at_end(self):
        if self.is_empty():
            print("Empty list")
            return
        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            curr = self.tail
            self.tail = curr.prev
            self.tail.next = self.head
            self.head.prev = self.tail

        self.length -= 1
        self.display_forward()

    def delete_in_middle(self,pos):
        n = self.length
        if (pos < 0) or (pos > n):
            print("Invalid position ")
            return
        elif pos == 0:
            self.delete_at_beginning()
        elif pos == n-1:
            self.delete_at_end()
        else:
            p = self.head
            for _ in range(pos):
                p = p.next
            q = p.prev

            q.next = p.next
            p.next.prev = q
            p.next = p.prev = None

            self.length -= 1
            self.display_forward()

# Function calling
sll = CircularDoublyLL()
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
