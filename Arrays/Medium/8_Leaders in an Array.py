def learder_array(arr):
    ans = []
    max_num = arr[-1]
    ans.append(max_num)

    for i in range (len(arr)-1, 0, -1):

        if arr[i] > max_num:
            ans.append(arr[i])
            max_num = arr[i]
    ans.reverse()

    return ans

arr =  [1, 2, 5, 3, 1, 2]
print(learder_array(arr))

#brute force
'''def learder_array(arr):
    ans = []
    n = len(arr)

    for left in range(n-1):
        right = left + 1

        while right <= n and arr[left] > arr[right]:
                right += 1
                if right == n:
                     ans.append(arr[left])
                     break
    ans.append(arr[n-1])
    return ans
arr =  [-3, 4, 5, 1, -30, -10]
print(learder_array(arr))'''
        