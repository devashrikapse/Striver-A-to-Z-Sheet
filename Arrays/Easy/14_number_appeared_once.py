def number_appeared_once(arr):

    Xor = 0

    for i in arr:
        Xor ^= i

    return Xor

arr = [2, 2, 3, 1, 4, 5, 6, 5, 6, 3, 4]
print(number_appeared_once(arr))