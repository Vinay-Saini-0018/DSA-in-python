def selection_sort(arr):
    n = len(arr)

    for i in  range(n):
        min_index = i   # assuming the first index of unsorted part as min_element index

        for j in range(i+1,n):
            if arr[j] < arr[min_index]:
                min_index = j             # if value less than that comes then updating the index of min_element

        arr[i],arr[min_index] = arr[min_index],arr[i]    # swapping the elements

    return arr

arr = [5,3,7,8,2,1]
print(selection_sort(arr))