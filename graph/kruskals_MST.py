edges = [
    (11,1,6),
    (27,1,2),
    (24,6,5),
    (23,5,7),
    (22,5,4),
    (13,2,7),
    (17,7,4),
    (15,2,3),
    (12,3,4)
]

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

def kruskals(n,edges):
    edges.sort()
    dsu = DSU(n)
    mst = []
    total_cost = 0

    for weight,u,v in edges:
        if dsu.union(u,v):
            mst.append((u,v,weight))
            total_cost += weight

    return mst,total_cost

# calling the kruskals function
mst,cost = kruskals(8,edges)

print('Edges in Mst: ')
for u,v,w in mst:
    print(f'{u}----{v} == {w}')

print(f"total-cost = {cost}")