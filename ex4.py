#Part 1
import graphviz

class Graph2:
    def __init__(self, num_nodes):
        self.num_nodes = num_nodes
        self.adjacency_matrix = [[0] * num_nodes for _ in range(num_nodes)]

    def addEdge(self, n1, n2, weight):
        if n1 < 0 or n1 >= self.num_nodes or n2 < 0 or n2 >= self.num_nodes:
            raise ValueError("Node index out of bounds")
        self.adjacency_matrix[n1][n2] = weight
        self.adjacency_matrix[n2][n1] = weight 

    def removeEdge(self, n1, n2):
        if n1 < 0 or n1 >= self.num_nodes or n2 < 0 or n2 >= self.num_nodes:
            raise ValueError("Node index out of bounds")
        self.adjacency_matrix[n1][n2] = 0
        self.adjacency_matrix[n2][n1] = 0

    def printGraph(self):
        print("Adjacency Matrix:")
        for row in self.adjacency_matrix:
            print(row)
    
    def drawGraph(self, filename='graph'):
        graph = graphviz.Graph(format='png')

        for i in range(self.num_nodes):
            graph.node(str(i))

        for i in range(self.num_nodes):
            for j in range(i + 1, self.num_nodes):
                if self.adjacency_matrix[i][j] != 0:
                    graph.edge(str(i), str(j), label=str(self.adjacency_matrix[i][j]))

        graph.render(filename, view=True)


# Testing the Graph2 class
graph2 = Graph2(4) 
graph2.addEdge(0, 1, 2)
graph2.addEdge(1, 2, 1)
graph2.addEdge(2, 3, 7)
graph2.printGraph()

graph2.drawGraph()
# Part 2
import graphviz

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
        #self.adjacency_list[n1].remove(n2)
        #self.adjacency_list[n2].remove(n1)
        self.adjacency_list[n1] = [edge for edge in self.adjacency_list[n1] if edge[0] != n2]
    
    def printGraph(self):
        print("Nodes and Adjacency List:")
        for node, adjacent_nodes in self.adjacency_list.items():
            print(node.data, "->", [(adjacent_node[0].data, adjacent_node[1]) for adjacent_node in adjacent_nodes])

    def importFromFile(self, filename):
        self.adjacency_list = {}
        try:
            with open(filename, 'r') as file:
                lines = file.readlines()
                if len(lines) < 2 or not lines[0].startswith("strict graph"):
                    return None  # Not a valid GraphViz file
                for line in lines[1:]:
                    line = line.strip()
                    if line and not line.startswith("{") and not line.startswith("}"):
                        parts = line.split("[")  
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
    
    def dfs(self, start_node):
        visited = set()
        dfs_order = []

        def dfs_util(node):
            visited.add(node)
            dfs_order.append(node)

            for neighbor, _ in self.adjacency_list[node]:
                if neighbor not in visited:
                    dfs_util(neighbor)

        dfs_util(start_node)
        return dfs_order

class Graph2:
    def __init__(self, num_nodes):
        self.num_nodes = num_nodes
        self.adjacency_matrix = [[0] * num_nodes for _ in range(num_nodes)]

    def addEdge(self, n1, n2, weight):
        if n1 < 0 or n1 >= self.num_nodes or n2 < 0 or n2 >= self.num_nodes:
            raise ValueError("Node index out of bounds")
        self.adjacency_matrix[n1][n2] = weight
        self.adjacency_matrix[n2][n1] = weight  # If the graph is undirected

    def removeEdge(self, n1, n2):
        if n1 < 0 or n1 >= self.num_nodes or n2 < 0 or n2 >= self.num_nodes:
            raise ValueError("Node index out of bounds")
        self.adjacency_matrix[n1][n2] = 0
        self.adjacency_matrix[n2][n1] = 0

    def printGraph(self):
        print("Adjacency Matrix:")
        for row in self.adjacency_matrix:
            print(row)
    
    def dfs(self, start_node):
        visited = set()
        dfs_order = []

        def dfs_util(node):
            visited.add(node)
            dfs_order.append(node)

            for i in range(self.num_nodes):
                if self.adjacency_matrix[node][i] != 0 and i not in visited:
                    dfs_util(i)

        dfs_util(start_node)
        return dfs_order

# Test the Graph class
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

dfs_order = graph.dfs(nodeOne)
print("DFS order for Graph:")
for node in dfs_order:
    print(node.data)

# Test the Graph2 class
graph2 = Graph2(4)
graph2.addEdge(0, 1, 2)
graph2.addEdge(1, 2, 1)
graph2.addEdge(2, 3, 7)

dfs_order = graph2.dfs(0)
print("\nDFS order for Graph2:")
for node in dfs_order:
    print(node)

#Part 3
import time

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
        if n1 not in self.adjacency_list or n2 not in self.adjacency_list:
            raise ValueError("One of the nodes does not exist in the graph. Try again")
        self.adjacency_list[n1].append((n2, weight))
    
    def removeEdge(self, n1, n2):
        if n1 not in self.adjacency_list or n2 not in self.adjacency_list:
            raise ValueError("One of the nodes does not exist in the graph. Try again")
        self.adjacency_list[n1] = [edge for edge in self.adjacency_list[n1] if edge[0] != n2]
    
    def printGraph(self):
        print("Nodes and Adjacency List:")
        for node, adjacent_nodes in self.adjacency_list.items():
            print(node.data, "->", [(adjacent_node[0].data, adjacent_node[1]) for adjacent_node in adjacent_nodes])

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
    
    def dfs(self, start_node):
        visited = set()
        dfs_order = []

        def dfs_util(node):
            visited.add(node)
            dfs_order.append(node)

            for neighbor, _ in self.adjacency_list[node]:
                if neighbor not in visited:
                    dfs_util(neighbor)

        dfs_util(start_node)
        return dfs_order

def measure_performance(graph, iterations=10):
    total_times = []
    for _ in range(iterations):
        start_time = time.time()
        start_node = list(graph.adjacency_list.keys())[0]  # Starting node
        graph.dfs(start_node)
        end_time = time.time()
        total_times.append(end_time - start_time)
    max_time = max(total_times)
    min_time = min(total_times)
    avg_time = sum(total_times) / len(total_times)
    return max_time, min_time, avg_time

filename = "random.dot"
graph = Graph()
result = graph.importFromFile(filename)

if result:
    max_time_graph, min_time_graph, avg_time_graph = measure_performance(graph)
    print("Performance of dfs() for Graph:")
    print("Maximum time:", max_time_graph)
    print("Minimum time:", min_time_graph)
    print("Average time:", avg_time_graph)
else:
    print("Failed to read graph from file")



class Graph2:
    def __init__(self, num_nodes):
        self.num_nodes = num_nodes
        self.adjacency_matrix = [[0] * num_nodes for _ in range(num_nodes)]

    def addEdge(self, n1, n2, weight):
        if n1 < 0 or n1 >= self.num_nodes or n2 < 0 or n2 >= self.num_nodes:
            raise ValueError("Node index out of bounds")
        self.adjacency_matrix[n1][n2] = weight
        self.adjacency_matrix[n2][n1] = weight  # If the graph is undirected

    def removeEdge(self, n1, n2):
        if n1 < 0 or n1 >= self.num_nodes or n2 < 0 or n2 >= self.num_nodes:
            raise ValueError("Node index out of bounds")
        self.adjacency_matrix[n1][n2] = 0
        self.adjacency_matrix[n2][n1] = 0

    def printGraph(self):
        print("Adjacency Matrix:")
        for row in self.adjacency_matrix:
            print(row)
    
    def importFromFile(self, filename):
        self.num_nodes = 0  # Initialize the number of nodes
        self.adjacency_matrix = []  # Initialize the adjacency matrix

        try:
            with open(filename, 'r') as file:
                lines = file.readlines()
                if len(lines) < 2 or not lines[0].startswith("strict graph"):
                    return False  # Not a valid GraphViz file

                nodes = set()  # Set to store distinct nodes

                for line in lines[1:]:
                    line = line.strip()
                    if line and not line.startswith("{") and not line.startswith("}"):
                        parts = line.split("[")
                        edge_info = parts[0].strip().split("--")
                        n1 = edge_info[0].strip()
                        n2 = edge_info[-1].strip()
                        nodes.add(n1)  # Add nodes to the set
                        nodes.add(n2)

                self.num_nodes = len(nodes)  # Set the number of nodes
                self.adjacency_matrix = [[0] * self.num_nodes for _ in range(self.num_nodes)]  # Initialize adjacency matrix

                return True
        except FileNotFoundError:
            return False
        except Exception as e:
            print("Error:", e)
            return False
 
    def dfs(self, start_node):
        visited = set()
        dfs_order = []

        def dfs_util(node):
            visited.add(node)
            dfs_order.append(node)

            for i in range(self.num_nodes):
                if self.adjacency_matrix[node][i] != 0 and i not in visited:
                    dfs_util(i)

        dfs_util(start_node)
        return dfs_order

def measure_performance(graph, iterations=10):
    total_times = []
    for _ in range(iterations):
        start_time = time.time()
        start_node = 0  # Starting node
        graph.dfs(start_node)
        end_time = time.time()
        total_times.append(end_time - start_time)
    max_time = max(total_times)
    min_time = min(total_times)
    avg_time = sum(total_times) / len(total_times)
    return max_time, min_time, avg_time

filename = "random.dot"
graph2 = Graph2(0)  # Initialize with 0 nodes
num_nodes = graph2.importFromFile(filename)  # Update the number of nodes

if num_nodes:
    max_time_graph2, min_time_graph2, avg_time_graph2 = measure_performance(graph2)
    print("Performance of dfs() for Graph2:")
    print("Maximum time:", max_time_graph2)
    print("Minimum time:", min_time_graph2)
    print("Average time:", avg_time_graph2)
else:
    print("Failed to read graph from file")


    """Based on the results generated by the time calculation it can be seen that Graph2 works faster than graph one
    this is becuase for dense graphs with many edges, adjacency matrices works better than adjacency lists which is used by 
    Graph thats why its a bit slower than Graph2.
    """