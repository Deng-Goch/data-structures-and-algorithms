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
    
    ## o(n)
    def __iter__(self):
        curr = self.head
        for i in range(self.len):
            yield curr.value
            curr = curr.next

    ## O(n)
    def __repr__(self) -> str:
        return f"Head => {(self)} <= Tail"

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
        newnode = DoublyList._DoublyNode_(value)
        if position == 1:
            self.DelStart()
            self.InsertStart(value)
        elif position == self.len:
            self.DelEnd()
            self.InsertEnd(value)
        elif position < 1 or position > self.len:
            raise IndexError("Index out of range.")
        else:
            curr = self.head
            for _ in range(1, position):
                curr = curr.next
            curr.next.prev = newnode
            curr.prev.next = newnode
            newnode.prev = curr.prev
            newnode.next = curr.next
            curr = newnode
        
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
    def InsertStart(self, value):
        newnode = DoublyList._DoublyNode_(value)
        if self.head == None:
            self.head = newnode
            self.tail = newnode
        else:
            newnode.next = self.head
            self.head.prev = newnode
            self.head = newnode
        self.len += 1

    ## O(1)
    def InsertEnd(self, val):
        newnode = DoublyList._DoublyNode_(val)
        if self.tail == None:
            self.tail = newnode
            self.head = newnode
        else:
            self.tail.next = newnode
            newnode.prev = self.tail
            self.tail = newnode
        self.len += 1
    
    ## O(n)
    def InsertAt(self, value, position:int):
        newnode = DoublyList._DoublyNode_(value)
        if position == 1:
            self.InsertStart(value)
        elif position == (self.len + 1):
            self.InsertEnd(value)
        elif position < 1 or position > (self.len + 1):
            raise IndexError("Index out of range.")
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
        if self.head == None:
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
        if self.tail == None:
            raise IndexError("Empty Linked List.")
        else:
            del_val = self.tail
            self.tail = self.tail.prev
            self.tail.next.prev = None
            self.tail.next = None
            self.len -= 1
            return del_val.value
    
    ## O(n)
    def RevLinkList(self):
        iters = ((self.len) // 2)
        p1 = self.head
        p2 = self.tail

        for _ in range(iters):
            p1.value, p2.value = p2.value, p1.value
            p1 = p1.next
            p2 = p2.prev
        return self.head


if __name__ == "__main__":
    x = DoublyList(1,2,3,4,5,6,7)

    print(x)
