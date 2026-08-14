# Implementing through Array Module

import array

# array creation
arr = array.array('i',[1,2,3,4,5,6,7])
arr2 = array.array('i',[9,10,11])

# accessing
print(f"accessing 2nd index value : {arr[2]}")

# traversal
print("Traversal : ")
for ele in arr:
    print(ele, end=' ')
print('\n')

# insertion
arr.insert(2,8)
print(f"8 is inserted at 2nd index : {arr}")

# deletion
arr.remove(8)
print("8 is deleted from arr : ", arr)

# updation
arr[0] = 0
print("0th index is updated by 0 : ", arr)

# sorting
array.array('i',sorted(arr))
print(f"sorted array : {arr}")

# mering arr and arr2
new_arr = arr + arr2
print(f"merged array : {new_arr}")

# splitting arr
half_len = len(arr)//2
a1 = arr[ : half_len]
a2 = arr[half_len : ]
print(f"splitted arr : {a1} and {a2}")