def check_sorted(arr):

    for i in range(len(arr)-1):
        if arr[i]> arr[i+1]:
            return False
    return True

arr = [1, 2, 4, 7, 3]
print(check_sorted(arr))