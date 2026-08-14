def merge(left,right):
    result =[]

    i = j = 0

    # appending the values from both in result in sorting order
    while ((i<len(left)) and (j<len(right))):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    # while use while loop if one list used and one list remains then add that in result
    result.extend(left[i:])
    result.extend(right[j:])

    return result

def merge_sort(arr):
    if len(arr) == 1:
        return arr
    mid = len(arr)//2
    # dividing the arr in sub parts
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    return merge(left,right)   # calling that above function

arr = [5,3,7,8,2,1]
print(merge_sort(arr))        