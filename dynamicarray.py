from ctypes import py_object

class DynArray:
    def __init__(self, *args):
        self.capacity = 1
        self.size = 0
        self.array = self._make_array(self.capacity)
        for el in args:
            self.append(el)

    ## O(x)
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

    ## O(1)
    ## print(x[2:3:5])
    def __getitem__(self, index):
        ## Handle slicing
        if isinstance(index, slice):
            start, stop, step = index.indices(self.size)
            result = DynArray()
            for i in range(start, stop, step):
                result.append(self.array[i])
            return result

        # Handle normal indexing
        if index < 0:
            index += self.size
        if index < 0 or index >= self.size:
            raise IndexError("Index out of bounds")
        return self.array[index]

    ## O(1)
    def __setitem__(self, index, value):
        if index < 0 or index >= self.size:
            raise IndexError("Index out of bounds")
        self.array[index] = value

    ## O(n)
    def __delitem__(self, index):
        return self.pop(index)


    ## 1 helper methods, used internally by other methods.
    def _make_array(self, capacity):
        return (capacity * py_object)()  # raw block of pointers

    def _resize(self, new_capacity):
        NewArray = self._make_array(new_capacity)

        for i in range(self.size):
            NewArray[i] = self.array[i]

        self.array = NewArray
        self.capacity = new_capacity


    ## instance methods - 11
    ## O(1)*
    def append(self, value):
        if self.size == self.capacity:
            self._resize(2 * self.capacity)

        self.array[self.size] = value
        self.size += 1

    ## O(n)
    ## insert, but lose the last element if the array is filled up.
    def insert(self, index, value):
        if index < 0 or index >= self.size:
            raise IndexError("Index out of bounds")

        for i in range(self.size-1, index-1, -1):
            self.array[i] = self.array[i - 1]

        self.array[index] = value

        if self.size < self.capacity:
            self.size += 1

    ## O(n)
    def remove(self, value) -> None:
        index = 0
        for i in range(self.size):
            if self.array[i] == value:
                index += i
                break
        else:
            return

        for i in range(index, self.size -1):
            self.array[i] = self.array[i + 1]

        self.array[self.size - 1] = None
        self.size -= 1
    
    ## O(n)
    def pop(self, index=None):
        if self.size == 0:
            raise IndexError("Poping from an empty array")

        if index is None:
            index = self.size - 1

        if index < 0 or index >= self.size:
            raise IndexError("Index out of bounds")

        value = self.array[index]

        for i in range(index, self.size - 1):
            self.array[i] = self.array[i + 1]

        self.array[self.size - 1] = None
        self.size -= 1

        return value

    ## O(n)
    def reverse(self):
        start = int(0)
        stop = (self.size - 1)

        ops = (self.size // 2)

        for i in range(0, ops, 1):
            self.array[start], self.array[stop] = self.array[stop], self.array[start]
            start += 1
            stop -= 1
        
        return self.__str__()

    ## O(n)
    def copy(self):
        newArr = DynArray(self.size)
        for i in range(self.size):
            newArr.append(self.array[i])
        self.array = newArr

    ## O(n)
    def count(self, value):
        counter = int(0)

        for i in range(self.size):
            if self.array[i] == value:
                counter += 1
            else:
                continue
        return counter

    ## O(n)
    def index(self, value):
        for i in range(self.size):
            if self.array[i] == value:
                return i
            else:
                continue
        return -1

    ## O(n)
    def extend(self, elements):
        for i in elements:
            self.append(i)

        return self

    ## O(n)
    def clear(self):
        for i in range(self.size):
            self.array[i] = None
        return self.array

    ## O(n2)
    def bubbleSort(self):

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
    
    ## O(log2 n)
    def binSearch(self, target):
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
    
    ## O(log n)
    def linSearch(self, target):
        for i in range(self.array):
            if self.array[i] == target:
                return True
        return False


if __name__ == "__main__":
    x = DynArray(1,2,3,4,5,6,8)

    print(x)