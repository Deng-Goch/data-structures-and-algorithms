from dynamicarray import DynArray

class DoublyList:
    class _DoublyNode_:
        def __init__(self, value):
            self.value = value
            self.next = None
            self.prev = None

    ## 8 magic method
    
    ## O(1)
    def __init__(self):
        self.head = None
        self.tail = None
        self.len = 0

    ## O(1)
    def __len__(self):
        return self.len
    
    ## O(n)
    def __str__(self):
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
    def __repr__(self):
        return f"Head => {(self)} <= Tail"

    ## 27 in x
    ## O(n)
    def __contains__(self, item):
        curr = self.head
        for _ in range(1, self.len + 1):
            if curr.value == item:
                return True
            else:
                curr = curr.next
        return False
    
    ## print(x[3])
    ## O(1)
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
    
    ## x[3] = 10
    ## O(1)
    def __setitem__(self, position, value):
        newNode = DoublyList._DoublyNode_(value)
        if position == 1:
            self.DelStart()
            return self.InsertStart(value)
        elif position == self.len:
            self.DelEnd()
            return self.InsertEnd(value)
        elif position < 1 or position > self.len:
            raise IndexError("Index out of range.")
        else:
            curr = self.head
            for _ in range(1, position):
                curr = curr.next
            curr.next.prev = newNode
            curr.prev.next = newNode
            newNode.prev = curr.prev
            newNode.next = curr.next
            curr = newNode
        
    ## del x[7]
    ## O(1)
    def __delitem__(self, position):
        if position == 1:
            return DoublyList.DelStart(self)
        elif position == self.len:
            return DoublyList.DelEnd(self)
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
        newNode = DoublyList._DoublyNode_(value)
        if self.head == None:
            self.head = newNode
            self.tail = newNode
        else:
            newNode.next = self.head
            self.head.prev = newNode
            self.head = newNode
        self.len += 1

    ## O(1)
    def InsertEnd(self, val):
        newNode = DoublyList._DoublyNode_(val)
        if self.tail == None:
            self.tail = newNode
            self.head = newNode
        else:
            self.tail.next = newNode
            newNode.prev = self.tail
            self.tail = newNode
        self.len += 1
    
    ## O(n)
    def InsertAt(self, value, position:int):
        newNode = DoublyList._DoublyNode_(value)
        if position == 1:
            return DoublyList.InsertStart(self, value)
        elif position == (self.len + 1):
            return DoublyList.InsertEnd(self, value)
        elif position < 1 or position > (self.len + 1):
            raise IndexError("Index out of range.")
        else:
            curr = self.head
            for _ in range(1, position - 1):
                curr = curr.next
            newNode.next = curr.next
            newNode.next.prev = newNode
            newNode.prev = curr
            curr.next = newNode
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

        for i in range(iters):
            p1.value, p2.value = p2.value, p1.value
            p1 = p1.next
            p2 = p2.prev
        return self.head


if __name__ == "__main__":
    x = DoublyList()
    x.InsertEnd(1)
    x.InsertEnd(2)
    x.InsertEnd(3)
    x.InsertEnd(4)
    x.InsertEnd(5)
    # x.InsertEnd(6)

    print(x)

    x.RevLinkList()
    print(x)

    ## output: 5 <-> 4 <-> 3 <-> 2 <-> 1