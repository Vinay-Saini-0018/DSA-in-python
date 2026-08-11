inf = float('inf')

# number of nodes
n = 4

# matrix creation of n*n
matrix = [[inf] * n for _ in range(n)]

# distance from self to self == 0
for i in range(n):
    matrix[i][i] = 0

edges = [
    (1,2,4),
    (2,1,10), 
    (2,3,3),
    (3,4,2),
    (4,1,1),
    (1,4,9),
    (3,1,5)
]

# fill the weights of edges
for u,v,w in edges:
    matrix[u-1][v-1] = w

# print the matrix
for row in matrix:
    print(row)

# floyd function
def floyd_warshall(matrix):
    n = len(matrix)

    # k = middle node , i = starting node, j = destination node
    for k in range(n):
        for i in range(n):
            for j in range(n):

                # if going through node < than going direct than update the distances
                if matrix[i][k] + matrix[k][j] < matrix[i][j]:
                    matrix[i][j] = matrix[i][k] + matrix[k][j]

    return matrix

# calling the floyd function
print(floyd_warshall(matrix))
