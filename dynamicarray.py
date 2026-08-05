from staticarray import StatArray

class DynArray(StatArray):
    def __init__(self, capacity=8):
       super().__init__(capacity)
    
    def append(self, value):
        if self.size == self.capacity:
            self._resize(2 * self.capacity)

        self.Array[self.size] = value
        self.size += 1
    
    def _resize(self, new_capacity):
        NewArray = self._make_array(new_capacity)

        for i in range(self.size):
            NewArray[i] = self.Array[i]

        self.Array = NewArray
        self.capacity = new_capacity
    


if __name__ == "__main__":
    x = DynArray()
    x.append(1)
    print(x)
    x.append(6)
    print(x)