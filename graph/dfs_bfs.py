from collections import deque

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

# dfs
def depth_first_search(node,visited = set(),result = []):

    visited.add(node)
    result.append(node)

    for neighbour in graph[node]:
        if neighbour not in visited:
            depth_first_search(neighbour)
    
    return result


# bfs
def breadth_first_search(node,result = []):
    visited = set()
    visited.add(node)
    
    queue = deque()
    queue.append(node)

    while queue:
        curr = queue.popleft()
        result.append(curr)

        for neighbour in graph[curr]:
            if neighbour not in visited:
                visited.add(neighbour)
                queue.append(neighbour)

    return result

node = 10
# calling the dfs function
print(f"{depth_first_search(node)} --> dfs output")

# calling the bfs function
print(f"{breadth_first_search(node)} --> bfs output")