from dynamicarray import DynArray

class Array_Based_Max_Heap:
    ## 3 magic methods
    ## O(1)
    def __init__(self, *args):
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

            if left <= (len(self.heap)-1) and right <= (len(self.heap)-1):

                if self.heap[left] > self.heap[parent]:
                    self.heap[left], self.heap[parent] = self.heap[parent], self.heap[left]
                    
                elif self.heap[right] > self.heap[parent]:
                    self.heap[right], self.heap[parent] = self.heap[parent], self.heap[right]
                    
                if self.heap[left] > self.heap[right]:
                    self.heap[left], self.heap[right] = self.heap[right], self.heap[left]
                self._sift_up_(parent)

            elif left <= (len(self.heap)-1):

                if self.heap[left] > self.heap[parent]:
                    self.heap[left], self.heap[parent] = self.heap[parent], self.heap[left]
                    self._sift_up_(parent)
            else:
                return
        else:
            return
    
    ## O(log2 n) - used with left and right for deleting
    def _sift_down_(self, index):
        right = self._right_(index)
        left = self._left_(index)
        
        if left <= (len(self.heap)-1) and right <= (len(self.heap)-1):
            self.heap[index], self.heap[right] = self.heap[right], self.heap[index]
            if self.heap[left] > self.heap[right]:
                self.heap[left], self.heap[right] = self.heap[right], self.heap[left]
            self._sift_down_(left)

        elif left <= (len(self.heap)-1):
            if self.heap[index] < self.heap[left]:
                self.heap[index], self.heap[left] = self.heap[left], self.heap[index]
                self._sift_down_(right)
        else:
            return

    ## 5 methods
    ## O(log2 n)
    def insert(self, value):
        self.heap.append(value)
        self._sift_up_(len(self.heap)-1)

        ## O(1)
    def peek(self):
        if len(self.heap) == 0:
            raise IndexError('Peeking from an empty Heap.')
        else:
            return self.heap[0]

    ## O(log2 n)
    def pop(self):
        if len(self.heap) == 0:
            raise IndexError('Poping from an empty Heap.')
        elif len(self.heap) == 1:
            self.heap.pop()
        else:
            poped = self.heap[0]

            self.heap[0] = self.heap[len(self.heap)-1]
            self.heap.pop()

            self._sift_down_(0)

            return poped

    ## O(log2 n)
    def meld(self, *args) -> None:
        for arg in args:
            self.insert(arg)


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

    # maxheap.meld(102, 79, 0, 15, 69)

    # print(maxheap)

    maxheap.pop()

    print(maxheap)

    # maxheap.pop()

    # print(maxheap)

    # maxheap.pop()

    # print(maxheap)

    # maxheap.insert(70)

    # print(maxheap)


    # maxheap.insert(51)

    # print(maxheap)

    # maxheap.pop()

    # print(maxheap)