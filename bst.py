from queu import Queue
from dynamicarray import DynArray

class BST:
    class TreeNode:
        def __init__(self, key):
            self.key = key
            self.value = None
            self.left = None
            self.right = None
            self.parent = None
    
        def __repr__(self):
            return f"({self.key}, {self.value})"

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

    def __iter__(self):
        yield from self._in_order(self.root)

    def __repr__(self):
        return str(list(self._in_order(self.root)))
    

    ## main operations - 4
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


    def delete(self, val):
        node = self.search(val)
        if node is None:
            raise ValueError('Node with this key does not exist!')
        else:
            self._delete(node)


    def travers(self, order):
        if order == "inorder":
            yield from self._in_order(self.root)
        elif order == "postorder":
            yield from self._post_order(self.root)
        elif order == "inorder":
            yield from self._post_order(self.root)
        elif order == "levelorder":
            yield from self._level_order(self.root)
        else:
            raise ValueError("Unknow order.")


    ## internal functions - 7
    def _delete(self, node):
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
            successor = self._suceessor(node)
            node.key = successor.key
            node.value = successor.value

            self.delete(successor)


    def _pre_order(self, node):
        if node is not None:
            yield (node.key, node.value)
            yield from self._pre_order(node.left)
            yield from self._pre_order(node.right)

    def _in_order(self, node):
        if node is not None:
            yield from self._in_order(node.left)
            yield (node.key, node.value)
            yield from self._in_order(node.right)

    def _post_order(self, node):
        if node is not None:
            yield from self._pre_order(node.left)
            yield from self._pre_order(node.right)
            yield (node.key, node.value)


    def _level_order(self, node):
        pass


    def _suceessor(self, node):
        if node is None:
            raise ValueError("Can't find the successor of a None node.")
        
        if node.right is None:
            return None
        else:
            currNode = node.right
            while currNode.left is not None:
                currNode = currNode.left
            return currNode


    def _predocessor(self, node):
        if node is None:
            raise ValueError("Can't find the predocessor of a None node.")
        
        if node.left is None:
            return None
        else:
            currNode = node.left
            while currNode.right is not None:
                currNode = currNode.right
            return currNode



if __name__ == "__main__":
    bst = BST()
    bst.insert(8, 23)
    bst.insert(3, 50)
    bst.insert(27, "xyz")

    print(bst)
    print(bst.travers("levelorder"))