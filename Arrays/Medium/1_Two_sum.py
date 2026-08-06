def two_sum(arr, k):

    seen = {}

    for i in range (len(arr)):
        if k - arr[i] in seen:
            return [seen[k - arr[i]], i]
        else:
            seen[arr[i]] = i
    return 

arr = [0, 6, 2, 10, 1]

print(two_sum(arr, 8))









#brute force
'''def two_sum(arr, k):

    for i in range(len(arr)):
        for j in range(i+1, len(arr)):

            if arr[i] + arr[j] == k and i != j:
                return [i, j]   

arr = [0, 6, 2, 10, 1]

print(two_sum(arr, 8))'''