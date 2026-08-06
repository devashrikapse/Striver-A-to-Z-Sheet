def longest_seq(arr):
    map = set(arr)
    max_len = 0

    for i in range(len(arr)):

        if arr[i] - 1 not in map:
            current = arr[i]
            length = 1

            while current + 1 in map:
                current += 1
                length += 1
            max_len = max(max_len, length)
    return max_len


arr = [100, 4, 200, 1, 3, 2]
print(longest_seq(arr))