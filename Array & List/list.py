# operations in list

num = [1,2,3,4,5,6,7,8]
num2 = [16,17,18]

# append
num.append(9)
print(f"Appended 9 in the list : {num}")

# insert
num.insert(0,10)
print(f"inserting 10 in the starting : {num}")

# merging
num.extend(num2)
print(f"merging num and num2 : {num}")

# sorting
num.sort()
print(f"sorted list : {num}")

# copy of num2
cp = num2.copy()
print(f"copy of num2 : {cp}")