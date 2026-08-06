class InsertionSort:
    def insertion_sort(self, arr):
        n = len(arr)
        for i in range(1, n):
            key = arr[i]
            j = i-1

            while j >= 0 and arr[j] > key:
                arr[j+1] = arr[j]
                j -= 1

            arr[j+1] = key

        return arr

__name__ == "__main__"

arr = [20, 2, 25, 15, 1, 6, 18]
print("befor sorting:",arr)

sorter = InsertionSort()
sorted_arr = sorter.insertion_sort(arr)

print("after sorting", sorted_arr)
            
            


