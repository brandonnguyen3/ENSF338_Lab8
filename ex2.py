"""
QUESTION ONE
1. List two possible ways to implement this queue, with different efficiency (a slow one which uses linear search, and something faster).
-linear search and using heaps

"""

import heapq
import timeit 
import time
import matplotlib.pyplot as plt

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
      
    def neighbors(self, node):
        if node is None:
            print("Error: Current node is None.")
            return []

        print("Current node:", node.data)  # Debugging output
        if node not in self.adjacency_list:
            print("Error: Node not found in adjacency list.")
            return []
        return self.adjacency_list[node]

    
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
    
    def printGraph(self):
        print("Nodes and Adjacency List:")
        for node, adjacent_nodes in self.adjacency_list.items():
            print(node.data, "->", [(adjacent_node[0].data, adjacent_node[1]) for adjacent_node in adjacent_nodes])
  
    
#linear seach implementation
def slowDji(graph, start):
    # Initialize the distance of all nodes to infinity
    distance = {node: float('infinity') for node in graph.adjacency_list}
    distance[start] = 0
    visited = set()

    # Loop to visit all nodes
    while any(node not in visited for node in graph.adjacency_list):
        # Find the node with the smallest distance
        current = None
        min_distance = float('infinity')

        for node in graph.adjacency_list:
            # Check if the node has been visited and if the distance is less than the minimum distance
            # If true, update the minimum distance and the current node
            if node not in visited and distance[node] < min_distance:
                min_distance = distance[node]
                current = node
        visited.add(current)

        print("Processing node:", current.data)  # Debugging output
        for neighbor, weight in graph.neighbors(current):
            # Update the distance of the neighbor if the current distance + weight is less than neighbor's current distance 
            newPath = distance[current] + weight
            if newPath < distance[neighbor]:
                distance[neighbor] = newPath
        
    return distance

    
def fastDji(graph, start):
    #initialize the distance of all nodes to infinity
    distance = {node: float('infinity') for node in graph.adjacency_list}
    distance[start] = 0
    visited = set()
    heap = [(0, start)]

    while heap:
        current_distance, current = heapq.heappop(heap)
        if current in visited:
            continue
        visited.add(current)
        
        for neighbor, weight in graph.neighbors(current):
            newPath = current_distance + weight
            if newPath < distance[neighbor]:
                distance[neighbor] = newPath
                heapq.heappush(heap, (newPath, neighbor))
    return distance

"""
#used chatgpt
def performance(graph):
    slowAlgorithm = []
    fastAlgorithm = []

    for node in graph.adjacency_list:
        slowAlgorithm.append(timeit.timeit(lambda: slowDji(graph, node), number=1))
        fastAlgorithm.append(timeit.timeit(lambda: fastDji(graph, node), number=1))

    slowAvg = sum(slowAlgorithm) / len(slowAlgorithm)
    fastAvg = sum(fastAlgorithm) / len(fastAlgorithm)

    return slowAlgorithm, fastAlgorithm, slowAvg, fastAvg
#end of chatgpt
 """


def measure_performance(graph):
    slow_times = []
    fast_times = []

    for node in graph.adjacency_list:
        if node is None:
            print("Error: Found a None node.")
            continue
        print("Processing node:", node.data)  # Print the node being processed
        start_time = time.time()
        slowDji(graph, node)
        slow_times.append(time.time() - start_time)

        start_time = time.time()
        fastDji(graph, node)
        fast_times.append(time.time() - start_time)

    slow_avg = sum(slow_times) / len(slow_times)
    fast_avg = sum(fast_times) / len(fast_times)

    return slow_times, fast_times, slow_avg, fast_avg
    
# Test the importFromFile method

example = Graph()
result = example.importFromFile('random.dot')
if result is True:
    print("Graph imported successfully!")
    print("Nodes in the graph:", [node.data for node in example.adjacency_list.keys()])

    #graph.printGraph()
elif result is None:
    print("Error occurred during import or file not found.")
else:
    print("Invalid GraphViz file.")

#slowTime, fastTime, slowAvg, fastAvg = measure_performance(example)
resultOne = measure_performance(example)
print(result)

"""
print("Slow Algorithm:")
print("Average time:", slowAvg)
print("Max time:", max(slowTime))
print("Min time:", min(slowTime))

print("\nFast Algorithm:")
print("Average time:", fastAvg)
print("Max time:", max(fastTime))
print("Min time:", min(fastTime))


def plot_histogram(data, title):
    plt.hist(data, bins=20)
    plt.title(title)
    plt.xlabel('Time')
    plt.ylabel('Frequency')
    plt.show()

plot_histogram(slowTime, 'Dijkstra’s Algorithm using linear search (slow implementation)')
plot_histogram(fastTime, 'Dijkstra’s Algorithm using heaps (fast implementation)')
"""