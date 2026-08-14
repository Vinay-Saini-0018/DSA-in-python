def LinearSearch(arr,target):
    for i , element in enumerate(arr):
        if element == target:
            return i

    return -1

# calling the function
arr = [3,4,5,7,2,87,34,23,54]
print(f"checking 87 : {LinearSearch(arr,87)}")
print(f"checking 99 : {LinearSearch(arr,99)}")