from hashtable import HashTable
from hashset import HashSet
from dynamicarray import DynArray

from stack import Stack
from queu import Queue



class Adjaceny_List_Based_Graph:
    ## 2 maigic methods
    ## O(1)
    def __init__(self, directed:bool=True, weighted:bool=False, cyclic:bool=True, Node_Self_Cyclic:bool=False):

        """
        Input:
        
        Directed:bool - default=True - Tells if edges are two ways or one way.
        
        Weighted:bool - default=False - Tells if edges carry a weight or not "type(weight) is int/float".
        
        Cyclic:bool - default=False - Tells if a directed graph has cycles i.e, if a node can connect to a certain node and that node connects back to it. Please node that this is only applicable to directed graph.
        
        NodeSelfCycle:bool - default=False - Tells if a directed graph nodes can point to themselves or not. Please node that this is only applicable to directed graph.

        
        Process: Creates an Adjaceny LIst.

        Output: An Adjaceny_List_Based_Graph object.

        Error: None
        """

        self.directed = directed
        self.weighted = weighted
        self.cyclic = cyclic                        ## Only applicable if directed
        self.Node_Self_Cyclic = Node_Self_Cyclic    ## Only applicable if directed
        self.adjaceny_list = HashTable()


    ## O(n)
    def __repr__(self):
        graph = ""
        for node, neighbors in self.adjaceny_list.items():
            graph += f"{node} -> {neighbors}\n"
        return graph


    ## 16 instance methods - 
    ## O(1)
    def add_node(self, node) -> None:

        """
        Input: a node of any type.

        Process: adds a node to the graph but without edges.

        Output: None.

        Error: If no input, it throws a TypeError: Adjaceny_List_Based_Graph.add_node() missing 1 required positional argument: 'node'
        """

        if node not in self.adjaceny_list:
            self.adjaceny_list[node] = HashSet()
        else:
            raise ValueError('Node exist.')

    
    ## O(n)
    def remove_node(self, node) -> None:

        """
        Input: a node of any type.

        Process: Removes the given node from the graph along with its edges.

        Output: None.

        Error: It throws a "ValueError: Node does not exist." if node not in the Graph.
        """

        if node not in self.adjaceny_list:
            raise ValueError('Node does not exist.')
        else:
            if self.weighted:
                for neighbors in self.adjaceny_list.values():
                    for value in neighbors:
                        if value[0] == node:
                            neighbors.discard(value)
                del self.adjaceny_list[node]
            else:
                for neighbors in self.adjaceny_list.values():
                    neighbors.discard(node)
                del self.adjaceny_list[node]


    ## O(1)
    def add_edge(self, from_node, to_node, weight=None) -> None:

        """
        Input: 

        Process: 

        Output: 

        Error: 
        """

        if from_node == to_node:
            if self.Node_Self_Cyclic is False:
                raise AssertionError("Can't have node self loop/cycle.")
        
        if from_node not in self.adjaceny_list:
            raise ValueError('"From Node" does not exist.')
        elif to_node not in self.adjaceny_list:
            raise ValueError('"To Node" does not exist.')
        else:
            if self.weighted is False:
                if self.directed is False:
                    self.adjaceny_list[from_node].add(to_node)
                    self.adjaceny_list[to_node].add(from_node)
                else:
                    if self.cyclic is True:
                        self.adjaceny_list[from_node].add(to_node)
                    else:
                        if from_node in self.adjaceny_list[to_node]:
                            raise AssertionError("Can't have cycles.")
                        else:
                            self.adjaceny_list[from_node].add(to_node)
            else:
                if weight is None or type(float(weight)) != float:
                    raise TypeError("Enter a weight of type int/float.")
                else:
                    if self.directed is False:
                        self.adjaceny_list[to_node].add((from_node,weight))
                        self.adjaceny_list[from_node].add((to_node,weight))
                    else:
                        if self.cyclic is True:
                            self.adjaceny_list[from_node].add(to_node)
                        else:
                            if from_node in self.adjaceny_list[to_node]:
                                raise AssertionError("Can't have cycles.")
                            else:
                                self.adjaceny_list[from_node].add(to_node)


    ## O(1)
    def remove_edge(self, from_node, to_node) -> None:

        """
        Input: 

        Process: 

        Output: 

        Error: 
        """

        if from_node in self.adjaceny_list:
            if to_node in self.adjaceny_list[from_node]:
                if self.directed is False:
                    self.adjaceny_list[from_node].remove(to_node)
                    self.adjaceny_list[to_node].remove(from_node)
                else:
                    self.adjaceny_list[from_node].remove(to_node)
            else:
                raise ValueError('"To Node" does not exist.')
        else:
            raise ValueError('"From Node" does not exist."')


    ## O(1)*
    def get_neighbors(self, node) -> HashSet:

        """
        Input: 

        Process: 

        Output: 

        Error: 
        """

        if node not in self.adjaceny_list:
            raise ValueError("Node does not exist.")
        else:
            return self.adjaceny_list.get(node)


    ## O(1)*
    def node_exist(self, node) -> bool:

        """
        Input: graph node.

        Process: Checks if the givem node is in the graph.

        Output: Either True or False.

        Error: Throws a "TypeError: Adjaceny_List_Based_Graph.node_exist() missing 1 required positional argument: 'node'" if no node entered.
        """

        if node in self.adjaceny_list:
            return True
        else:
            return False


    ## O(1)*
    def edge_exist(self, from_node, to_node) -> bool:

        """
        Input: 

        Process: Checks if there's an edge between "From Node" to "To Node".

        Output: Either True or False.

        Error: 
        """

        if from_node in self.adjaceny_list:
            if to_node in self.adjaceny_list[from_node]:
                return True
            else:
                return False
        else:
            return False


    ## O(n)
    def get_nodes(self) -> DynArray:

        """
        Input: 

        Process: Get all the nodes that are in this graph, including the isolated nodes.

        Output: An array obects whose elements are all the nodes in this geraph object.

        Error: 
        """

        return self.adjaceny_list.keys()


    ## O(x)
    def iterative_bfs(self, start_node) -> DynArray:

        """
        Input: A node to start from.

        Process: Get all the nodes that aren't isolated/disconnected from the graph.

        Output: An array object whoes elements are graph nodes in a BFS traversal given the start node.

        Error: If the entered node is not on the graph, it throws a "ValueError('"Start Node" does not exist.')"
        """

        if start_node not in self.adjaceny_list:
            raise ValueError("Start Node does not exist.")
        else:
            queu = Queue()
            queu.Push(start_node)
            seen = HashSet()
            order = DynArray()

            while queu:
                node = queu.PopLeft()
                if node not in seen:
                    seen.add(node)
                    order.append(node)

                    neighbors = self.get_neighbors(node)

                    if self.weighted:
                        for neighbor in sorted(neighbors, reverse=True):
                            if neighbor[0] not in seen:
                                queu.Push(neighbor[0])
                    else:
                        for neighbor in sorted(neighbors, reverse=True):
                            if neighbor not in seen:
                                queu.Push(neighbor)
            return order

    
    ## O(x)
    def iterative_dfs(self, start_node) -> DynArray:

        """
        Input: A node to start from.

        Process: Get all the nodes that aren't isolated/disconnected from the graph.

        Output: An array object whoes elements are graph nodes in a DFS traversal given the start node.

        Error: If the entered node is not on the graph, it throws a "ValueError('"Start Node" does not exist.')"
        """

        if start_node not in self.adjaceny_list:
            raise ValueError('"Start Node" does not exist.')
        else:
            stack = Stack()
            stack.push(start_node)
            seen = HashSet()
            order = DynArray()

            while stack:
                node = stack.pop()
                if node not in seen:
                    seen.add(node)
                    order.append(node)

                    neighbors = self.get_neighbors(node)

                    if self.weighted:
                        for neighbor in sorted(neighbors, reverse=True):
                            if neighbor[0] not in seen:
                                stack.push(neighbor[0])
                    else:
                        for neighbor in sorted(neighbors, reverse=True):
                            if neighbor not in seen:
                                stack.push(neighbor)
            return order


    ## O(x)
    def recursive_bfs(self, start_node) -> DynArray:

        """
        Input: 

        Process: 

        Output: 

        Error: 
        """

        pass

    
    ## O(x)
    def recursive_dfs(self, start_node) -> DynArray:

        """
        Input: 

        Process: 

        Output: 

        Error: 
        """

        pass


    ## O(x)
    def dijkstra(self, source_node):

        """
        Input: 

        Process: 

        Output: 

        Error: 
        """

        pass


    ## O(x)
    def a_star(self, source_node):

        """
        Input: 

        Process: 

        Output: 

        Error: 
        """

        pass


    ## O(x)
    def bellman_fords(self, source_node):

        """
        Input: 

        Process: 

        Output: 

        Error: 
        """

        pass


    ## O(x)
    def primes(self):

        """
        Input: 

        Process: 

        Output: 

        Error: 
        """

        pass


    ## O(x)
    def krustkal(self):

        """
        Input: 

        Process: 

        Output: 

        Error: 
        """

        pass


    ## O(x)
    def ford_fulkerson(self):

        """
        Input: 

        Process: 

        Output: 

        Error: 
        """

        pass




if __name__ == "__main__":
    graph = Adjaceny_List_Based_Graph(directed=True, weighted=False, cyclic=False, Node_Self_Cyclic=False)

    graph.add_node("A")
    graph.add_node("B")
    graph.add_node("C")
    graph.add_node("D")

    graph.add_edge("A", "B")
    graph.add_edge("B", "C")

    graph.add_edge("C", "D")

    print(graph)

    graph.remove_node('D')