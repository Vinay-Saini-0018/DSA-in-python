from collections import defaultdict
import math

v = 7

# edges
edges = [
    (1,2,6), 
    (1,3,5),
    (1,4,5),
    (4,3,-2),
    (3,2,-2),
    (2,5,-1),
    (3,5,1),
    (5,7,3),
    (4,6,-1),
    (6,7,3)
]

# dictionary with default value = empty list
graph = defaultdict(list)

for u,v,w in edges:
    graph[u].append((v,w))

# sort based on key value and print 
for node in sorted(graph):
    print(f"{node} -> {graph[node]}")

# bellman function
def bellman_ford(v,edges,source):
    distance = [math.inf] * (v+1)
    distance[source] = 0

    # In each iteration we work on every edge 
    for i in range(v-1):
        print(f'Iteration : {i+1}')

        for u,v,w in edges:
            if (distance[u] != math.inf) and (distance[u] + w < distance[v]):
                distance[v] = distance[u] + w
                print(f"updated distance[{v}] to {distance[v]}")

        print('Distances : ',distance[1:])
        print('-'*40)

    # checking all the edges one more time
    for u,v,w in edges:
        if (distance[u] != math.inf) and (distance[u] + w < distance[v]):
            print('Negative Cycle Detected')
            return None

    return distance[1:]

# calling thata function
print(bellman_ford(v,edges,1))