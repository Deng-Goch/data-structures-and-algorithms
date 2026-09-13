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

    ## O(log2 n)
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

            elif right <= (len(self.heap)-1):

                if self.heap[right] > self.heap[parent]:
                    self.heap[right], self.heap[left] = self.heap[left], self.heap[right]
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
            if self.heap[left] > self.heap[right]:
                self.heap[index] = self.heap[left]
                self._sift_down_(left)
            else:
                self.heap[index] = self.heap[right]
                self._sift_down_(right)
        elif left <= (len(self.heap)-1):
            self.heap[index] = self.heap[left]
            self._sift_down_(left)
        elif right <= (len(self.heap)-1):
            self.heap[index] = self.heap[right]
            self._sift_down_(right)
        else:
            self.heap.pop()

    ## O(n2)
    def _heapify_(self):
        reversed = True
        while reversed:
            reversed = False
            for i in range(len(self.heap)-1):
                left = self._left_(i)
                right = self._right_(i)

                if left <= (len(self.heap)-1) and right <= (len(self.heap)-1):
                    if self.heap[left] > self.heap[i]:
                        self.heap[left], self.heap[i] = self.heap[i], self.heap[left]
                        reversed = True
                    elif self.heap[right] > self.heap[i]:
                        self.heap[right], self.heap[i] = self.heap[i], self.heap[right]
                        reversed = True
                elif left <= (len(self.heap)-1):
                    if self.heap[left] > self.heap[i]:
                        self.heap[left], self.heap[i] = self.heap[i], self.heap[left]
                        reversed = True
                elif right <= (len(self.heap)-1):
                    if self.heap[right] > self.heap[i]:
                        self.heap[right], self.heap[i] = self.heap[i], self.heap[right]
                        reversed = True

    ## 5 methods
    ## O(log2 n)
    def insert(self, value):
        self.heap.append(value)
        self._sift_up_(len(self.heap)-1)

    ## O(log2 n)
    def pop(self):
        if len(self.heap) == 0:
            raise IndexError('Poping from an empty Heap.')
        elif len(self.heap) == 1:
            self.heap.pop()
        else:
            poped = self.heap[0]

            self._sift_down_(0)

            return poped

    ## O(1)
    def peek(self):
        if len(self.heap) == 0:
            raise IndexError('Peeking from an empty Heap.')
        else:
            return self.heap[0]

    ## O(log2 n)
    def meld(self, *other_heap) -> None:
        self.heap.extend(other_heap)
        self._heapify_()


if __name__ == "__main__":
    maxheap = Array_Based_Max_Heap()

    # maxheap.meld(27, 19, 17, 14, 20, 21, 30, 70, 18, 7, 37, 81)

    maxheap.insert(27)
    maxheap.insert(19)
    maxheap.insert(17)
    maxheap.insert(14)
    maxheap.insert(20)
    maxheap.insert(21)
    maxheap.insert(30)
    maxheap.insert(70)
    maxheap.insert(18)
    maxheap.insert(7)
    maxheap.insert(37)
    maxheap.insert(81)
    # maxheap.insert(81)

    # maxheap.meld(27, 19, 17)

    print("\n")

    ## achieved with _sift_up()
    ## [81, 37, 70, 20, |30, 27, 21|, 14, 18, 7, 19, 17]


    ## achieved with _heapify_() - the most accurate
    ## [81, 37, 70, 20, |27, 21, 30|, 14, 18, 7, 19, 17]
    


    print(maxheap)