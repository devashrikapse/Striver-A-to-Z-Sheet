def count_frequencies(arr):

    freq={}

    for num in arr:
        if num in freq:
            freq[num] += 1
        else:
            freq[num] = 1

    result = []

    for key, value in freq.items():
        result.append([key, value])

    return result

print(count_frequencies(arr = [1, 2, 2, 3, 3, 3, 4, 4]))