
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
        self.adjacency_list[n2].append((n1, weight))
    
    def removeEdge(self, n1, n2):
        if n1 not in self.adjacency_list or n2 not in self.adjacency_list:
            raise ValueError("One of the nodes does not exist in the graph. Try again")
        self.adjacency_list[n1].remove(n2)
        self.adjacency_list[n2].remove(n1)
    
    #used chatgpt
    def printGraph(self):
        print("Nodes and Adjacency List:")
        for node, adjacent_nodes in self.adjacency_list.items():
            print(node.data, "->", [(adjacent_node[0].data, adjacent_node[1]) for adjacent_node in adjacent_nodes])
    #end of chatgpt
            
    def importFromFile(self, filename):
        self.adjacency_list = {}
        try:
            with open(filename, 'r') as file:
                lines = file.readlines()
                if len(lines) < 2 or not lines[0].startswith("strict graph"):
                    return None  # Not a valid GraphViz file
                
                #used chatgpt to help me with this part
                for line in lines[1:]:
                    line = line.strip()
                    #print("Debug: Line:", line) 
                    if line and not line.startswith("{") and not line.startswith("}"):
                        parts = line.split("[")  
                        #print("Debug: Parts:", parts)  
                        
                        edge_info = parts[0].strip().split("--")
                        n1 = Node(edge_info[0].strip())
                        n2 = Node(edge_info[-1].strip())

                        weight = 1 
                        if len(parts) > 1:
                            attr_parts = parts[1].split("]")[0].split(",")
                            for attr in attr_parts:
                                key, value = attr.strip().split("=")
                                if key == "weight":
                                    weight = int(value.strip())
                    #end of chatgpt help
                                    
                        if n1 not in self.adjacency_list:
                            self.addNode(n1)
                        if n2 not in self.adjacency_list:
                            self.addNode(n2)
                        self.addEdge(n1, n2, weight)

                        
            return True  
        except FileNotFoundError:
            return None  
        except Exception as e:
            print("Error:", e)
            return None  
        
# Create a graph
graph = Graph()

nodeOne = Node("A")
nodeTwo = Node("B")
nodeThree = Node("C")
nodeFour = Node("D")

graph.addNode(nodeOne)
graph.addNode(nodeTwo)
graph.addNode(nodeThree)
graph.addNode(nodeFour)
graph.addEdge(nodeOne, nodeTwo, 2)
graph.addEdge(nodeTwo, nodeThree, 1)
graph.addEdge(nodeThree, nodeFour, 7)

"""
print("Adjacency List:")
for node, adjacent_nodes in graph.adjacency_list.items():
    print(node.data, "->", [adjacent_node[0].data for adjacent_node in adjacent_nodes]) 
"""

graph.removeNode(nodeThree)
graph.printGraph()
print (" ")


# Test the importFromFile method
""" 
graph = Graph()
result = graph.importFromFile('try.dot')
if result is True:
    print("Graph imported successfully!")
    graph.printGraph()
elif result is None:
    print("Error occurred during import or file not found.")
else:
    print("Invalid GraphViz file.")
"""
