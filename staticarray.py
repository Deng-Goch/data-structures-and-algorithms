from ctypes import py_object

class StatArray:
    ## 7 magic methods
    ## O(x)
    def __init__(self, capacity):
        self.capacity = capacity
        self.size = int(0)
        self.Array = self._make_array(self.capacity)

    ## O(x)
    def __len__(self):
        return self.size
    
    ## O(n)
    def __iter__(self):
        for i in range(self.size):
            yield self.Array[i]

    ## O(n)
    def __str__(self):
        if self.size == 0:
            return "[]"
        elif self.size == 1:
            return f"[{self.Array[0]}]"
        else:
            rep = str("")
            for i in range(self.size-1):
                rep += str(f"{self.Array[i]}, ")

            rep += str(self.Array[i+1])
            return "[" + rep + "]"

    ## O(1)
    ## print(x[2:3:5])
    def __getitem__(self, index):
        ## Handle slicing
        if isinstance(index, slice):
            start, stop, step = index.indices(self.size)
            result = StatArray(self.size)
            for i in range(start, stop, step):
                result.append(self.Array[i])
            return result

        # Handle normal indexing
        if index < 0:
            index += self.size
        if index < 0 or index >= self.size:
            raise IndexError("Index out of bounds")
        return self.Array[index]

    ## O(1)
    def __setitem__(self, index, value):
        if index < 0 or index >= self.size:
            raise IndexError("Index out of bounds")
        self.Array[index] = value

    ## O(n)
    def __delitem__(self, index):
        return self.pop(index)


    ## 1 helper methods, used internally by other methods.
    def _make_array(self, capacity):
        return (capacity * py_object)()  # raw block of pointers


    ## instance methods - 11
    ## O(1)*
    def append(self, value):
        if self.size == self.capacity:
            raise BufferError('No Empty Space - Array filled up.')
        self.Array[self.size] = value
        self.size += 1

    ## O(n)
    ## insert, but lose the last element if the array is filled up.
    def insert(self, index, value):
        if index < 0 or index >= self.size:
            raise IndexError("Index out of bounds")

        for i in range(self.size-1, index-1, -1):
            self.Array[i] = self.Array[i - 1]

        self.Array[index] = value

        if self.size < self.capacity:
            self.size += 1

    ## O(n)
    def pop(self):
        self.Array[self.size - 1] = None
        self.size -= 1

        return self.Array[self.size - 1]
    
    ## O(n)
    def remove(self, index=None):
        if self.size == 0:
            raise IndexError("Poping from an empty array")

        if index is None:
            index = self.size - 1

        if index < 0 or index >= self.size:
            raise IndexError("Index out of bounds")

        value = self.Array[index]

        # Shift left
        for i in range(index, self.size - 1):
            self.Array[i] = self.Array[i + 1]

        self.Array[self.size - 1] = None
        self.size -= 1

        return value

    ## O(n)
    def reverse(self):
        start = int(0)
        stop = (self.size - 1)

        ops = (self.size // 2)

        for i in range(0, ops, 1):
            self.Array[start], self.Array[stop] = self.Array[stop], self.Array[start]
            start += 1
            stop -= 1
        
        return self.__str__()

    ## O(n)
    def copy(self):
        newArr = StatArray(self.size)
        for i in range(self.size):
            newArr.append(self.Array[i])
        self.Array = newArr

    ## O(n)
    def count(self, value):
        counter = int(0)

        for i in range(self.size):
            if self.Array[i] == value:
                counter += 1
            else:
                continue
        return counter

    ## O(n)
    def index(self, value):
        for i in range(self.size):
            if self.Array[i] == value:
                return i
            else:
                continue
        return int(-1)

    ## O(n)
    def extend(self, elements):
        for i in elements:
            self.append(i)

        return self

    ## O(n)
    def clear(self):
        for i in range(self.size):
            self.Array[i] = None
        return self.Array

    ## O(log2 n)
    def mergeSort(self):
        theArr = self.Array
        pass
    
    ## O(log2 n)
    def binSearch(self, target):
        self.mergeSort()

        le = 0
        ri = (len(self.Array)-1)

        while le <= ri:
            mid = ((ri + le) // 2)
            if self.Array[mid] == target:
                return True
            elif self.Array[mid] > target:
                ri = (mid - 1)
            elif self.Array[mid] < target:
                le = (mid + 1)
        return False
    
    ## O(log n)
    def linSearch(self, target):
        for i in range(self.Array):
            if self.Array[i] == target:
                return True
        return False


if __name__ == "__main__":
    x = StatArray(20)
    x.append(1)
    x.append(2)
    x.append(3)
    x.append(4)
    x.append(5)
    x.append(6)
    x.append(7)
    x.append(8)
    x.append(9)
    x.append(10)
    x.append(11)
    x.append(12)

    print(x)

    # print(x[2:12:2])

    # x = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']

    # y = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
    # print(x[3:8:2])