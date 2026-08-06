def recursion_bubble_sort(arr, n):

    swapped = False

    for j in range(n-1):
        if arr[j] > arr[j+1]:
            arr[j], arr[j+1] = arr[j+1], arr[j]
            swapped = True
    if not swapped:
        return arr
    
    return recursion_bubble_sort(arr, n-1)

arr = [7, 6, 5, 4, 3]
print(recursion_bubble_sort(arr, len(arr)))

### below is the preffered base condition

'''def recursion_bubble_sort(arr, n):

    if n == 1:
        return arr

    swapped = False

    for j in range(n - 1):
        if arr[j] > arr[j + 1]:
            arr[j], arr[j + 1] = arr[j + 1], arr[j]
            swapped = True

    if not swapped:
        return arr

    return recursion_bubble_sort(arr, n - 1)


arr = [7, 6, 5, 4, 3]
print(recursion_bubble_sort(arr, len(arr)))'''