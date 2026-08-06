def reverse_array(arr, l, r):

    if  l >= r:
        return

    arr[l], arr[r] = arr[r], arr[l]

    return reverse_array(arr, l+1, r-1)

arr = [2, 3, 4, 5, 6]
reverse_array(arr, 0, len(arr)-1)
print(arr)
    