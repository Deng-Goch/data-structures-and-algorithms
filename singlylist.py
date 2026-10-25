from dynamicarray import DynArray
from stack import Stack

class SinglyList:
    class _SinglyNode_:
        def __init__(self, value):
            self.value = value
            self.next = None


    ## 8 magic methods
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
    def __contains__(self, item) -> bool:
        curr = self.head
        for _ in range(1, self.len):
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
            raise IndexError("Position out of range.")
        else:
            curr = self.head
            for _ in range(1, position):
                curr = curr.next
        return curr.value


    ## O(n)
    ## allows us to do: x[3] = 100
    def __setitem__(self, position, value):
        if position == 1:
            self.head.value = value
        elif position == (self.len):
            self.tail.value = value
        elif position < 1 or position > (self.len):
            raise IndexError("Position Out Of Range.")
        else:
            curr = self.head
            for _ in range(1, position):
                curr = curr.next
            curr.value = value


    ## 4 instances methods
    ## sO(1)
    def InsertStart(self, value) -> None:

        """
        Input: 

        Process: 

        Output: 

        Error: 
        """

        newnode = self._SinglyNode_(value)
        if self.head is None:
            self.head = newnode
            self.tail = newnode
        else:
            newnode.next = self.head
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

        newnode = self._SinglyNode_(value)
        if self.tail is None:
            self.tail = newnode
            self.head = newnode
        else:
            self.tail.next = newnode
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

        newnode = self._SinglyNode_(value)
        if position == 1 :
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
            newHead = self.head.next
            self.head.next = None
            self.head = newHead
            self.len -= 1
            return del_val.value


    ## O(n)
    def RevLinkList(self):

        """
        Input: 

        Process: 

        Output: 

        Error: 
        """

        stak = Stack()

        for node in self:
            stak.push(node)

        curr = self.head
        for node in range(len(self)):
            curr.value = stak.pop()
            curr = curr.next


if __name__ == "__main__":
    x = SinglyList(1,2,3,4,5,6,7)

    print(x)

    x.revLinkList()

    print(x)