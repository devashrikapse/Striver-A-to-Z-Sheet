def highest_occuring(arr):

    freq={}

    for num in arr:
        if num in freq:
            freq[num] += 1
        else:
            freq[num] = 1

    max = 0

    for key, value in freq.items():
        if value > max:
            max = key

    return freq[max]

print(highest_occuring(arr = [1, 2, 2, 3, 3, 3, 4, 4]))