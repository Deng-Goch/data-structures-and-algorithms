from dynamicarray import DynArray
from queu import Queue


class Array_Based_Min_Heap:

    ## 3 magic methods
    ## O(1)
    def __init__(self):
        self.heap = DynArray()

    ## O(1)
    def __len__(self):
        return len(self.heap)

    ## O(n)
    def __str__(self):
        return str(self.heap)


    ## 5 inner / helper methods
    ## (log2 n)
    def _sift_up_(self, index):
        pass

    ## O(log2 n)
    def _sift_down_(self, index):
        ind = 0
        if self._left_(ind) < self._right_(ind):
            self.heap[ind], self._left_(ind) = self._left_(ind), self.heap[ind]
        else:
            pass


    ## O(1)
    def _left_(self, index):
        if index >= len(self.heap):
            raise IndexError('Index Out of Range.')
        else:
            left = ((index * 2) + 1)
            if not self.heap[left]:
                raise ValueError('No left child.')
            else:
                return self.heap[left]

    ## O(1)
    def _right_(self, index):
        if index >= len(self.heap):
            raise IndexError('Index Out of Range.')
        else:
            right = ((index * 2) + 2)
            if not self.heap[right]:
                raise ValueError('No right child.')
            else:
                return self.heap[right]

    ## O(1)
    def _parent_(self, index):
        if index == 0:
            raise IndexError('No parent.')
        else:
            parent = ((index - 1) // 2)
            if not self.heap[parent]:
                raise ValueError('No parent.')
            else:
                return self.heap[parent]


    ## 5 methods
    ## O(log2 n)
    def insert(self, key, value):
        self.heap.append((key, value))
        self._sift_up_(len(self.heap)-1)

    ## O(log2 n)
    def del_min(self):
        if len(self.heap) == 0:
            raise IndexError('Deleting from an empty heap.')
        elif len(self.heap) == 1:
            deleted = self.heap[0]
            self.heap.pop()
            return deleted
        else:
            deleted = self.heap[0]
            self.heap[0] = self.heap[len(self.heap)-1]
            self.heap.pop()
            self._sift_down_(self.heap[0])
            return deleted

    ## O(log2 n)
    def heapify(self, elements):
        pass

    ## O(log2 n)
    def meld(self, elements):
        pass

    ## O(1)
    def PeekMin(self):
        if len(self.heap) == 0:
            raise IndexError('Peeking from an empty MinHeap.')
        else:
            return self.heap[0]






# class Tree_Based_Min_Heap:
#     class HeapNode:
#         ## O(1)
#         def __init__(self, key, value):
#             self.key = key
#             self.value = value
#             self.left = None
#             self.right = None
#             self.parent = None

#         ## O(1)
#         def __str__(self):
#             return f"(K: {self.key}, V: {self.value})"


#     ## 2 magic methods
#     ## O(1)
#     def __init__(self):
#         self.root = None

#     ## O(n)
#     def __repr__(self):
#         pass


#     ## 4 internal / helper methods
#     ## O(n)
#     ## Left, Node, Right
#     def _pre_order(self, node):
#         if node is not None:
#             self._pre_order(node.left)
#             self._pre_order(node.right)
#             print(f'({node.key}, {node.value})')

#     ## O(n)
#     ## Node, Left, Right
#     def _in_order_(self, node):
#         if node is not None:
#             self._pre_order(node.left)
#             print(f'({node.key}, {node.value})')
#             self._pre_order(node.right)

#     ## O(n)
#     ## Left, Right, Node
#     def _post_order_(self, node):
#         if node is not None:
#             print(f'({node.key}, {node.value})')
#             self._pre_order(node.left)
#             self._pre_order(node.right)

#     ## O(n)
#     ## Node, Left, Right - Level by level
#     def _level_order_(self, node):
#         pass


#     ## 4 instance methods
#     ## O(log2 n)
#     def insert(self, key, value):

#         if self.root is None:
#             self.root = self.HeapNode(key, value)
#         else:
#             CurrNode = self.root
#             while True:
#                 if key < CurrNode.key:
#                     pass
#                 elif key > CurrNode.key:
#                     pass
#                 else:
#                     pass

#     ## O(log2 n)
#     def del_min(self):
#         if self.root is None:
#             raise ValueError('Empty Heap')
#         else:
#             deleted = self.root
#             CurrNode = self.root
#             while CurrNode:
#                 if CurrNode.left:
#                     CurrNode.key = CurrNode.left.key
#                     CurrNode.value = CurrNode.left.value
#                     CurrNode = CurrNode.left
#                 elif CurrNode.left:
#                     pass
#                 else:
#                     CurrNode.key = None
#                     CurrNode.value = None
#             return deleted

#     ## O(1)
#     def peakMin(self):
#         if self.root is None:
#             raise ValueError('Empty Heap')
#         else:
#             return self.root

#     ## O(log2 n)
#     def travers(self, order:str):
#         if order.lower() == 'preorder':
#             return self._post_order_(self.root)
#         elif order.lower() == 'inorder':
#             return self._in_order_(self.root)
#         elif order.lower() == 'postorder':
#             return self._post_order_(self.root)
#         elif order.lower() == 'levelorder':
#             return self._level_order_(self.root)
#         else:
#             raise ValueError('Unknown order.')


    
# if __name__ == "__main__":
#     pass