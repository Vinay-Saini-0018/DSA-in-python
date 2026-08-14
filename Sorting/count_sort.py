def count_sort(arr):
    max_value = max(arr)
    count_arr = [0] * (max_value + 1)   # extra 1 --> for 0th index

    for ele in arr:
        count_arr[ele] += 1

    result = []
    for i in range(len(count_arr)):
        result.extend([i] * count_arr[i])

    return result,count_arr

arr = [2,3,4,3,2,3,4,5,15]
result , count_arr = count_sort(arr)
print(f'sorted array : {result}')
print(f"count_arr : {count_arr}")