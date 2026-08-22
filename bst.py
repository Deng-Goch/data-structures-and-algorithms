from dynamicarray import DynArray
from queu import Queue

class BST:
    class TreeNode:
        def __init__(self, key):
            self.key = key
            self.value = None
            self.left = None
            self.right = None
            self.parent = None
    
        def __repr__(self):
            return f"(Key: {self.key}, Value: {self.value})"

    ## magic methods - 4
    ## O(1)
    def __init__(self):
        self.root = None

    ## O(log2 n)
    def __contains__(self, key):
        currNode = self.root
        while currNode is not None:
            if key < currNode.key:
                currNode = currNode.left
            elif key > currNode.key:
                currNode = currNode.right
            else:
                return True
        return False

    ## O(n)
    def __iter__(self):
        yield from self._in_order_(self.root)

    ## O(n)
    def __repr__(self):
        rep = DynArray()
        for node in self:
            rep.append(node)

        return str(rep)


    ## Internal/Helper methods - 6
    def _pre_order_(self, node):
        if node is not None:
            print((node.key, node.value))
            self._pre_order_(node.left)
            self._pre_order_(node.right)

    def _in_order_(self, node):
        if node is not None:
            self._in_order_(node.left)
            print((node.key, node.value))
            self._in_order_(node.right)

    def _post_order_(self, node):
        if node is not None:
            self._pre_order_(node.left)
            self._pre_order_(node.right)
            print((node.key, node.value))

    def _level_order(self, node):
        if node is None:
            return None
        else:
            # return node
            queue = Queue(node)
            order = DynArray()

            while queue:
                nod = (queue.left.val)

                order.append((nod.key))

                if nod.left is not None:
                    queue.Push(nod.left)
                if nod.right is not None:
                    queue.Push(nod.right)

                queue.PopLeft()

            return order
        

    def _suceessor_(self, node):
        if node is None:
            raise ValueError("Can't find the successor of a None node.")
        
        if node.right is None:
            return None
        else:
            currNode = node.right
            while currNode.left is not None:
                currNode = currNode.left
            return currNode

    def _predocessor_(self, node):
        if node is None:
            raise ValueError("Can't find the predocessor of a None node.")
        
        if node.left is None:
            return None
        else:
            currNode = node.left
            while currNode.right is not None:
                currNode = currNode.right
            return currNode


    ## main operations - 4
    ## O(log2 n)
    def insert(self, key, val):
        if self.root is None:
            self.root = BST.TreeNode(key)
            self.root.value = val
        else:
            currNode = self.root
            while True:
                if key < currNode.key:
                    if currNode.left is None:
                        currNode.left = BST.TreeNode(key)
                        currNode.left.value = val
                        currNode.left.parent = currNode
                        break
                    else:
                        currNode = currNode.left

                elif key > currNode.key:
                    if currNode.right is None:
                        currNode.right = BST.TreeNode(key)
                        currNode.right.value = val
                        currNode.right.parent = currNode
                        break
                    else:
                        currNode = currNode.right
                else:
                    currNode.value = val
                    break

    ## O(log2 n)
    def search(self, key):
        currNode = self.root

        while True:
            if currNode is None or currNode.key == key:
                return currNode
            elif currNode.key < key:
                if currNode.right == None:
                    return None
                else:
                    currNode = currNode.right
            else:
                if currNode.left == None:
                    return None
                else:
                    currNode = currNode.left

    ## O(log2 n)
    def delete(self, key):
        node = self.search(key)
        if node is None:
            raise ValueError('Node with this key does not exist!')
        else:
            #CASE 1: if it is a leaf node
            if node.left is None and node.right is None:
                if node.parent is None:
                    self.root = None
                else:
                    if node.parent.right == node:
                        node.parent.right = None
                    else:
                        node.parent.left = None
                    node.parent = None

            #CASE 2: if it has 1 child node
            elif node.right is None or node.left is None:

                ## assiging the child node, either left or right
                if node.left is None:
                    childNode = node.right
                else:
                    childNode = node.left
                
                # if it is the root node
                if node.parent is None:
                    childNode.parent = None
                    self.root.left = None
                    self.root.right = None
                    self.root = childNode
                else:

                # if it is not the root node
                    if node.parent.right == node:
                        node.parent.right = childNode
                    else:
                        node.parent.left = childNode
                    childNode.parent = node.parent
                    node.parent = None
                    node.left = None
                    node.right = None

            #CASE 3: it has 2 child node
            else:
                successor = self._suceessor_(node)
                node.key = successor.key
                node.value = successor.value

                self.delete(successor)

    ## O(n)
    def travers(self, order:str):
        if order.lower() == "preorder":
            return self._pre_order_(self.root)
        elif order.lower() == "inorder":
            return self._in_order_(self.root)
        elif order.lower() == "postorder":
            return self._post_order_(self.root)
        elif order.lower() == "levelorder":
            return self._level_order(self.root)
        else:
            raise ValueError("Unknow order.")


if __name__ == "__main__":
    bst = BST()
    bst.insert(53, 53)
    bst.insert(21, 21)
    bst.insert(13, 13)
    bst.insert(4, 4)
    bst.insert(18, 18)
    bst.insert(47, 47)
    bst.insert(32, 32)
    bst.insert(49, 49)
    bst.insert(67, 67)
    bst.insert(59, 59)
    bst.insert(58, 58)
    bst.insert(63, 63)
    bst.insert(74, 74)
    bst.insert(70, 70)
    bst.insert(77, 77)

    # print(bst)

    # bst.delete('g')
    
    # bst.travers('preordeR')

    # print("\n")

    # bst.travers('InORDEr')

    # print("\n")

    # bst.travers('postorder')

    # print("\n")

    print(bst.travers('leveLordeR'))
