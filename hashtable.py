from dynamicarray import DynArray

class HashTable:
    ## 8 Magic Methods
    ## O(1)
    def __init__(self):
        self.size = 0
        self.capacity = 8
        self.buckets = self._Make_Table_(self.capacity)
        self.last = DynArray()

    ## O(n)
    def __repr__(self):
        if self.size == 0:
            return "{}"
        else:
            ends = len(self.items())
            dic = str("{")
            for k, v in self.items():
                dic += f"'{k}': {v}"
                ends -= int(1)
                if ends >= 1:
                    dic += str(", ")
                else:
                    dic += str("}")
            return dic

    # O(1)
    def __len__(self):
        return self.size

    ## O(1)*
    def __contains__(self, key):
        index = self._Hash_Func_(key)
        bucket = self.buckets[index]

        for k, v in bucket:
            if k == key:
                return True
        return False

    ## O(1)*
    def __getitem__(self, key):
        return self.get(key)

    ## O(1)*
    def __setitem__(self, key, value):
        return self.update(key, value)

    ## O(1)*
    def __delitem__(self, key):
        return self.pop(key)
    
    ## O(n)
    def __iter__(self):
        items = self.items()

        for k, v in items:
            yield f"{k}: {v}"


    ## 4 inner helper functions
    ## O(len(key))
    def _Hash_Func_(self, key):
        keyCasted = str(key)
        hashRes = 0
        for char in keyCasted:
            hashRes = (((hashRes * 31) + ord(char)) % self.capacity)
        return hashRes

    ## O(n)
    def _Make_Table_(self, capacity):
        table = DynArray(capacity)
        for _ in range(capacity):
            table.append(DynArray())
        return table

    ## O(1)*
    def _NewInsert_(self, ky, vl, tb):
        index = self._Hash_Func_(ky)
        bucket = tb[index]

        for i, (k, v) in enumerate(bucket):
            if k == ky:
                bucket[i] = (ky, vl)
                break
        else:
            bucket.append((ky, vl))
            self.size += 1
        return tb

    ## O(n)
    def _MoveToNewTable_(self):
        items = self.items()
        self.capacity *= 2
        self.size = 0
        NewTable = self._Make_Table_(self.capacity)
        self.buckets = NewTable

        for (ky, vl) in items:
            self._NewInsert_(ky, vl, self.buckets)
        return self.buckets


    ## 11 methods
    ## O(1)*
    def update(self, key, value):
        if ((self.size / self.capacity) * 100) <= 60:
            self._NewInsert_(key, value, self.buckets)
        else:
            self._MoveToNewTable_()
            self._NewInsert_(key, value, self.buckets)
        self.last.append(key)

    ## O(1)*
    def pop(self, key):
        index = self._Hash_Func_(key)
        bucket = self.buckets[index]

        for i, (k, v) in enumerate(bucket):
            if k == key:
                bucket.remove(i)
                self.size -= 1
                break
        else:
            raise KeyError('Key Not Found')

    ## O(1)*
    def get(self, key):
        index = self._Hash_Func_(key)
        bucket = self.buckets[index]

        for k, v in bucket:
            if k == key:
                return v
        else:
            raise KeyError('Key Not Found')

    ## O(n)
    def keys(self):
        keys = DynArray(self.size)
        for bucket in self.buckets:
            for k, _ in bucket:
                keys.append(k)
        return keys
    
    ## O(n)
    def values(self):
        vals = DynArray(self.size)
        for bucket in self.buckets:
            for _, v in bucket:
                vals.append(v)
        return vals

    ## O(n)
    def items(self):
        keyVals = DynArray(self.size)
        for bucket in self.buckets:
            for k, v in bucket:
                keyVals.append((k, v))
        return keyVals

    ## O(n)
    def clear(self):
        for i in range(self.capacity):
            self.buckets.pop()
        self.size = 0

    ## O(n)
    def copy(self):
        NewHashTable = HashTable()

        for k, v in self.items():
            NewHashTable.update(k, v)
            
        return NewHashTable

    ## O(1)
    def popitem(self):
        if len(self.last) == 0:
            raise IndexError("Empty Hashtable")
        else:
            end = self.last[-1]
            HashTable.pop(self, self.last[-1])
            self.last.pop()
            return end

    ## O(1)
    def setdefault(self, key, val_to_give=None):
        if key in self.keys():
            return self.get(key)
        else:
            self.update(key, val_to_give)

    ## O(n)
    def fromkeys(self, array, default_val=None):
        NewHashTable = HashTable()
        NewTable = self._Make_Table_(len(array))

        for el in array:
            NewHashTable._NewInsert_(el, default_val, NewTable)
        NewHashTable.buckets = NewTable
        return NewHashTable



if __name__ == "__main__":
    hashmap = HashTable()
    # print(hashmap.buckets)

    hashmap.update("Deng", "DG")
    hashmap.update("Goch", "GH")
    hashmap.update("Yassin", "YN")
    hashmap.update("Monydhot", "MT")
    hashmap.update("Yor", "YR")
    hashmap.update("Bol", "BL")
    # hashmap.update("Monywiir", "MR")
    # hashmap.update("Anyang", "AG")
    # hashmap.update("Kuac", "KC")
    # hashmap.update("John", "JN")
    # hashmap.update("David", "DD")
    # hashmap.update("Kol", "KL")
    # hashmap.update("Dau", "DU")
    # hashmap.update("Ayuel", "AL")
    # hashmap.update("Musa", "MA")
    # hashmap.update("Brown", "BN")
    # hashmap.update("Chan", "CN")
    # hashmap.update("Nyok", "NK")
    # hashmap.update("Kunebuny", "KY")
    # hashmap.update("Salva", "AA")
    # hashmap.update("ArialDit", "AD")

    # print(hashmap.setdefault("Yor"))
    # print(hashmap)
    # hashmap.setdefault("ArialBek", "Nyan")
    # print(hashmap)

    # print("\n")

    # print(hashmap.items())

    # print("\n")

    # print(hashmap.keys())

    print(hashmap.size)

    print("\n")

    print(hashmap.values())

    copied = hashmap.copy()

    print(copied.values())

    print(hashmap.keys())

    print(copied.keys())

    hashmap.popitem()
    hashmap.popitem()

    print(hashmap.size)
    print(copied.size)

    print("\n")

    print(hashmap.keys())

    print(copied.keys())