from dynamicarray import DynArray

class CirclyList:
    class _CirclyNode_:
        def __init__(self, value=None):
            self.value = value
            self.next = None
            self.prev = None

    ## magic methods - 8

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
    def __str__(self):
        arr = DynArray()
        curr = self.head
        for _ in range(1, self.len + 1):
            arr.append(str(curr.value))
            curr = curr.next
        return ' ~ '.join(arr)
            
    ## O(n)
    def __repr__(self):
        return f"{self.tail.value} <-> {(self)} <-> {self.head.value}"

    ## O(n)
    ## print(7 in x)
    def __contains__(self, item) -> bool:
        curr = self.head
        for _ in range(1, self.len + 1):
            if curr.value == item:
                return True
            curr = curr.next
        return False
    
    ## o(n)
    def __iter__(self):
        curr = self.head
        for i in range(self.len):
            yield curr.value
            curr = curr.next
    
    ## O(n)
    ## print(x[5])
    def __getitem__(self, position):
        if position == 1:
            return self.head.value
        elif position == self.len:
            return self.tail.value
        elif position < 1 or position > (self.len):
            raise IndexError("Index out of range.")
        else:
            curr = self.head
            for _ in range(1, position):
                curr = curr.next
        return curr.value

    ## O(n)
    ## x[3] = 9
    def __setitem__(self, position, value):
        newnode = CirclyList._CirclyNode_(value)
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
    ## del x[7]
    def __delitem__(self, position):
        if position == 1:
            self.DelStart()
        elif position == self.len:
            self.DelEnd()
        elif position < 1 or position > self.len:
            raise IndexError("Position out of range.")
        else:
            curr = self.head
            for _ in range(1, position):
                curr = curr.next
            curr.prev.next = curr.next
            curr.next.prev = curr.prev
            curr.next = None
            curr.prev = None
        self.len -= 1
    

    ### instance methods - 5
    ## O(1)
    def InsertStart(self, value):
        newnode = CirclyList._CirclyNode_(value)
        if self.head == None:
            self.head = newnode
            self.tail = newnode
            self.head.prev = self.tail
            self.tail.next = self.head
        else:
            newnode.next = self.head
            self.head.prev = newnode
            self.head = newnode
            self.head.prev = self.tail
            self.tail.next = self.head
        self.len += 1

    ## O(1)
    def InsertEnd(self, val):
        newnode = CirclyList._CirclyNode_(val)
        if self.tail == None:
            self.tail = newnode
            self.head = newnode
            self.tail.next = self.head
            self.head.prev = self.tail
        else:
            newnode.next = self.head
            self.tail.next = newnode
            self.head.prev = newnode
            newnode.prev = self.tail
            self.tail = newnode
        self.len += 1
    
    ## O(n)
    def InsertAt(self, value, pos:int):
        newnode = CirclyList._CirclyNode_(value)
        if pos == 1:
           self.InsertStart(value)
        elif pos == (self.len + 1):
           self.InsertEnd(value)
        elif pos < 1 or pos > (self.len + 1):
            raise IndexError("Index out of range.")
        else:
            curr = self.head
            for _ in range(1, pos - 1):
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
            self.head.prev.prev = None
            self.head.prev = self.tail
            self.tail.next = self.head
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
            self.tail.next.next = None
            self.tail.next = self.head
            self.head.prev = self.tail
            self.len -= 1
            return del_val.value


if __name__ == "__main__":
    x = CirclyList(1,2,3,4,5,6,7,8)

    print(x)