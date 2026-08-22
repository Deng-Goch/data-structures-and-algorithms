from timeit import timeit

class Sorting:
    ## O(n2)
    def bubbleSort(self, array):
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

    def mergeSort(self, array):
        pass

    ## O(n2)
    def selectionSort(self, array):

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

    def insertionSort(self, array):

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


if __name__ == "__main__":
    x = Sorting()
    y = [0, 0, 1, 2, 2, 3, 4, 4, 5, 6, 6, 7, 8, 9]
    z = [6,2,0,1,6,8]
    # print(x.selectionSort(z))
    print(x.insertionSort(z))