def rotate_by_one(arr):

    n = len(arr)
    
    for i in range(n-1):
        temp = arr[i]
        arr[i] = arr[i+1]
        arr[i+1] = temp

    return arr

arr = [5, 1, 2, 3, 4]
print(rotate_by_one(arr))


