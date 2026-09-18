from ctypes import py_object

class DynArray:

    ## O(n)
    def __init__(self, *args):
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

    ## O(1)
    ## allows us to do: print(x[2:3:5])
    def __getitem__(self, index):
        if isinstance(index, slice):
            start, stop, step = index.indices(self.size)
            result = DynArray()
            for i in range(start, stop, step):
                result.append(self.array[i])
            return result
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
        if self.size == self.capacity:
            self._resize_(self.capacity * 2)

        self.array[self.size] = value
        self.size += 1

    ## O(n)
    def insert(self, index, value):
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
        else:

            if index is None:
                index = (self.size - 1)

            if index < 0:
                index += self.size

            if index < 0 or index >= self.size:
                raise IndexError("List List index out of range.")

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
        
        return self

    ## O(n)
    def copy(self):
        newArr = DynArray(self.size)
        for i in range(self.size):
            newArr.append(self.array[i])
        return newArr

    ## O(n)
    def count(self, value) -> int:
        counter = int(0)

        for i in range(self.size):
            if self.array[i] == value:
                counter += 1
            else:
                continue
        return counter

    ## O(n)
    def index(self, value) -> int:
        for i in range(self.size):
            if self.array[i] == value:
                return i
            else:
                continue
        return -1

    ## O(n)
    def extend(self, elements):
        for el in elements:
            self.append(el)

    ## O(n)
    def clear(self) -> None:
        for i in range(self.size):
            self.pop()

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
    def binSearch(self, target) -> bool:
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
    def linSearch(self, target) -> bool:
        for i in range(self.array):
            if self.array[i] == target:
                return True
        return False


if __name__ == "__main__":
    x = DynArray(1,2,3,4,5)
    
    print(x)

    x.pop(-2)

    # x.clear()

    print(x)



    # lista = list([1,2,3,4,5,6,7])

    # lista.pop(-30)
    # print(lista)