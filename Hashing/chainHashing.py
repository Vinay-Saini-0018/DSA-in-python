class ChainingHashTable:
    def __init__(self,size=5):
        self.size = size
        self.table = [[] for _ in range(self.size)]   # List of lists

    # return the hash_value(index value) of the table
    def hash_function(self,key):
        return sum(ord(ch) for ch in key) % self.size

    # insert (key,value) in the table
    def insert(self,key,value=None):
        index = self.hash_function((key))

        # if key already exist then updating that
        for i,(k,v) in enumerate(self.table[index]):
            if k == key:
                self.table[index[i]] = (key,value)
                return

        # adding (key,value) in the table
        self.table[index].append((key,value))


    # searching the value of key in the hash_table
    def search(self,key):
        index = self.hash_function(key)

        for (k,v) in self.table[index]:
            if k == key:
                return v

            return None


    # Display hash table
    def display(self):
        for i, bucket in enumerate(self.table):
            print(f" {i} : {bucket}")

hash_table = ChainingHashTable(3)
hash_table.insert("apple",10)
hash_table.insert("boy",20)
hash_table.insert("cat",30)
hash_table.insert("dog",40)
hash_table.insert("Ronit",50)
hash_table.insert("Nitin",60)
hash_table.insert("Vinay",70)

hash_table.display()