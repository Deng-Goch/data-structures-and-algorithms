from dynamicarray import DynArray

class Queue:
    class _QueueNode_:
        def __init__(self, val):
            self.val = val
            self.prev = None
            self.next = None

    def __init__(self, *args):
        self.right = None
        self.left = None
        self.len = 0
        for arg in args:
            self.Push(arg)
    
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
        self.len += 1
    
    ## O(1)
    def PopLeft(self):
        if self.left is None:
           raise ValueError('Empty Stack')
        else:
            popped = self.left.val
            if self.len == 1:
                self.left = None
                self.right = None
            else:
                newLeft = self.left.next
                newLeft.prev = None
                self.left.next = None
                self.left = newLeft
            self.len -= 1
            return popped

    ## O(1)
    def PeekLeft(self):
        if self.left is None:
            raise ValueError('Empty Stack')
        else:
            return str(self.left.val)
    
    ## O(1)
    def PeekRight(self):
        if self.right is None:
            raise ValueError('Empty Stack')
        else:
            return str(self.right.val)


if __name__ == "__main__":
    x = Queue(1,2,3,4,5,6,7)

    print(x)