# Linear probing
# Quadratic probing  -> change this only "index = (h+i) % self.size" in search function

class LinearProbingHashing:
    def __init__(self,size=5):
        self.size = size
        self.table = [None] * self.size

    def display(self):
        print(self.table)

    def hash_function(self,key):
        return sum(ord(ch) for ch in key) % self.size

    def insert(self,key):
        h = self.hash_function(key)

        for i in range(self.size):
            index = (h+i) % self.size

            if self.table[index] is None:
                self.table[index] = key
                print(f"key : {key} is inserted at index {index}")
                return True

            raise Exception('Table is full')

    def search(self,key):
        h = self.hash_function(key)
        for i in range(self.size):
            index = (h+i) % self.size
            if self.table[index] is None:
                return False
            if self.table[index] == key:
                return index

        return False

lph = LinearProbingHashing(3)
lph.insert('vinay')
lph.insert('ronit')
lph.insert('nitin')
lph.insert('vijay')

lph.display()