from dynamicarray import DynArray

class DoublyList:
    class _DoublyNode_:
        def __init__(self, value):
            self.value = value
            self.next = None
            self.prev = None

    ## 8 magic method
    ## O(n)
    def __init__(self, *args):

        """
        Input: 

        Process: 

        Output: 

        Error: 
        """

        self.head = None
        self.tail = None
        self.len = 0
        for arg in args:
            self.InsertEnd(arg)


    ## O(1)
    def __len__(self) -> int:
        return self.len

    
    ## O(n)
    def __str__(self) -> str:
        arr = DynArray()
        curr = self.head
        while curr:
            arr.append(str(curr.value))
            curr = curr.next
        return ' <-> '.join(arr)


    ## O(n)
    def __repr__(self) -> str:
        return f"Head => {(self)} <= Tail"
    
    
    ## o(n)
    def __iter__(self):
        curr = self.head
        for _ in range(self.len):
            yield curr.value
            curr = curr.next


    ## O(n)
    ## allows us to do: 27 in x
    def __contains__(self, item) -> bool:
        curr = self.head
        for _ in range(1, self.len + 1):
            if curr.value == item:
                return True
            else:
                curr = curr.next
        return False

    
    ## O(n)
    ## allows us to do: print(x[3])
    def __getitem__(self, position):
        if position == 1:
            return self.head.value
        elif position == self.len:
            return self.tail.value
        elif position < 1 or position > (self.len + 1):
            raise IndexError("Index out of range.")
        else:
            curr = self.head
            for _ in range(1, position):
                curr = curr.next
        return curr.value
    

    ## O(n)
    ## allows us to do: x[3] = 10
    def __setitem__(self, position, value):
        if position == 1:
            self.head.value = value
        elif position == self.len:
            self.tail.value = value
        elif position < 1 or position > self.len:
            raise IndexError("Index out of range.")
        else:
            curr = self.head
            for _ in range(1, position):
                curr = curr.next
            curr.value = value

        
    ## O(n)
    ## allows us to do: del x[7]
    def __delitem__(self, position):
        if position == 1:
            self.DelStart()
        elif position == self.len:
            self.DelEnd()
        elif position < 1 or position > self.len:
            raise IndexError("Index out of range.")
        else:
            curr = self.head
            for _ in range(1, position):
                curr = curr.next
            curr.prev.next = curr.next
            curr.next.prev = curr.prev
            curr.next = None
            curr.prev = None
        self.len -= 1


    ### 6 instance methods
    ## O(1)
    def InsertStart(self, value) -> None:

        """
        Input: 

        Process: 

        Output: 

        Error: 
        """

        newnode = self._DoublyNode_(value)
        if self.head is None:
            self.head = newnode
            self.tail = newnode
        else:
            newnode.next = self.head
            self.head.prev = newnode
            self.head = newnode
        self.len += 1


    ## O(1)
    def InsertEnd(self, value) -> None:

        """
        Input: 

        Process: 

        Output: 

        Error: 
        """

        newnode = self._DoublyNode_(value)
        if self.tail is None:
            self.tail = newnode
            self.head = newnode
        else:
            self.tail.next = newnode
            newnode.prev = self.tail
            self.tail = newnode
        self.len += 1

    
    ## O(n)
    def InsertAt(self, value, position:int) -> None:

        """
        Input: 

        Process: 

        Output: 

        Error: 
        """

        newnode = self._DoublyNode_(value)
        if position == 1:
            self.InsertStart(value)
        elif position == (self.len + 1):
            self.InsertEnd(value)
        elif position < 1 or position > (self.len + 1):
            raise IndexError("Position Out Of Range.")
        else:
            curr = self.head
            for _ in range(1, position - 1):
                curr = curr.next
            newnode.next = curr.next
            newnode.next.prev = newnode
            newnode.prev = curr
            curr.next = newnode
        self.len += 1


    ## O(1)
    def DelStart(self):

        """
        Input: 

        Process: 

        Output: 

        Error: 
        """

        if self.head is None:
            raise IndexError("Empty Linked List.")
        else:
            del_val = self.head
            self.head = self.head.next
            self.head.prev.next = None
            self.head.prev = None
            self.len -= 1
            return del_val.value

    
    ## O(1)
    def DelEnd(self):

        """
        Input: 

        Process: 

        Output: 

        Error: 
        """

        if self.tail is None:
            raise IndexError("Empty Linked List.")
        else:
            del_val = self.tail
            self.tail = self.tail.prev
            self.tail.next.prev = None
            self.tail.next = None
            self.len -= 1
            return del_val.value

    
    ## O(n)
    def RevLinkList(self) -> None:

        """
        Input: 

        Process: 

        Output: 

        Error: 
        """

        iters = ((self.len) // 2)
        left = self.head
        right = self.tail

        for _ in range(iters):
            left.value, right.value = right.value, left.value
            left = left.next
            right = right.prev


if __name__ == "__main__":
    x = DoublyList(1,2,3,4,5,6,7)

    print(x)

    x.InsertAt('XY', 4)

    print(x)