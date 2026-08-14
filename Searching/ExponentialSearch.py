def binary_search(arr,target,low,high):
    while low <=high:
        mid = low + (high-low) // 2

        if arr[mid] == target:
            return mid

        if arr[mid] < target:
            low = mid + 1
        else :
            high = mid -1

    return -1

def ExponentialSearch(arr,target):
    if arr[0]  == target:
        return 0

    i = 1
    n = len(arr)
    # AT the end this will return the upper boundary of range
    while (i<n) and (arr[i] <= target):
        i *= 2

    low = i//2   # lower boundary of range
    high = min(i,n-1)    # if arr size is less but the upper-boundary is larger. than we take the arr's last index as upper-boundary
    print(f"Target : {target}")
    print(f"Range : {low} to {high}")

    return binary_search(arr,target,low,high)

arr = [1,2,3,4,5,6,7,12,14,15,18,24,29,35,46,76,78]
print(f"At index : {ExponentialSearch(arr,24)}")