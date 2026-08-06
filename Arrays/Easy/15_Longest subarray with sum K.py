def longestSubarray(nums, k):

    prifix_sum = 0
    max_length = 0

    prifix_map = {0: -1}

    for i in range (len(nums)):

        prifix_sum += nums[i]

        if (prifix_sum - k) in prifix_map:
            lenght = i - prifix_map[prifix_sum - k]

            if lenght > max_length:
                max_length = max(lenght, max_length)
                start = prifix_map[prifix_sum - k] + 1
                end = i


        if prifix_sum not in prifix_map:
            prifix_map[prifix_sum] = i

    return nums[start: end+1], max_length

nums = [10, 5, 2, 7, 1, 9]
k = 15

print(longestSubarray(nums, k))