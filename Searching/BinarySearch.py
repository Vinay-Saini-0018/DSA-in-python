def BinarySearch(arr,target):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = low + (high-low) //2

        if arr[mid] == target:
            return mid

        if arr[mid] < target:
            low = mid + 1

        else : 
            high = mid - 1

    return -1

arr = [1,2,3,4,5,6,7,12,14,15,18,24,29,35,46,76,78]
print(f"At index : {BinarySearch(arr,24)}")