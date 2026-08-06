def remove_duplicates(arr):

    seen = []

    for num in arr:
        if num in seen:
            i =+ 1
        else:
            seen.append(num)

    return seen

arr = [2, 5, 7, 5, 1, 2, 7]
print(remove_duplicates(arr))