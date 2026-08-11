from collections import deque
import math

# graph creation
graph = {
    10 : [40,20],
    20 : [10,35,60,70,80],
    25 : [35],
    35 : [20,25,40,50],
    40 : [10,35],
    50 : [35],
    60 : [20,80,90],
    70 : [20,80],
    80 : [20,60,70],
    90 : [60]
}

def multi_source_bfs(graph,sources):
    distance = {node : math.inf for node in graph}
    queue = deque()

    for source in sources:
        distance[source] = 0
        queue.append(source)

    while queue:
        curr = queue.popleft()
        for neighbour in graph[curr]:
            if distance[neighbour] == math.inf:  # it means if node(neighbour) is not visited then:
                distance[neighbour] = distance[curr] + 1     # update the distance of that neighbour
                queue.append(neighbour)     # And add that neighbour in queue 

    return distance

# calling 
print(multi_source_bfs(graph,[10,25,35]))

