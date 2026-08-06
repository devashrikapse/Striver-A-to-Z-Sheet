def largest_element(arr):

    largest = arr[0]
    for num in arr:
        if num > largest:
            largest = num

    return largest

arr = [4, 7, 1, 3, 9, 5, 6]
print(largest_element(arr))