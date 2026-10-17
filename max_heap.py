from dynamicarray import DynArray

class Array_Based_Max_Heap:
    ## 3 magic methods
    ## O(1)
    def __init__(self, *args):

        """
        Input: takes a collection of arguments.

        Process: inserts the arguments into the heap one after the other.

        Output: 

        Error:
        """

        self.heap = DynArray()
        for arg in args:
            self.insert(arg)


    ## O(1)
    def __len__(self):
        return len(self.heap)


    ## O(n)
    def __str__(self):
        return str(self.heap)


    ## 5 inner / helper methods
    ## (log2 n) - used with parent for inserting
    ## O(1)
    def _parent_(self, index):
        return ((index - 1) // 2)


    ## O(1)
    def _left_(self, index):
        return ((index * 2) + 1)


    ## O(1)
    def _right_(self, index):
        return ((index * 2) + 2)


    ## O(log2 n) - used for inserting
    def _sift_up_(self, index):
        parent = self._parent_(index)

        if parent >= 0:

            left = self._left_(parent)
            right = self._right_(parent)

            if left < (len(self.heap)) and right < (len(self.heap)):

                if self.heap[left] > self.heap[parent]:
                    self.heap[left], self.heap[parent] = self.heap[parent], self.heap[left]
                    self._sift_up_(parent)
                elif self.heap[right] > self.heap[parent]:
                    self.heap[right], self.heap[parent] = self.heap[parent], self.heap[right]
                    self._sift_up_(parent)
                else:
                    return

            elif left < (len(self.heap)):

                if self.heap[left] > self.heap[parent]:
                    self.heap[left], self.heap[parent] = self.heap[parent], self.heap[left]
                    self._sift_up_(parent)
            else:
                return
        else:
            return

    
    ## O(log2 n) - used with left and right for deleting
    def _sift_down_(self, index):
        left = self._left_(index)
        right = self._right_(index)
        
        if left < (len(self.heap)) and right < (len(self.heap)):

            if self.heap[left] > self.heap[right] and self.heap[left] > self.heap[index]:
                self.heap[left], self.heap[index] = self.heap[index], self.heap[left]
                self._sift_down_(left)

            elif self.heap[right] > self.heap[left] and self.heap[right] > self.heap[index]:
                self.heap[right], self.heap[index] = self.heap[index], self.heap[right]
                self._sift_down_(right)

        elif left < (len(self.heap)):
            if self.heap[left] > self.heap[index]:
                self.heap[left], self.heap[index] = self.heap[index], self.heap[left]
        else:
            return


    ## 5 methods
    ## O(log2 n)
    def insert(self, value):

        """
        Input: 

        Process: 

        Output: 

        Error: 
        """

        self.heap.append(value)
        self._sift_up_(len(self.heap)-1)


    ## O(1)
    def peek(self):

        """
        Input: 

        Process: checks the first element/node on the tree without removing it.

        Output: returns the checked element/node.

        Error: 
        """

        if len(self.heap) == 0:
            raise IndexError('Peeking from an empty Heap.')
        else:
            return self.heap[0]


    ## O(log2 n)
    def pop(self):

        """
        Input: 

        Process: removes the first element/node in the tree.

        Output: the removed element/node.

        Error: 
        """

        if len(self.heap) == 0:
            raise IndexError('Poping from an empty Heap.')
        elif len(self.heap) == 1:
            self.heap.pop()
        else:
            poped = self.heap[0]

            self.heap[0], self.heap[len(self.heap)-1] = self.heap[len(self.heap)-1], self.heap[0]
            self.heap.pop()

            self._sift_down_(0)

            return poped


    ## O(n)
    def meld(self, Iterable) -> None:

        """
        Input: takes an iterable or a collection of arguments.

        Process: inserts the arguments into the heap one after the other.

        Output: returns a new heap with the new arguments inserted to their right position on the heap.

        Error: throws a "TypeError: '>' not supported between instances of 'x' and 'y'" if the value in the heap and the values in the iterable are of different data types. OR "TypeError: Array_Based_Max_Heap.meld() missing 1 required positional argument: 'Iterable'" if no iterable object entered.
        """

        for arg in Iterable:
            self.insert(arg)


    def max_heapify(self, array:DynArray) -> DynArray:

        """
        Input: 

        Process: 

        Output: 

        Error: 
        """

        pass


if __name__ == "__main__":
    maxheap = Array_Based_Max_Heap()

    maxheap.insert(70)
    maxheap.insert(81)
    maxheap.insert(37)
    maxheap.insert(17)
    maxheap.insert(14)
    maxheap.insert(19)
    maxheap.insert(27)
    maxheap.insert(45)
    maxheap.insert(75)

    print(maxheap)
    print()

    # maxheap.pop()
    # print(maxheap.peek())

    # maxheap.pop()
    # print(maxheap)

    # maxheap.pop()
    # print(maxheap)

    # maxheap.pop()
    # print(maxheap)

    # maxheap.pop()
    # print(maxheap)

    # maxheap.pop()
    # print(maxheap)

    # maxheap.pop()
    # print(maxheap)

    # maxheap.pop()
    # print(maxheap)

    # maxheap.pop()
    # print(maxheap)


    # maxheap.pop()
    # print(maxheap)