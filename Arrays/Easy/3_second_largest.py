def second_largest(arr):

    largest = float("-inf")
    second = float("-inf")

    for num in arr:

        if num > largest:
            second = largest
            largest = num

        elif num > second and num != largest:
            second = num

    if second == float("-inf"):
        return -1

    return second


arr = [8, 8, 7, 6, 5]
print(second_largest(arr))