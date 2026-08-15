class Node:
    def __init__(self,val):
        self.val = val
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None

    def getLength(self):
        length = 0

        curr = self.head
        while curr:
            length += 1
            curr = curr.next

        return length

    def display(self):
        if not self.head:
            print("Empty List")
        else:
            curr = self.head
            while curr:
                print(curr.val,end = ' ')
                curr = curr.next
            print('\n')

    #  ----------  Insertion  -----------

    def insert_at_beginning(self,value):
        node = Node(value)
        if self.head:
            node.next = self.head

        self.head = node
        self.display()

    def insert_at_end(self,value):
        node = Node(value)
        if not self.head:
            self.head = node
        else :
            curr = self.head
            while curr.next:
                curr = curr.next
            curr.next = node

        self.display()

    def insert_in_middle(self,pos,value):
        n = self.getLength()
        if (pos < 0) or (pos > n):
            print("Invalide Position")
        elif pos == 0:
            self.insert_at_beginning(value)
        elif pos == n:
            self.insert_at_end(value)
        else:
            node = Node(value)
            p = self.head
            q = None
            for _ in range(pos):
                q = p
                p = p.next
            q.next = node
            node.next = p
            self.display()

    # -------- Searching ---------

    def search(self,key):
        if not self.head:
            print("Empty List")

        pos = 0
        curr = self.head
        while curr:
            if curr.val == key:
                return (f"{key} found at pos {pos}")
            pos += 1
            curr = curr.next
        return ("key not found")

    # --------- deletion ----------

    def delete_at_beginning(self):
        if self.head:
            curr = self.head
            self.head = curr.next
            curr.next = None
            self.display()
        else:
            print("Empty List")

    def delete_at_end(self):
        if not self.head:
            print("Empty List")
        else:
            ''' This code will not work if there is only one node present in List -->
            curr = self.head
            while curr.next.next:
                curr = curr.next
            curr.next = None
            self.display()'''

            p = self.head
            q = None
            while p.next:
                q = p
                p = p.next
            if p == self.head:
                self.head = None
            else:
                q.next = None
            self.display()

    def delete_in_middle(self,pos):
        n = self.getLength()
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
            self.display()

# Function calling
sll = SinglyLinkedList()
sll.insert_at_beginning(5)
sll.insert_at_beginning(4)
sll.insert_at_beginning(3)
sll.insert_at_end(7)
sll.insert_at_end(8)
sll.insert_at_end(9)
sll.insert_in_middle(3,6)

print(sll.search(7))

sll.delete_at_beginning()
sll.delete_at_end()
sll.delete_in_middle(1)


