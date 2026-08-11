from collections import deque, defaultdict

graph = defaultdict(list)

graph[6] = [1,5]
graph[0] = [1,2]
graph[1] = [2,5]
graph[2] = [3]
graph[5] = [3,4]
graph[3] = []
graph[4] = []

for u in graph:
    print(u,"-->",graph[u])

def kahns_algo(graph):
    indegree = defaultdict(int)
    topo = []

    for u in graph:
        for v in graph[u]:
            indegree[v] +=1

    queue = deque()

    # calculating indegree of nodes
    for node in graph:
        if indegree[node] == 0:
            queue.append(node)

    while queue:
        u = queue.popleft()
        topo.append(u)

        for v in graph[u]:
            indegree[v] -= 1
            if indegree[v] == 0:
                queue.append(v)

    # if top length not equal to graph length --> it means there is cycle in graph
    if len(topo) != len(graph):
        return "cycle detected"

    return topo

print(kahns_algo(graph))