def max_sum(arr):
    current_sum = 0
    max_sum = arr[0]
    start = 0 
    end = 0
    temp_start = 0


    for i in arr:
        current_sum += i
        if current_sum > max_sum:
            max_sum = current_sum
            start = temp_start
            end = i        

        if current_sum < 0:
            current_sum = 0
            temp_start = i + 1

    return arr[start:end+1], max_sum

arr =  [2, 3, 5, -2, 7, -4]

print(max_sum(arr))
