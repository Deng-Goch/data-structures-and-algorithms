from dynamicarray import DynArray
from hashtable import HashTable
from hashset import HashSet

from stack import Stack
from queu import Queue

class Graph:
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

    ## 10 instance methods - 
    ## O(1)
    def add_node(self, node):
        if node not in self.adjaceny_list:
            self.adjaceny_list[node] = HashSet()
        else:
            raise ValueError('Node exist.')
    
    ## O(x)
    def remove_node(self, node):
        if node not in self.adjaceny_list:
            raise ValueError('Node does not exist.')
        else:
            for neighnors in self.adjaceny_list.values():
                neighnors.discard(node)
            del self.adjaceny_list[node]

    ## O(x)
    def add_edge(self, from_node, to_node, weight=None):
        if from_node not in self.adjaceny_list:
            raise ValueError('"From Node" does not exist.')
        elif to_node not in self.adjaceny_list:
            raise ValueError('"To Node" does not exist.')

        if self.weighted is False:
            if self.directed is False:
                self.adjaceny_list[from_node].add(to_node)
                self.adjaceny_list[to_node].add(from_node)
            else:
                self.adjaceny_list[from_node].add(to_node)
        else:
            if weight is None or type(float(weight)) != float:
                raise TypeError("Enter a weight of type int/float.")
            
            if self.directed is False:
                self.adjaceny_list[to_node].add((from_node,weight))
                self.adjaceny_list[from_node].add((to_node,weight))
            else:
                self.adjaceny_list[from_node].add((to_node,weight))

    ## O(x)
    def remove_edge(self, from_node, to_node):
        if from_node in self.adjaceny_list:
            if to_node in self.adjaceny_list[from_node]:
                if self.directed is False:
                    self.adjaceny_list[from_node].remove(to_node)
                    self.adjaceny_list[to_node].remove(from_node)
                else:
                    self.adjaceny_list[from_node].remove(to_node)
            else:
                raise ValueError('Edge does not exist.')
        else:
            raise ValueError("From node does not exist.")

    ## O(1)*
    def get_neighbors(self, node):
        if node not in self.adjaceny_list:
            raise ValueError("Node does not exist.")
        else:
            return self.adjaceny_list.get(node)

    ## O(n)
    def node_exist(self, node):
        if node in self.adjaceny_list:
            return True
        else:
            return False

    ## O(1)*
    def edge_exist(self, from_node, to_node):
        if from_node in self.adjaceny_list:
            if to_node in self.adjaceny_list[from_node]:
                return True
            else:
                return False
        else:
            return False

    ## O(n)
    def get_nodes(self):
        return self.adjaceny_list.keys()

    ## O(n)
    def bfs(self, start_node):
        if start_node not in self.adjaceny_list:
            raise ValueError("Start Node does not exist.")

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
    
    ## O(n)
    def dfs(self, start_node):
        if start_node not in self.adjaceny_list:
            raise ValueError("Start Node does not exist.")
        
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

    ## O()
    def dijkstra(self, source_node):
        pass

    ## O()
    def a_star(self, source_node):
        pass

    ## O()
    def bellman_fords(self, source_node):
        pass

    ## O()
    def primes(self):
        pass

    ## O()
    def krustkal(self):
        pass

    ## O()
    def ford_fulkerson(self):
        pass




if __name__ == "__main__":
    graph = Graph(directed=False, weighted=False)
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
    graph.add_edge("B", "C")

    graph.add_edge('D', 'E', 4)
    graph.add_edge('D', 'F', 8)
    graph.add_edge('D', 'C', 9)

    graph.add_edge("E", "A", 2)
    graph.add_edge('E', 'B', 5)
    graph.add_edge('E', 'C', 11)

    graph.add_edge('F', 'H', 8.6)
    graph.add_edge("G", "E", 6)

    
    print(graph)

    graph.remove_node("A")
    print(graph)

    print(graph.dfs('B'))
    print(graph.bfs("B"))

    
    # print("\n")

    # print(graph.adjaceny_list)