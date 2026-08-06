def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        swappeed = False

        for j in range(n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True
        if not swapped:
            break    
    return arr

if __name__ == "__main__":
    arr = [13, 46, 12, 90, 6]
    print("before soRting", arr)

    sorted_arr = bubble_sort(arr)
    print("after sorting", sorted_arr)
