from dynamicarray import DynArray

class Heap_Based_Max_Priority_Queue:
    def __init__(self, *args):
        self.heap = DynArray()
        for arg in args:
            self.push(arg)


    def __str__(self):
        return str(self.heap)


    def __len__(self):
        return len(self.heap)


    ## 5 internal helper methods
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
    def _sift_up_(self, index:int) -> int:
        parent = self._parent_(index)

        if parent >= 0:

            left = self._left_(parent)
            right = self._right_(parent)

            if left <= (len(self.heap)-1) and right <= (len(self.heap)-1):

                if self.heap[left][0] > self.heap[parent][0]:
                    self.heap[left], self.heap[parent] = self.heap[parent], self.heap[left]
                    
                elif self.heap[right][0] > self.heap[parent][0]:
                    self.heap[right], self.heap[parent] = self.heap[parent], self.heap[right]
                    
                if self.heap[left][0] > self.heap[right][0]:
                    self.heap[left], self.heap[right] = self.heap[right], self.heap[left]
                self._sift_up_(parent)

            elif left <= (len(self.heap)-1):

                if self.heap[left][0] > self.heap[parent][0]:
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
            if self.heap[left][0] > self.heap[right][0]:
                self.heap[left], self.heap[right] = self.heap[right], self.heap[left]
            self._sift_down_(left)

        elif left <= (len(self.heap)-1):
            if self.heap[index][0] < self.heap[left][0]:
                self.heap[index], self.heap[left] = self.heap[left], self.heap[index]
                self._sift_down_(right)
        else:
            return


    ## methods / operations
    ## O(log2 n)
    def push(self, priority, value) -> None:

        """
        Input:
        Priority: this has to be a value of the same type, mostly int.
        Value: It could be anything.

        Action:
        It returns nothing, but it adds the element to the queue and insert it to its right place.

        Error:
        if priorities of different types are input, it throws "TypeError: '<' not supported between instances of 'int' and 'str'"
        """
        
        node = tuple((priority, value))
        self.heap.append(node)

        self._sift_up_(len(self.heap)-1)


    ## O(1)
    def pop(self) -> None:

        """
        Action: it removes the element with the least priority.

        Error: if the queue is empty, it throws "IndexError: Empty Priority Queue."

        """

        if len(self.heap) == 0:
            raise IndexError('Empty Priority Queue.')
        else:
            self.heap[0] = self.heap[len(self.heap)-1]
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
            raise IndexError('Empty Priority Queue.')
        else:
            return self.heap[0]



if __name__ == "__main__":
    pq = Heap_Based_Max_Priority_Queue()
    # pq.push(7, 'Deng')
    # pq.push(9, 'Goch')
    # pq.push(6, 'Monydhot')
    # pq.push('z', 'Yor')
    # pq.push(4, 'DENG')

    print(pq)

    pq.pop()

    # print("\n")

    # print(pq)

    # pq.push(15, 'Pakodi')

    # print(pq)

    # print(pq.peek())
