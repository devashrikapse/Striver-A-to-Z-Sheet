def subarray_count(nums, k):

    prifix_sum = 0
    count = 0

    prifix_map = {0: 1}

    for i in range (len(nums)):

        prifix_sum += nums[i]

        if (prifix_sum - k) in prifix_map:
            count += prifix_map[prifix_sum-k]
        
        prifix_map[prifix_sum] = prifix_map.get(prifix_sum, 0) + 1

    return count

nums = [1, 2, 3]
k = 3
print(subarray_count(nums, k))