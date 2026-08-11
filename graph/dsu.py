class DSU:
    def __init__ (self,n):
        self.parent = list(range(n))
        self.rank = [0] * n

    def find(self,x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self,x,y):
        px,py = self.find(x),self.find(y)

        if px == py:
            return False

        if self.rank[px] < self.rank[py]:
            self.parent[px] = py

        elif self.rank[px] > self.rank[py]:
            self.parent[py] = px

        else:
            self.parent[py] = px
            self.rank[px] += 1

        return True

dsu = DSU(5)
print(dsu.union(0,1))
print(dsu.union(1,2))
print(dsu.union(3,4))

print(dsu.find(1))