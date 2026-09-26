from hashtable import HashTable
from hashset import HashSet
from dynamicarray import DynArray

from stack import Stack
from queu import Queue



class Adjaceny_List_Based_Graph:
    ## 2 maigic methods
    ## O(1)
    def __init__(self, directed=True, weighted=False):
        self.directed = directed
        self.weighted = weighted
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
        if node not in self.adjaceny_list:
            self.adjaceny_list[node] = HashSet()
        else:
            raise ValueError('Node exist.')

    
    ## O(n)
    def remove_node(self, node) -> None:
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
                    self.adjaceny_list[from_node].add(to_node)
            else:
                if weight is None or type(float(weight)) != float:
                    raise TypeError("Enter a weight of type int/float.")
                else:
                    if self.directed is False:
                        self.adjaceny_list[to_node].add((from_node,weight))
                        self.adjaceny_list[from_node].add((to_node,weight))
                    else:
                        self.adjaceny_list[from_node].add((to_node,weight))


    ## O(1)
    def remove_edge(self, from_node, to_node) -> None:
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
        if node not in self.adjaceny_list:
            raise ValueError("Node does not exist.")
        else:
            return self.adjaceny_list.get(node)


    ## O(1)*
    def node_exist(self, node) -> bool:
        if node in self.adjaceny_list:
            return True
        else:
            return False


    ## O(1)*
    def edge_exist(self, from_node, to_node) -> bool:
        if from_node in self.adjaceny_list:
            if to_node in self.adjaceny_list[from_node]:
                return True
            else:
                return False
        else:
            return False


    ## O(n)
    def get_nodes(self) -> DynArray:
        return self.adjaceny_list.keys()


    ## O(x)
    def iterative_bfs(self, start_node) -> DynArray:
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
        if start_node not in self.adjaceny_list:
            raise ValueError("Start Node does not exist.")
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
        pass

    
    ## O(x)
    def recursive_dfs(self, start_node) -> DynArray:
        pass


    ## O(x)
    def dijkstra(self, source_node):
        pass


    ## O(x)
    def a_star(self, source_node):
        pass


    ## O(x)
    def bellman_fords(self, source_node):
        pass


    ## O(x)
    def primes(self):
        pass


    ## O(x)
    def krustkal(self):
        pass


    ## O(x)
    def ford_fulkerson(self):
        pass




if __name__ == "__main__":
    graph = Adjaceny_List_Based_Graph(directed=False, weighted=True)
    graph.add_node('A')
    graph.add_node('B')
    graph.add_node('C')
    graph.add_node('D')
    graph.add_node('E')
    graph.add_node('F')
    graph.add_node("G")
    graph.add_node('H')

    print(graph)

    # graph.remove_node("A")

    # print(graph)

    graph.add_edge("A", "B", 7)
    graph.add_edge('A', 'C', 3)
    graph.add_edge('A', 'E', 10)

    graph.add_edge('B', 'A', 6)
    graph.add_edge("B", "C", 4)

    graph.add_edge('D', 'E', 4)
    graph.add_edge('D', 'F', 8)
    graph.add_edge('D', 'C', 9)

    graph.add_edge("E", "A", 2)
    graph.add_edge('E', 'B', 5)
    graph.add_edge('E', 'C', 11)

    graph.add_edge('F', 'H', 8.6)
    graph.add_edge("G", "E", 6)

    
    print(graph)

    # print(graph.adjaceny_list.values())

    graph.remove_node("A")

    print("\n")

    print(graph)

    print(graph.iterative_bfs("E"))
    print(graph.iterative_dfs("B"))