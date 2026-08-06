class SelectionSort:
    def selection_sort(self, arr):
        n = len(arr)

        for i in range(n):
            min = 1
            for j in range(i+1, n):
                if arr[j] < arr[min]:
                    min = j

            arr[i], arr[min] = arr[min], arr[i]
           
        return arr


__name__ = "__main__"

arr = [4, 9, 2, 5, 9, 1]
print("befor sorting:", arr)

sorter = SelectionSort()
sorted_arr = sorter.selection_sort(arr)
print("after sorting:", sorted_arr)


            

    