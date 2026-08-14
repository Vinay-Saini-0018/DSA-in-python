def bubble_sort(arr):
    n = len(arr)

    # i represting the pass number
    for i in range(n):
        swapped = False

        # swapping elements only in the unsorted part
        for j in range(0,n-1-i):
            if arr[j] > arr[j+1]:
                arr[j],arr[j+1] = arr[j+1],arr[j]
                swapped = True

        # if no swapping happens means data is sorted
        if not swapped:
            break

    return arr

arr = [5,3,7,8,2,1]
print(bubble_sort(arr))