class Node:
    # Constructor to create a new node with data
    def __init__(self, data):
        self.data = data

class Graph:
    def __init__(self):
        self.adjacency_list = {}
    
    def addNode(self, node):
        node =Node(node)
        self.adjacency_list[node.data] = []
        return node
    
    def removeNode(self, node):
        del self.adjacency_list[node]
        for adjacentNodes in self.adjacency_list.values():
            if node in adjacentNodes:
                adjacentNodes.remove(node)
    
    def addEdge(self, n1, n2, weight=None):
        # Check if both nodes exist in the graph
        if n1 not in self.adjacency_list or n2 not in self.adjacency_list:
            raise ValueError("Error. One of the nodes does not exist in the graph")
        self.adjacency_list[n1].append((n2, weight))
        self.adjacency_list[n2].append((n1, weight))
    
    def removeEdge(self, n1, n2):
        if n1 not in self.adjacency_list or n2 not in self.adjacency_list:
            raise ValueError("Error. One of the nodes does not exist in the graph")
        self.adjacency_list[n1].remove(n2)
        self.adjacency_list[n2].remove(n1)

        #self.adjacency_list[n1] = [(node, weight) for node, weight in self.adjacency_list[n1] if node != n2]
        #self.adjacency_list[n2] = [(node, weight) for node, weight in self.adjacency_list[n2] if node != n1]
    
    def importFromFile(self, filename):
        with open(filename, 'r') as file:
            lines = file.readlines()
            for line in file:
                return      

# Create a graph
graph = Graph()

# Add nodes
node1 = graph.addNode("A")
node2 = graph.addNode("B")
node3 = graph.addNode("C")

# Add edges
graph.addEdge(node1.data, node2.data, 2)
graph.addEdge(node2.data, node3.data, 1)

# Print adjacency list
print("Adjacency List:")
for node, adjacent_nodes in graph.adjacency_list.items():
    print(node, "->", adjacent_nodes)

# Remove node
graph.removeNode(node2.data)

# Print adjacency list after removing node
print("\nAdjacency List after removing node B:")
for node, adjacent_nodes in graph.adjacency_list.items():
    print(node, "->", adjacent_nodes)
