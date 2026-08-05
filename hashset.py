from hashtable import HashTable

class HashSet:
    ## magic methods - 5
    def __init__(self):
        self._table = HashTable()

    ## O(n)
    def __iter__(self):
        for i in range(self._table.size):
            yield self._table.keys()[i]

    ## O(n)
    def __repr__(self):
        rep = str("")
        for i in range(self._table.size):
            rep += str(self._table.keys()[i])

            if i != (self._table.size - 1):
                rep += ", "

        return "{" + rep + "}"

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

     ## O(1)
    def discard(self, element:object) -> None:
        if element in self._table:
            self._table.pop(element)
        else:
            return

    ## O(x)
    def clear(self) -> None:
        pass
    
    ## O(x)
    def copy(self):
        pass

    ## O(x)
    def difference(self):
        pass

    ## O(x)
    def difference_update(self):
        pass

    ## O(x)
    def intersection(self):
        pass

    ## O(x)
    def intersection_update(self):
        pass

    ## O(x)
    def isdisjoint(self):
        pass

    ## O(x)
    def issubset(self, sec_set):
        pass

    ## O(x)
    def issuperset(self, sec_set):
        pass

    ## O(x)
    def pop(self):
        pass

    ## O(x)
    def remove(self, element:object) -> None:
        pass
    
    ## O(x)
    def symmetric_difference(self, sec_set):
        pass

    ## O(x)
    def symmetric_difference_update(self, s) -> None:
        pass

    ## O(x)
    def union(self, sec_set):
        pass

    ## O(x)
    def update(self, sec_set):
        pass


if __name__ == "__main__":
    hs = HashSet()
    # hs.add(7)
    # hs.add(1)
    # hs.add(2)
    # hs.add(2)
    
    # print(hs)
    # # print(len(hs))

    # hs.discard(2)

    # for i in hs:
    #     print(i)

    # print("\n")

    s = set()
    s.add(1)
    s.add(7)
    s.add(2)
    s.add(2)
    s.add(7)
    print(s)
    print(len(s))

    s.discard(2)
    print(s)

    for i in s:
        print(i)