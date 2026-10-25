class Stack:
    class _StackNode_:
        def __init__(self, value):
            self.value = value
            self.next = None
            self.prev = None


    ## O(n)
    def __init__(self, *args):

        """
        Input: Takes a collection of elements to be inserted into the stack.

        Process: Inserts all the elements one after the other while increasing the length of the stack.

        Output: 

        Error: 
        """

        self.top = None
        self.len = 0
        for arg in args:
            self.push(arg)

    
    ## O(1)
    def __len__(self):
        return self.len


    ## O(1)
    def push(self, value):

        """
        Input: Value of any type to be inserted into the stack.

        Process: Inserts the given value to the stack and increment the lenght.

        Output: 

        Error: 
        """

        newnode = self._StackNode_(value)
        if self.top is None:
            self.top = newnode
        else:
            self.top.next = newnode
            newnode.prev = self.top
            self.top = newnode
        self.len += 1

    
    ## O(1)
    def pop(self):

        """
        Input: 

        Process: Checks if the stack is empty or not, if not, it removes the element on the top of the stack from the stack.

        Output: Returns the popped element, i.e., the one on top of the stack.

        Error: Throws "ValueError('Empty Stack')" if called on an empty stack.
        """

        if self.top is None:
           raise ValueError('Empty Stack')
        else:
            popped = self.top.value
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

        """
        Input: 

        Process: Checks if the stack is empty or not.

        Output: Returns the value that's on the top of the stack.

        Error: Throws a "ValueError('Empty Stack')" if called on an empty stack.
        """

        if self.top is None:
            raise ValueError('Empty Stack')
        else:
            return (f'{str(self.top.value)}')


if __name__ == "__main__":
    x = Stack(1,2,3,4,5,6,7,8,9,10)

    print(x.peek())
