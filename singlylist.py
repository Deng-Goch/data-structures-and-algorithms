from dynamicarray import DynArray

class SinglyList:
    class _SinglyNode_:
        def __init__(self, value):
            self.value = value
            self.next = None

    ## 8 magic methods
    def __init__(self, *args):
        self.head = None
        self.tail = None
        self.len = 0
        for arg in args:
            self.InsertEnd(arg)
    
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
        return ' -> '.join(arr)
    
    ## o(n)
    def __repr__(self):
        return f"Head => {self} <= Tail"
    
    ## o(n)
    def __iter__(self):
        curr = self.head
        for _ in range(self.len):
            yield curr.value
            curr = curr.next
    
    ## O(n)
    ## allows us to do: 3 in x
    def __contains__(self, item):
        curr = self.head
        for _ in range(1, self.len):
            if item == curr.value:
                return True
            curr = curr.next
        return False

    ## O(n)
    ## allows us to do: print(x[3])
    def __getitem__(self, position):
        if position < 1 or position > self.len:
            raise IndexError("Index out of range.")
        curr = self.head
        for _ in range(1, position):
            curr = curr.next
        return curr.value

    ## O(n)
    ## allows us to do: x[4] = 100
    def __setitem__(self, position, value):
        newNode = SinglyList._SinglyNode_(value)
        if position == 1:
            self.head.value = newNode.value
        elif position == (self.len):
            self.tail.value = newNode.value
        elif position < 1 or position > (self.len):
            raise IndexError("Position Out Of Range.")
        else:
            curr = self.head
            for _ in range(1, position - 1):
                curr = curr.next
            newNode.next = curr.next.next
            curr.next.next = None
            curr.next = newNode



    ## 4 instances methods
    ## op 1 - O(1)
    def InsertStart(self, value):
        newNode = SinglyList._SinglyNode_(value)
        if self.head == None:
            self.head = newNode
            self.tail = newNode
        else:
            newNode.next = self.head
            self.head = newNode
        self.len += int(1)

    ## op 2 - O(1)
    def InsertEnd(self, value):
        newNode = SinglyList._SinglyNode_(value)
        if self.tail == None:
            self.tail = newNode
            self.head = newNode
        else:
            self.tail.next = newNode
            self.tail = newNode
        self.len += int(1)

    ## op 3 - O(n)
    def InsertAt(self, value, position):
        newNode = SinglyList._SinglyNode_(value)
        if position == 1 :
            return SinglyList.InsertStart(self, value)
        elif position == (self.len + 1):
            return SinglyList.InsertEnd(self, value)
        elif position < 1 or position > (self.len + 1):
            raise IndexError("position Out Of Range.")
        else:
            curr = self.head
            for _ in range(1, position-1):
                curr = curr.next
            newNode.next = curr.next
            curr.next = newNode
        self.len += int(1)

    ## op 4 - O(1)
    def DelStart(self):
        if self.head == None:
            raise IndexError("Empty list.")
        else:
            newHead = self.head.next
            self.head.next = None
            self.head = newHead
            self.len -= int(1)


if __name__ == "__main__":
    x = SinglyList(1,2,3,4,5,6,7)

    print(x)