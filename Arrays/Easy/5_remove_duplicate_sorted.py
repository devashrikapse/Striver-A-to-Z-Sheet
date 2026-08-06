def in_place_remove_duplicate(arr):

    i = 0

    for j in range(1, len(arr)):
        if arr[j] != arr[i]:
            i += 1
            arr[i] = arr[j]

    return i+1

arr = [1, 1, 2, 2, 2, 4, 4]
k = in_place_remove_duplicate(arr)

print(k)
print(arr[:k])

#only for sorted
