def missing_number(arr):

    n = len(arr)

    expected = n * (n+1) // 2
    actual = sum(arr)

    return expected - actual

arr = [0, 1, 3, 5, 4, 7, 6]
print(missing_number(arr))







#brute force
'''def missing_number(arr):

    for i in range(len(arr)+1):
        if i in arr:
            continue
        else:
            return i
    return len(arr)+1

arr = [0, 1, 3, 5, 4, 7, 6]
print(missing_number(arr))'''
