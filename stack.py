class Stack:
    class _StackNode_:
        def __init__(self, val):
            self.val = val
            self.next = None
            self.prev = None

    ## O(n)
    def __init__(self, *args):
        self.top = None
        self.len = 0
        for arg in args:
            self.push(arg)
    
    ## O(1)
    def __len__(self):
        return self.len


    ## O(1)
    def push(self, val):
        newnode = self._StackNode_(val)
        if self.top is None:
            self.top = newnode
        else:
            self.top.next = newnode
            newnode.prev = self.top
            self.top = newnode
        self.len += 1
    
    ## O(1)
    def pop(self):
        if self.top is None:
           raise ValueError('Empty Stack')
        else:
            popped = self.top.val
            if self.len == 1:
                self.top = None
            else:
                self.top = self.top.prev
                self.top.next.prev = None
                self.top.next = None
            self.len -= 1
            return popped

    ## O(1)
    def peek(self):
        if self.top is None:
            raise ValueError('Empty Stack')
        else:
            return (f'{str(self.top.val)}')


if __name__ == "__main__":
    x = Stack()

    print(x.peek())
