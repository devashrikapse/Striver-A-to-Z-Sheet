def reverse( arr, left, right):
    while left < right:
        arr[left], arr[right] = arr[right], arr[left]
        left += 1
        right -= 1

    return arr

def rotate_by_k(arr, k):

    n = len(arr)
    k = k % n

    reverse(arr, 0, k-1)
    reverse(arr, k, n-1)
    reverse(arr, 0, n-1)

    return arr

arr = [1, 2, 3, 4, 5, 6]
print(rotate_by_k(arr, 2))


