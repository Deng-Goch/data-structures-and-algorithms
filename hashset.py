from hashtable import HashTable

class HashSet:
    ## magic methods - 5
    ## O(1)
    def __init__(self):
        self._table = HashTable()

    ## O(n)
    def __iter__(self):
        for i in range(self._table.size):
            yield self._table.keys()[i]

    ## O(n)
    def __repr__(self):
        if len(self) > 0:
            rep = str("")
            for i in range(self._table.size):
                rep += str(self._table.keys()[i])

                if i != (self._table.size - 1):
                    rep += ", "

            return "{" + rep + "}"
        else:
            return 'set()'

    ## O(1)
    def __contains__(self, value):
        if value in self._table:
            return True
        else:
            return False

    ## O(1)
    def __len__(self):
        return (self._table.size)


    ## instance methods - 17
    # O(1)
    def add(self, element) -> None:
        if element in self._table:
            return
        else:
            self._table.update(element, None)

    ## O(n)
    def update(self, Iterable) -> None:
        for key in Iterable:
            self.add(key)

    ## O(1)
    def discard(self, element:object) -> None:
        if element in self._table:
            del self._table[element]
        else:
            return

    ## O(1)
    def remove(self, element:object) -> None:
        if element in self._table:
            del self._table[element]
        else:
            raise KeyError

    ## O(1)
    def pop(self):
        if len(self) > 0:
            poped = self._table.keys()[0]
            del self._table[poped]
            return poped
        else:
            raise KeyError('Pop from an empty set.')

    ## O(n)
    def clear(self) -> None:
        for key in self:
            del self._table[key]
    
    ## O(n)
    def copy(self) -> 'HashSet':
        NewSet = HashSet()

        for key in self:
            NewSet.add(key)
        return NewSet



    ## 10 set operations
    ## O(n)
    def isdisjoint(self, Iterable) -> bool:
        for key in Iterable:
            if key in self:
                return False
            else:
                continue
        return True

    ## O(n)
    def issubset(self, Iterable) -> bool:
        for key in self:
            if key in Iterable:
                continue
            else:
                return False
        return True

    ## O(n)
    def issuperset(self, Iterable) -> bool:
        for key in Iterable:
            if key in self:
                continue
            else:
                return False
        return True

    ## O(n)
    def union(self, Iterable) -> 'HashSet':
        NewSet = HashSet()
        for key in self:
            NewSet.add(key)

        for key in Iterable:
            NewSet.add(key)

        return NewSet

    ## O(n)
    def intersection(self, Iterable) -> 'HashSet':
        NewSet = HashSet()
        for key in self:
            if key in Iterable:
                NewSet.add(key)
            else:
                continue
        return NewSet

    ## O(n)
    def intersection_update(self, Iterable):
        for key in Iterable:
            if key in self:
                self.add(key)
            else:
                continue

    ## O(n)
    def difference(self, Iterable=None) -> 'HashSet':
        NewSet = HashSet()

        if Iterable is None:
            for key in self:
                NewSet.add(key)
            return NewSet
        else:
            for key in self:
                if key not in Iterable:
                    NewSet.add(key)
                else:
                    continue
            return NewSet

    ## O(n)
    def difference_update(self, Iterable=None) -> None:
        if Iterable is None:
            return
        else:
            for key in self:
                if key in Iterable:
                    self.remove(key)
            return    

    ## O(x)
    def symmetric_difference(self, Iterable):
        NewSet = HashSet()
        for key in Iterable:
            if key in self:
                continue
            else:
                NewSet.add(key)

        for key in self:
            if key in Iterable:
                continue
            else:
                NewSet.add(key)

        return NewSet
        
    ## O(x)
    def symmetric_difference_update(self, Iterable) -> None:
        keys = self._table.keys()

        for key in keys:
            if key in Iterable:
                self.remove(key)
            else:
                continue

        for key in Iterable:
            if key in keys:
                continue
            else:
                self.add(key)



if __name__ == "__main__":
    hs = HashSet()

    hs.add(2)
    hs.add(3)
    hs.add(1)
    hs.add(4)
    hs.add(5)
    hs.add(0)
    hs.add(10)

    print(hs)

    hs.symmetric_difference_update([0,1,2,4,5,6,10])
    print(hs)


    print("\n")


    
    x = set()
    x.add(2)
    x.add(3)
    x.add(1)
    x.add(4)
    x.add(5)
    x.add(0)

    print(x)

    x.symmetric_difference_update(set((0,1,2,4,5,6)))
    print(x)