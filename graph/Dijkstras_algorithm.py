# graph construction
graph = {
    10 : [(40,1),(20,1)],
    40 : [(10,1),(35,1)],
    35 : [(40,1),(50,2),(25,5),(20,0)],
    50 : [(35,2)],
    25 : [(35,1)],
    20 : [(10,1),(35,1),(60,0),(80,0),(70,1)],
    60 : [(20,0),(90,1),(80,0),(70,1)],
    90 : [(60,2)],
    80 : [(60,0),(20,2),(70,1)],
    70 : [(60,1),(20,4),(80,9)]
}

import heapq,math

# 1. Dijkstra's algorithm
def dijkstras(graph,source):
    distance = {node : math.inf for node in graph}
    distance[source] = 0

    # priority queue
    pq = [(0,source)]

    while pq:
        curr_dist,curr_node = heapq.heappop(pq)  # pop first -> which has less distance in pq
        if curr_dist > distance[curr_node]:
            continue

        for neighbour,weight in graph[curr_node]:
            new_distance = distance[curr_node] + weight
            if new_distance < distance[neighbour]:     # if new distance is less than the old one , then update it
                distance[neighbour] = new_distance
                heapq.heappush(pq,(new_distance,neighbour))

    return distance

# calling that function
print(dijkstras(graph,10))