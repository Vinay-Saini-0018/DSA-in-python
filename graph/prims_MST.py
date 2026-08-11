graph = {
    1 : [(6,11),(2,27)],
    2 : [(1,27),(7,13),(3,15)],
    3 : [(2,15),(4,12)],
    4 : [(3,12),(5,22),(7,18)],
    5 : [(6,24),(7,23),(4,22)],
    6 : [(1,11),(5,24)],
    7 : [(2,13),(5,23),(4,18)]
}

import heapq

def prims(graph,start):
    visited = set()
    min_heap = [(0,start,-1)]
    mst = []     # stores the edges of Mst
    total_cost = 0

    while min_heap:
        weight,node,parent = heapq.heappop(min_heap)

        # this will prevent us from cycle creation
        if node in visited:
            continue           # if node in visited then go to next iteration of min_heap

        # if node not in visited then do this till the end     
        visited.add(node)
        total_cost += weight

        if parent != -1 :
            mst.append((parent,node,weight))

        # getting the neighbours of that node
        for neighbour,wt in graph[node]:
            if neighbour not in visited:
                heapq.heappush(min_heap, (wt,neighbour,node))

    return mst,total_cost

# calling this function
mst,cost = prims(graph,1)

# edges in mst
for u,v,w in mst:
    print(f'{u}---{v} == {w}')

print(f'total cost : {cost}')