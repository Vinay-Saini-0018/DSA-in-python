def insertion_sort(arr):
    n = len(arr)
    for i in range(1,n):
        key = arr[i]
        j = i-1   # last element of the sorted part

        while (j>=0) and (arr[j]>key):    # finding the correct position of key
            arr[j+1] = arr[j]
            j-=1
        arr[j+1] = key     # now placing the key on its correct position

    return arr

arr = [5,3,7,8,2,1]
print(insertion_sort(arr))