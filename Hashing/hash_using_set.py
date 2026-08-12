# hashing operations using set

set = {'vinay','vinit',23,43,'ajmer'}
print("set : ",set)

# insrtion
set.add('Rajasthan')
print(f"added rajasthan : {set}")

# searching
print(f"vinay in set {'vinay' in set}")
print(f" 22 in set {22 in set}")

# iteration
for x in set:
    print(x,end=' ')
print('\n')

# deletion
set.remove('vinit')
print(f"removed 'vinit':{set}")
set.pop()
print(f"remvoed random element : {set}")
