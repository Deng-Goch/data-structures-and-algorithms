from dynamicarray import DynArray

class Sorting_Algos:
    ## O(n2)
    def bubbleSort(self, array) -> list:

        """
        Input: 

        Process: 

        Output: 

        Error: 
        """

        swap = True
        end = (len(array)-1)
        while swap:
            swap = False
            for i in range(iters):
                if array[i] < array[i+1]:
                    array[i], array[i+1] = array[i+1], array[i]
                    swap = True

            iters -= 1
        return array


    ## O(log2 n)
    def mergeSort(self, array):

        """
        Input: 

        Process: 

        Output: 

        Error: 
        """



    ## O(n2)
    def selectionSort(self, array):

        """
        Input: 

        Process: 

        Output: 

        Error: 
        """

        start = 0
        swap = True

        for i in range(start, len(array)-1):
            if swap:
                swap = False
                for j in range(start, len(array)-1):
                    if array[i] < array[j]:
                        array[i], array[j] = array[j], array[i]
                        swap = True
            else:
                return array

        return array


    ## O(x)
    def insertionSort(self, array):

        """
        Input: 

        Process: 

        Output: 

        Error: 
        """

        swap = True
        
        for i in range(len(array)-1):
            if swap:
                swap = False
                for j in range(i+1, 0, -1):
                    if array[j] < array[i]:
                        array[j], array[i] = array[i], array[j]
                        swap = True
            else:
                return array

        return array


    ## O(x)
    def quickSort(self):

        """
        Input: 

        Process: 

        Output: 

        Error: 
        """



    ## O(x)
    def heapSort(self, array):

        """
        Input: 

        Process: 

        Output: 

        Error: 
        """

        ### Part 1: Maxheap sort it.
        def _parent_(index:int) -> int:
            return ((index - 1) // 2)

        def _heapify_(array):
            swap = True

            while swap:
                swap = False
                for i in range((len(array)-1), 0, -1):
                    parent = _parent_(i)

                    if array[i] > array[parent]:
                        array[i], array[parent] = array[parent], array[i]
                        swap = True
                    else:
                        continue
            return array


        ### Part 2: Delete without poping the last element.
        def _left_(index:int) -> int:
            return ((index * 2) + 1)

        def _right_(index:int) -> int:
            return ((index * 2) + 2)

        def _sift_down_(index:int) -> None:
            left = _left_(index)
            right = _right_(index)

            if left < len(array) and right < len(array):
                if array[index] < array[left] and array[index] < array[right]:
                    array[index], array[left] = array[left], array[index]
                elif array[index] < array[right] and array[right] < array[index]:
                    array[index], array[right] = array[right], array[index]
                else:
                    return
                _sift_down_(left)

            elif left < len(array):
                if array[index] < array[left]:
                    array[index], array[left] = array[left], array[index]
                _sift_down_(right)
            else:
                return


        heaped = _heapify_(array)
        
        return heaped

    ## O(x)
    def topologicalSort(self):

        """
        Input: 

        Process: 

        Output: 

        Error: 
        """


    ## O(x)
    def bucketSort(self):

        """
        Input: 

        Process: 

        Output: 

        Error: 
        """



    ## O(x)
    def radixSort(self):

        """
        Input: 

        Process: 

        Output: 

        Error: 
        """



    ## O(x)
    def countingSort(self):

        """
        Input: 

        Process: 

        Output: 

        Error: 
        """




if __name__ == "__main__":
    x = Sorting_Algos()
    y = DynArray(3,7,0,12,4,6,2,3,9,39,20,1,3,38)
    # print(x.selectionSort(z))
    print(x.heapSort(y))