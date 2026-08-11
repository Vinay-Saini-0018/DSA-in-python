maze = [
    [1,0,0,1],
    [1,1,0,1],
    [0,1,1,1],
    [0,0,1,1]
]

from collections import deque

def rat_maze(maze):
    m,n = len(maze),len(maze[0])

    if maze[0][0] == 0:
        return False

    queue = deque([(0,0)])
    visited = set([(0,0)])
    directions = [(-1,0),(1,0),(0,-1),(0,1)]

    while queue:
        x,y = queue.popleft()

        # if we reached at final
        if (x,y) == (m-1,n-1):
            return True

        for dx,dy in directions:
            nx,ny = (x+dx,y+dy)

            if (0<=nx<m) and (0<=ny<n):
                if (maze[nx][ny] == 1) and (nx,ny) not in visited:
                    visited.add((nx,ny))
                    queue.append((nx,ny))

    return True

# calling this function
bool = rat_maze(maze)

if bool == True:
    print("There is path")
else:
    print("There is no path")