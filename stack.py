class Stack:
    class _StackNode_:
        def __init__(self, val):
            self.val = val
            self.prev = None
            self.next = None

    ## O(1)
    def __init__(self):
        self.top = None
        self.len = 0
    
    ## O(1)
    def __len__(self):
        return self.len


    ## O(1)
    def push(self, val):
        newNode = Stack._StackNode_(val)
        if self.top is None:
            self.top = newNode
        else:
            self.top.next = newNode
            newNode.prev = self.top
            self.top = newNode
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
        if self.top.val is None:
            raise ValueError('Empty Stack')
        else:
            return print(f'{str(self.top.val)}')


if __name__ == "__main__":
    x = Stack()
    x.push(1)
    x.push(2)
    x.push(3)
    print(x.pop())
    print(x.pop())
    print(x.pop())
    print(x.pop())