def majority_element(arr):

    num = None
    count = 0

    for i in arr:
        if count == 0:
            num = i
            count = 1
        elif num == i:
            count += 1
        else:
            count -= 1

    return num

arr = [1, 1, 1, 2, 1, 2]
print(majority_element(arr))