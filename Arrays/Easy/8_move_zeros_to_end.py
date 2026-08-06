def move_zeros_to_end(arr):

    left = 0
    right = 0

    for i in range(len(arr)):
        left = i

        if arr[left] != 0:
            arr[left], arr[right] = arr[right], arr[left]
            right += 1

    return arr
            

arr = [0, 3, 4, 0, 1]
print(move_zeros_to_end(arr))




