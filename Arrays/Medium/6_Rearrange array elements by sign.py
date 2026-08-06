def sort_by_sign(arr):

    positive = 0
    negative = 1
    ans =[0]*len(arr)

    for num in arr:
        if num > 0:
            ans[positive] = num
            positive += 2
        else:
            ans[negative] = num
            negative += 2


    return ans


arr = [2, 4, 5, -1, -3, -4]
print(sort_by_sign(arr))
            


