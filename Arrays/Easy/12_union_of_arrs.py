def union_of_arr(arr1, arr2):

    i = 0
    j = 0
    ans = []

    while i < len(arr1) and j < len(arr2):
        if arr1[i] < arr2[j]:
            if not ans or ans[-1] != arr1[i]:
                ans.append(arr1[i])
            i +=1
        elif arr1[i] > arr2[j]:
            if not ans or ans[-1] != arr1[i]:
                ans.append(arr2[j])
            j += 1
        else:
            if not ans or ans[-1] != arr1[i]:
                ans.append(arr1[i])
            i += 1
            j += 1

    while i < len(arr1):
        if not ans or ans[-1] != arr1[i]:
            ans.append(arr1[i])
        i += 1

    while j < len(arr2):
        if not ans or ans[-1] != arr2[j]:
            ans.append(arr2[j])
        j += 1

    return ans

arr1 = [1, 2, 3, 5, 6, 8]
arr2 = [4, 7]
print(union_of_arr(arr1, arr2))



