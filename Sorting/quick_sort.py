class QuickSort:
    def quick_sort(self, arr):

        if len(arr) <= 1:
            return arr

        pivot = arr[len(arr) // 2]

        left = [x for x in arr if x < pivot]
        middle = [x for x in arr if x == pivot] 
        right = [x for x in arr if x > pivot]
      
        return self.quick_sort(left) + middle + self.quick_sort(right)

if __name__ == "__main__":

    arr = [10, 4, 7, 1, 3, 8]
    print("befor sorting:", arr)

    sorter = QuickSort()
    sorted_arr = sorter.quick_sort(arr)
    print("after sorting:", sorted_arr)
