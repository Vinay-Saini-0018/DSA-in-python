# implementing array using numpy module

import numpy as np

arr = np.array([1,2,3,4,5,6,7,8])
arr2 = np.array([9,10,11,12])

# accessing
print(f"element in arr at index 5 : {arr[5]}")

# Traversal
print("Traversal")
for ele in arr:
    print(ele,end = ' ')
print('\n')

# insertion
inserted = np.insert(arr,0,15)
print(f"15 is inserted at index 0 in arr : {inserted}")

# updation
arr[0] = 13
print(f"updating 1 with 13 : {arr}")

# deletion
deletion = np.delete(arr,0)
print(f"Removed 13 from arr : {deletion}")

# sorting
sorted = np.sort(arr)
print(f"sorted arr : {sorted}")

# merging arr and arr2
new_arr = np.concatenate((arr,arr2))
print(f"merged array : {new_arr}")

# splitting arr
splt_arr = np.array_split(arr,3)
print(f"splitted array : {splt_arr}")
