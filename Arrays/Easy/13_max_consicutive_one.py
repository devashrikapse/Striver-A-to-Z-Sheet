def max_consicutive_one(arr):

    maximum = 0
    count = 0

    for numm in arr:
        if numm == 1:
            count += 1
        else:
            count = 0

        maximum= max(maximum, count)
            
    return maximum

arr = [1, 1, 1, 1, 0, 0, 1, 0, 1, 1, 0, 1, 0, 1, 1, 1, 1, 1]
print(max_consicutive_one(arr))


            
