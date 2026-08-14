# working on martix (2d list)

# creation 
matrix = [[2,3,4],[5,6,7],[8,9,0]]

# updation
matrix[2][2] = 1
print(f"updating 0 with 1 in 3rd row : {matrix}")

# insertion
matrix[1].insert(1,0)
print(f"inserting 0 in 2nd row : {matrix}")

# inserting at the end
matrix[0].append(11)
print(f"appending 11 in 1st row : {matrix}")

# removing
matrix[2].remove(8)
print(f"Removing 8 from 3rd row : {matrix}")



