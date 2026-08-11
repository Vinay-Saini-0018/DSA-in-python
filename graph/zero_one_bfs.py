from collections import deque
import math

graph = {
    10 : [(40,1),(20,1)],
    40 : [(10,1),(35,1)],
    35 : [(40,1),(50,1),(25,1),(20,1)],
    50 : [(35,1)],
    25 : [(35,1)],
    20 : [(10,1),(35,1),(60,1),(80,1),(70,1)],
    60 : [(20,0),(90,1),(80,1),(70,1)],
    90 : [(60,1)],
    80 : [(60,0),(20,1),(70,1)],
    70 : [(60,0),(20,1),(80,1)]
}

def zero_one_bfs(graph,source):
    distance = {node : math.inf for node in graph}
    dq = deque()

    distance[source] = 0
    dq.appendleft(source)

    while dq:
        curr = dq.popleft()
        for neighbour,weight in graph[curr]:
            if distance[curr] + weight < distance[neighbour]:
                distance[neighbour] = distance[curr] + weight

                # appending in queue based on conditon
                if weight == 0:
                    dq.appendleft(neighbour)
                else:
                    dq.append(neighbour)

    return distance

# calling this function
dist = zero_one_bfs(graph,10)
print(dist)