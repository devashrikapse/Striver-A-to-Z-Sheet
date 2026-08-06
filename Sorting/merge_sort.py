class MergeSort:
    def merge_sort(self, arr):
        if len(arr) <= 1:
            return arr
        
        mid = len(arr) // 2

        left = self.merge_sort(arr[:mid])
        right = self.merge_sort(arr[mid:])

        return self.merge(left, right)

    def merge(self, left, right):
        result=[]
        i = j = 0

        while i < len(left) and j < len(right):

            if left[i] < right[j]:
                result.append(left[i])
                i += 1
            
            else:
                result.append(right[j])
                j += 1

        result.extend(left[i:])
        result.extend(right[j:])

        return result

if __name__ == "__main__":

    arr = [20, 2, 25, 15, 1, 6, 18]
    print("befor sorting:",arr)

    sorter = MergeSort()
    sorted_arr = sorter.merge_sort(arr)

    print("after sorting", sorted_arr)
            


        