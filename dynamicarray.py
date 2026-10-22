from ctypes import py_object

class DynArray:

    ## O(n)
    def __init__(self, *args):

        """
        Input: Capacity: A collection of arguments seprated by a ",". "Optional"

        Process: Inserts all the argumnets into static array one after the other.

        Output: A static array object.

        Error:
        """

        self.capacity = 1
        self.size = 0
        self.array = self._make_array_(self.capacity)
        for arg in args:
            self.append(arg)


    ## O(1)
    def __len__(self):
        return self.size

    
    ## O(n)
    def __iter__(self):
        for i in range(self.size):
            yield self.array[i]


    ## O(n)
    def __str__(self):
        if self.size == 0:
            return "[]"
        elif self.size == 1:
            return f"[{self.array[0]}]"
        else:
            rep = str("")
            for i in range(self.size-1):
                rep += str(f"{self.array[i]}, ")

            rep += str(self.array[i+1])
            return "[" + rep + "]"


    ## O(1)*
    ## allows us to do: print(x[2:3:5])
    def __getitem__(self, index):
        ## slicing
        if isinstance(index, slice):
            start, stop, step = index.indices(self.size)
            result = DynArray()
            for i in range(start, stop, step):
                result.append(self.array[i])
            return result
        ## normal indexing
        else:
            if index < 0:
                index += self.size

            if index < 0 or index >= self.size:
                raise IndexError("List index out of range.")
            else:
                return self.array[index]


    ## O(1)
    ## allows us to do: x[3] = 100
    def __setitem__(self, index, value):
        if index < 0:
            index += self.size

        if index < 0 or index >= self.size:
            raise IndexError("List index out of range.")
        else:
            self.array[index] = value


    ## O(n)
    ## allows us to do: del x[3]
    def __delitem__(self, index):
        return self.pop(index)


    ## 1 helper methods, used internally by other methods.
    def _make_array_(self, capacity):
        return (capacity * py_object)()  # raw block of pointers


    def _resize_(self, new_capacity):
        NewArray = self._make_array_(new_capacity)

        for i in range(self.size):
            NewArray[i] = self.array[i]

        self.array = NewArray
        self.capacity = new_capacity


    ## instance methods - 11
    ## O(1)*
    def append(self, value):

        """
        Input: 

        Process: 

        Output: 

        Error: 
        """

        if self.size == self.capacity:
            self._resize_(self.capacity * 2)

        self.array[self.size] = value
        self.size += 1


    ## O(n)
    def insert(self, index, value) -> None:

        """
        Input: 

        Process: 

        Output: 

        Error: Throws a "TypeError: insert expected 2 arguments, got 0, 1" if no argument is passed in or 1 argument is passed in - 
        """
        if index < 0:
            index += self.size

        if index < 0 or index >= self.size:
            raise IndexError("List index out of range.")
        else:
            if self.size == self.capacity:
                self._resize_(self.capacity * 2)

            for i in range(self.size, index, -1):
                self.array[i] = self.array[i-1]

            self.array[index] = value
            self.size += 1


    ## O(n)
    def remove(self, value) -> None:

        """
        Input: 

        Process: 

        Output: 

        Error: 
        """

        index = 0
        for i in range(self.size):
            if self.array[i] == value:
                index += i
                break
        else:
            raise ValueError("DynArray.remove(x): x not in DynArray.")

        for i in range(index, self.size -1):
            self.array[i] = self.array[i + 1]

        self.array[self.size - 1] = None
        self.size -= 1

    
    ## O(n)
    def pop(self, index=None):

        """
        Input: Index: An integer positive or negative to determine the index of the element to be popped. "Optional". If not provided, it's equals the length of the array - 1, i.e., the last array element.

        Process: Pop the element by position/index and move all the elements to the right of it to left by one move each.

        Output: The popped array element.

        Error: 
        """

        if self.size == 0:
            raise IndexError("Poping from an empty array")
        else:

            if index is None:
                index = (self.size - 1)

            if index < 0:
                index += self.size

            if index < 0 or index >= self.size:
                raise IndexError("List index out of range.")

            value = self.array[index]

            for i in range(index, self.size - 1):
                self.array[i] = self.array[i + 1]

            self.array[self.size - 1] = None
            self.size -= 1

            return value


    ## O(n)
    def reverse(self) -> None:

        """
        Input: 

        Process: Reverse DynArray elements.

        Output: 

        Error: 
        """

        left = int(0)
        right = (self.size - 1)

        iters = (self.size // 2)

        for i in range(0, iters, 1):
            self.array[left], self.array[right] = self.array[right], self.array[left]
            left += 1
            right -= 1


    ## O(n)
    def copy(self):

        """
        Input: 

        Process: 

        Output: 

        Error: 
        """

        newArr = DynArray()
        for i in range(self.size):
            newArr.append(self.array[i])
        return newArr


    ## O(n)
    def count(self, value) -> int:

        """
        Input: 

        Process: 

        Output: 

        Error: 
        """

        counter = 0

        for i in range(self.size):
            if self.array[i] == value:
                counter += 1
            else:
                continue
        return counter


    ## O(n)
    def index(self, value, start=0, stop=None) -> int:

        """
        Input: 

        Process: 

        Output: 

        Error:
        
        Throws
        
        A "TypeError: index expected at least 1 argument, got 0" if no argument given.
        
        A "ValueError: 'x' is not in DynArray" if the given value is not in the array.

        """

        if start == 0:
            start = 0

        if stop is None:
            stop = self.size


        for i in range(start, stop):
            if self.array[i] == value:
                return i
            else:
                continue
        else:
            raise ValueError("ValueError: 'x' is not in DynArray")


    ## O(n)
    def extend(self, Iterable) -> None:

        """
        Input: 

        Process: 

        Output: 

        Error: 
        """

        for arg in Iterable:
            self.append(arg)


    ## O(n)
    def clear(self) -> None:

        """
        Input: 

        Process: 

        Output: 

        Error: 
        """

        for i in range(self.size):
            self.pop()


    ## O(n^2)
    def bubbleSort(self):

        """
        Input: 

        Process: 

        Output: 

        Error: 
        """

        swap = True
        iters = ((self.size)-1)

        while swap:
            swap = False
            for i in range(iters):
                if self.array[i] > self.array[i+1]:
                    self.array[i], self.array[i+1] = self.array[i+1], self.array[i]
                    swap = True
            iters -= 1
        return self.array


    ## O(log n)
    def linSearch(self, target) -> bool:

        """
        Input: 

        Process: 

        Output: 

        Error: 
        """

        for i in range(self.array):
            if self.array[i] == target:
                return True
        return False

    
    ## O(log2 n)
    def binSearch(self, target) -> bool:

        """
        Input: 

        Process: 

        Output: 

        Error: 
        """

        self.bubbleSort()

        le = 0
        ri = (len(self.array)-1)

        while le <= ri:
            mid = ((ri + le) // 2)
            if self.array[mid] == target:
                return True
            elif self.array[mid] > target:
                ri = (mid - 1)
            elif self.array[mid] < target:
                le = (mid + 1)
        return False


if __name__ == "__main__":
    x = DynArray(5,100,0,-7)
    print(x)

    x.bubbleSort()
    
    print(x)