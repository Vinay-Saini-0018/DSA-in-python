def quick_sort(arr):
    if len(arr) <= 1:
        return arr

    # taking middle element as middle
    pivot = arr[len(arr)//2]

    # defining that left side has elements less than pivot
    # And right side has elements greater than pivot
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]

    # Now calling the same function for left and right subtree
    return quick_sort(left) + middle + quick_sort(right)

arr = [5,3,7,8,2,1]
print(quick_sort(arr))
