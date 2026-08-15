class Node:
    def __init__(self,value):
        self.val = value
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def is_empty(self):
        return self.head is None

    def display_forward(self):
        if self.is_empty():
            print("Empty List")
        else:
            curr = self.head
            while curr:
                print(curr.val,end = " ")
                curr = curr.next
            print('\n')

    def display_backward(self):
        if self.is_empty():
            print("Empty List")

        else:
            curr = self.tail
            while curr:
                print(curr.val, end = " ")
                curr = curr.prev
            print('\n')

    # ----------- insertion ------------

    def insert_at_beginning(self,val):
        node = Node(val)
        if self.is_empty():
            self.head = node
            self.tail = node
        else:
            node.next = self.head
            self.head.prev = node
            self.head = node
        self.length += 1
        self.display_forward()

    def insert_at_end(self,val):
        node = Node(val)
        if self.is_empty():
            self.head = node
            self.tail = node
        else:
            self.tail.next = node
            node.prev = self.tail
            self.tail = node

        self.length += 1
        self.display_forward()

    def insert_in_middle(self,pos,val):
        n = self.length
        if (pos<0) or (pos>n):
            print("Invalid position")
            return
        elif pos == 0:
            self.insert_at_beginning(val)
        elif pos == n:
            self.insert_at_end(val)

        else:
            node = Node(val)
            p = self.head
            for _ in range(pos):
                p = p.next
            q = p.prev
            q.next = node
            node.prev = q
            node.next = p
            p.prev = node

            self.length += 1
            self.display_forward()

    # ----------- searching ------------

    def search(self,key):
        if self.is_empty():
            print("empty list")
            return
        else:
            pos = 0
            curr = self.head
            while curr:
                if curr.val == key:
                    print(f"{key} found at pos {pos}")
                    return
                pos += 1
                curr = curr.next
            print(f"{key} not found")

    # ----------- deletion -----------

    def delete_at_beginning(self):
        if self.is_empty():
            print("Empty List")
            return
        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            curr = self.head

            self.head = curr.next
            self.head.prev = None   # new head ka next
            curr.next = None
        self.length -= 1
        self.display_forward()

    def delete_at_end(self):
        if self.is_empty():
            print("Empty List")
            return
        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            curr = self.tail

            self.tail = curr.prev
            self.tail.next = None
            curr.prev = None

        self.length -= 1
        self.display_forward()

    def delete_in_middle(self,pos):
        n = self.length
        if self.is_empty():
            print("Empty List")
            return
        if (pos < 0) or (pos > n-1):
            print("Invalid position")
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
            p.prev = None
            p.next = None

            self.length -= 1
            self.display_forward()

# Function calling
sll = DoublyLinkedList()
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