""" 
QUESTION 1
Topological sorting can be implemented using an algorithm seen in
class. Which algorithm? Why? 

The topological sorting can be implemented using the Depth First Search (DFS) algorithm. 
DFS recursively visits each node, starting from either the far left or far right node, and then moves to the next node. 
This is because we need to visit all the nodes in the graph and order them in a linear sequence such that for every 
directed edge from node 'a' to node 'b', 'a' comes before 'b' in the ordering.


Source:
-Lectures notes
-GeeksforGeeks. (2013, May 12). Topological Sorting. Retrieved March 29, 2024, 
from GeeksforGeeks website: https://www.geeksforgeeks.org/topological-sorting/
"""

class Node:
    def __init__(self, data):
        self.data = data

class Graph:
    def __init__(self):
        self.adjacency_list = {}
    
    def addNode(self, node):
        self.adjacency_list[node] = []
        return node
    
    def removeNode(self, node):
        del self.adjacency_list[node]
        for adjacentNodes in self.adjacency_list.values():
            if node in adjacentNodes:
                adjacentNodes.remove(node)
    
    def addEdge(self, n1, n2, weight):
        # Check if both nodes exist in the graph
        if n1 not in self.adjacency_list or n2 not in self.adjacency_list:
            raise ValueError("One of the nodes does not exist in the graph. Try again")
        self.adjacency_list[n1].append((n2, weight))
    
    def removeEdge(self, n1, n2):
        if n1 not in self.adjacency_list or n2 not in self.adjacency_list:
            raise ValueError("One of the nodes does not exist in the graph. Try again")
        self.adjacency_list[n1] = [edge for edge in self.adjacency_list[n1] if edge[0] != n2]
    
    def isDag(self):
        visited = set()
        stack = set()
        
        #iterates through the neighbors of the node
        #used chatgpt
        def depth_first_search(node):
            visited.add(node)
            stack.add(node)
            for neighbor, _ in self.adjacency_list.get(node, []):
                if neighbor in stack:
                    return False  # Cycle detected
                if neighbor not in visited:
                    if not depth_first_search(neighbor):
                        return False
            stack.remove(node)
            return True
        #end of chatgpt
        #iterates through the nodes
        for node in self.adjacency_list:
            if node not in visited:
                if not depth_first_search(node):
                    return False  # Cycle detected
        return True
    
    def topoSort(self):
        if not self.isDag():
            return None  
        
        visited = set()
        list_of_nodes = []
        
        #used chatgpt
        def depthfsearch_topo(node):
            visited.add(node)
            for neighbor, _ in self.adjacency_list.get(node, []):
                if neighbor not in visited:
                    depthfsearch_topo(neighbor)
            list_of_nodes.append(node.data)
        #end of chatgpt
            
        for node in self.adjacency_list:
            if node not in visited:
                depthfsearch_topo(node)
        
        return list_of_nodes[::-1]  
    
# using example of the lectures
print("Testing for a graph without a cycle")
graphOne = Graph()
nodes = [Node(i) for i in range(10)]
for node in nodes:
    graphOne.addNode(node)

edges = [(nodes[0], nodes[1], 1), (nodes[1], nodes[2], 1), (nodes[1], nodes[3], 1),
         (nodes[1], nodes[4], 1), (nodes[3], nodes[5], 1), (nodes[3], nodes[6], 1), 
         (nodes[5], nodes[7], 1), (nodes[6], nodes[8], 1), (nodes[8], nodes[9], 1),
         (nodes[4], nodes[9], 1)]
for edge in edges:
    graphOne.addEdge(*edge)

 # The output should be True
print("Is DAG:", graphOne.isDag()) 
# Output should be:  [0, 1, 4, 3, 6, 8, 9, 5, 7, 2]
print("Topological order:", graphOne.topoSort())  
print ("")

#Now testing for a graph with a cycle
print("Testing for a graph with a cycle")
graphTwo = Graph()
nodes = [Node(i) for i in range(5)]
for node in nodes:
    graphTwo.addNode(node)

edges_cycle = [(nodes[0], nodes[1], 1), (nodes[1], nodes[2], 1),
               (nodes[2], nodes[3], 1), (nodes[3], nodes[0], 1),
               (nodes[3], nodes[4], 1), (nodes[4], nodes[2], 1)]

for edge in edges_cycle:
    graphTwo.addEdge(*edge)

# Output should be False 
print("Is DAG:", graphTwo.isDag())  
# Output should be None
print("Topological order:", graphTwo.topoSort())  
