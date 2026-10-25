from dynamicarray import DynArray

class Heap_Based_Min_Priority_Queue:

    ## 3 magic methods
    def __init__(self):
        self.heap = DynArray()


    def __str__(self):
        return str(self.heap)


    def __len__(self):
        return len(self.heap)


    ## 3 internal helper methods
    ## O(1)
    def _parent_(self, index:int) -> int:
        return ((index - 1) // 2)


    ## O(1)
    def _left_(self, index:int) -> int:
        return ((index * 2) + 1)


    ## O(1)
    def _right_(self, index:int) -> int:
        return ((index * 2) + 2)


    ## O(log2 n) - used for inserting
    def _sift_up_(self, index:int):
        parent = self._parent_(index)

        if parent >= 0:

            left = self._left_(parent)
            right = self._right_(parent)

            if left < (len(self.heap)) and right < (len(self.heap)):
                
                if self.heap[left][0] < self.heap[parent][0]:
                    self.heap[left], self.heap[parent] = self.heap[parent], self.heap[left]
                    self._sift_up_(parent)
                elif self.heap[right][0] < self.heap[parent][0]:
                    self.heap[right], self.heap[parent] = self.heap[parent], self.heap[right]
                    self._sift_up_(parent)
                else:
                    return

            elif left < len(self.heap):
                if self.heap[left][0] < self.heap[parent][0]:
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

            if self.heap[left][0] < self.heap[right][0] and self.heap[left][0] < self.heap[index][0]:
                self.heap[left], self.heap[index] = self.heap[index], self.heap[left]
                self._sift_down_(left)

            elif self.heap[right][0] < self.heap[left][0] and self.heap[right][0] < self.heap[index][0]:
                self.heap[right], self.heap[index] = self.heap[index], self.heap[right]
                self._sift_down_(right)

        elif left < (len(self.heap)):
            if self.heap[left][0] < self.heap[index][0]:
                self.heap[left], self.heap[index] = self.heap[index], self.heap[left]
                self._sift_down_(left)
            
        else:
            return


    ## 3 methods / operations
    ## O(log2 n)
    def push(self, priority, value) -> None:

        """
        Input: 

        Process: 

        Output: 

        Error: 
        """

        node = tuple((priority, value))
        self.heap.append(node)

        self._sift_up_(len(self.heap)-1)


    ## O(log2 n)
    def pop(self):

        """
        Input: 

        Process: 

        Output: 

        Error: 
        """
        if len(self.heap) == 0:
            raise IndexError('Empty Priority Queue.')
        else:
            self.heap[0], self.heap[len(self.heap)-1] = self.heap[len(self.heap)-1], self.heap[0]
            self.heap.pop()
            self._sift_down_(0)


    ## O(1)
    def peek(self):

        """
        Input: 

        Process: 

        Output: 

        Error: 
        """

        if len(self.heap) == 0:
            raise IndexError("Empty Priority Queue.")
        else:
            return self.heap[0]



if __name__ == "__main__":
    pq = Heap_Based_Min_Priority_Queue()
    pq.push(7, 'Deng')
    pq.push(3, 'Goch')
    pq.push(6, 'Monydhot')
    pq.push(9, 'Yor')
    pq.push(8, 'DENG')

    print(pq)

    pq.push(1, "Yassin")

    print(pq)

    pq.pop()

    print(pq)