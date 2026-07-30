from dynamicarray import DynArray
class Queue:

    class _QueueNode_:
        def __init__(self, val):
            self.val = val
            self.prev = None
            self.next = None

    def __init__(self):
        self.right = None
        self.left = None
        self.len = int(0)
    
    ## O(1)
    def __len__(self):
        return self.len
    
    ## O(n)
    def __str__(self):
        arr = DynArray()
        curr = self.left
        for _ in range(0, self.len):
            arr.append(str(curr.val))
            curr = curr.next
        return ' <~> '.join(arr)

    ## O(n)
    def __repr__(self):
        return f"Start -> {self} <- End"

        
    ## O(1)
    def Push(self, val):
        new_node = Queue._QueueNode_(val)

        if self.right == None:
            self.right = new_node
            self.left = new_node
        else:
            self.right.next = new_node
            new_node.prev = self.right
            self.right = new_node
        self.len += int(1)
    
    ## O(1)
    def PopLeft(self):
        val = self.left
        if self.left == None:
           raise ValueError('Empty Stack')
        else:
            newLeft = self.left.next
            self.left.next.prev = None
            self.left.next = None
            self.left = newLeft
            self.len -= int(1)
            return val

    ## O(1)
    def PeekLeft(self):
        if self.left == None:
            raise ValueError('Empty Stack')
        else:
            return str(self.left.val)
    
    ## O(1)
    def PeekRight(self):
        if self.right == None:
            raise ValueError('Empty Stack')
        else:
            return str(self.right.val)


if __name__ == "__main__":
    x = Queue()
    x.Push(1)
    x.Push(2)
    x.Push(3)
    x.Push(4)
    x.Push(5)

    print(x)
    x.PopLeft()
    x.PopLeft()
    print(x)