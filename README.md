# Data Structures and Algorithms:

A repository for data-structures-and-algorithms implemented from scratch, literally from scratch.


Some of these data structures are meant to imitate their Python built-ins, like:

    1- "DynArray" is meant to imitate the "list" object.
    2- "HashSet" is meant to behave exactly like the "set" object.
    3- and the "HashTable" is meant for "dict".

Alos, the Algorithms are built-in to the classes, like:

    1- GraphDFS (iterative & recursive)
    2- GraphBFS (iterative & recursive)
    3- Dijkstra's
    4- A*
    5- Bellman-fords
    6- prime's
    7- krustkals
    8- and fordfulkerson
    are all built-in to the "graph" class.

    1- TreeBFS
    2- TreeDFS
    3- and BST Binary Search
    are built-in to the BT (Binary Tree) class, and so on ....


A lot of these data structures are dependent on other data structures / each other e.g.,

    1- The "HashTable / HashMap / Dictionary" data structure depends on "DynArray" in implementation given that "HashTable / HashMap / Dictionary" in its essence, is just an array where indices are the dictionary keys and array values are the dictionary values.
    2- The "Set" data structure is also implemented as "DynArray", but with keys only, no values.
    3- The "Graph" data structure depends on the "HashTable / HashMap / Dictionary" when implemented as "Adjaceny List".
    4- The "Array Based Minheap" and "Array Based Maxheap" are implemented as "DynArray".
    5- The "Iterative Tree DFS" and "Iterative Tree BFS" depend on "Queue" and "Stack".
    6- The "Trie / Prefix Tree" depends on the "HashMap / HashTable / Dictionary".
    7- and The "Binary Tree Level Order Traversal" depends on "Queue".
    and so on ....

    so for it to work with you, you need the entire repo.


Additionally, most developers think of things like:

    1- Dynamic Programing.
    2- Recursion.
    3- Backtracking.
    4- Two Pointers.
    5- Sliding Window.
    6- Brute Force.
    7- Greedy Approach.
    8- and Divide & Conquer.
   
    as algorithms, but technically speacking, they are algrithms design methods / problem solving techniques. i.e, if a problem could be solved using any of them, we design the algorithm using the right one.

    Therefore, we don't have them implemented within a certain code file, instead you will just see them used in a certain algorithm implementation, e.g,
    1- "Dijkstra's shortes path" is implement using the "Greedy Approach".
    2- "Array Based Min and Max Heap" insert and pop methods use "Recursion"
    3- "Linear Seacrh" uses "Brute Force"
    4- "BST Binary Search" is a "Greedy Approach".
    5- and "Merge Sort" is a "Divide & Conquer" approach etc.




Alos, there's a class called "Sorting_Algos" in which I implemented 10 sorting algorithms namely:

    1- Merge Sort.
    2- Bubble Sort.
    3- Selection Sort.
    4- Insertion Sort.
    5- Quick Sort.
    6- Heap Sort.
    7- Topological Sort.
    8- Bucket Sort.
    9- Radix Sort.
    10- and Counting Sort.

    Specifically these sorting algorithms because the are the ones used in LeetCode.

Finally, please keep in mind that the data structures are continuously being improved, so there might be some bugs.




## The Data Structures are as follow:

## 1- Array ✅:
    1- Static Array ✔️.
    2- Dynamic Array ✔️.

## 2- Linked List ✅:
    1- Singly Linked List ✔️.
    2- Doubly Linked List ✔️.
    3- Circly Linked List ✔️.

## 3- Stack ✅:

## 4- Queue ✅:

## 5- Hash Table / Hash Map / Dictionary ✅:

## 6- Graph ✅:
    1- Directed & Undirected Graph ✔️.
    2- Weighted & Non-weighted Graph ✔️.
    3- Cyclic & Acyclic Graph (only if Directed Graph) ✔️.

## 7- Tree ✅:
    1- Binary Search Tree ✔️.
    2- Red-Black Tree.
    3- AVL Tree.
    4- Max Heap (Array Based & Tree Based) ✔️.
    5- Min Heap (Array Based & Tree Based) ✔️.
    6- Priority Queue.
    7- Trie / Prefix-Tree ✔️:
    8- Treap.
    9- Segment Tree.
    10- Binary Index Tree / Fenwick Tree.
    11- B-Tree.
    12- Cartesian Tree.
    13- Splay Tree.
    14- KD-Tree.

## 8- Others ✅:
    1- Hash Set ✔️.
    2- Union Find / Disjoint Set.
    3- SkipList
    4- Bloom Filter
    5- Sorting Algorithms ✔️.
