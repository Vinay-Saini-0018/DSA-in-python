start_state = (1,2,3,4,0,5,6,7,8)
goal_state = (1,2,3,4,5,6,7,8,0)

from collections import deque

def get_neighbours(state):
    neighbours = []
    idx = state.index(0)

    swaps = {
        0 : [1,3],
        1 : [0,2,4],
        2 : [1,5],
        3 : [0,4,6],
        4 : [1,3,5,7],
        5 : [2,4,8],
        6 : [3,7],
        7 : [4,6,8],
        8 : [5,7]
    }

    for swap in swaps[idx]:
        new_state = list(state)
        new_state[idx],new_state[swap] = new_state[swap], new_state[idx]

        neighbours.append(tuple(new_state))

    return neighbours

def solve_puzzle(start,goal):
    queue = deque([start])
    visited = set([start])

    while queue:
        state = queue.popleft()

        if state == goal:
            return True

        for next_state in get_neighbours(state):
            if next_state not in visited:
                visited.add(next_state)
                queue.append(next_state)

    return False