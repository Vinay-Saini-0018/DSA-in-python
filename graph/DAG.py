from collections import defaultdict
import math

graph = defaultdict(list)

graph[6] = [1,5]
graph[0] = [1,2]
graph[1] = [2,5]
graph[2] = [3]
graph[5] = [3,4]
graph[3] = []
graph[4] = []

weights = {
    (6,1) : 2,
    (6,5) : 4,
    (0,1) : 1,
    (0,2) : 5,
    (1,2) : 1,
    (1,5) : 3,
    (2,3) : 2,
    (5,3) : -2,
    (5,4) : 1
}

# source node
src = 6

for u in graph:
    print(u,"-->",graph[u])

class DAG:
    def topo_dfs(graph):
        visited = set()
        topo = []
        def dfs(u):
            visited.add(u)
            for v in graph[u]:
                if v not in visited:
                    dfs(v)
            topo.append(u)

        for node in graph:
            if node not in visited:
                dfs(node)

        return topo[: : -1]

    # DAG shoretes path algorithm
    def shortest_path(graph,weights,src):
        topo_order = DAG.topo_dfs(graph)
        distance = {node : math.inf for node in graph}
        distance[src] = 0

        for u in topo_order:
            if distance[u] != math.inf:
                for v in graph[u]:
                    if distance[v] > distance[u] + weights[(u,v)]:
                        distance[v] = distance[u] + weights[(u,v)]

        return distance

    # DAG longest path algorithm
    def longest_path(graph):
        topo = DAG.topo_dfs(graph)
        res = {node : 0 for node in graph}

        for u in topo:
            for v in graph[u]:
                res[v] = max(res[v],res[u]+weights[(u,v)])

        return res



# calling shortest_path function
print(DAG.shortest_path(graph,weights,src))
print(DAG.longest_path(graph))