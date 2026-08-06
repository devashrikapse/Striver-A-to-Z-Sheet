def index_of_target(arr, target):

    for i in range(len(arr)):
        if arr[i] == target:
            return i

    return -1

arr = [5, 1, 2, 1, 4, 2]
print(index_of_target(arr, 2))
