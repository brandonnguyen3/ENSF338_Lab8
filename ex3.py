#ENSF338 Lab 8 Exercise 3

import networkx as nx

import matplotlib.pyplot as plt  # Importing matplotlib for plotting
#used chatgpt

# QUESTION 2: Union Find
class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n

    def find(self, u):
        if self.parent[u] != u:
            self.parent[u] = self.find(self.parent[u])
        return self.parent[u]

    def union(self, u, v):
        pu, pv = self.find(u), self.find(v)
        if pu != pv:
            if self.rank[pu] < self.rank[pv]:
                self.parent[pu] = pv
            elif self.rank[pu] > self.rank[pv]:
                self.parent[pv] = pu
            else:
                self.parent[pv] = pu
                self.rank[pu] += 1

# QUESTION 3: Kruskal's algorithm
class Graph:
    def __init__(self):
        self.edges = []

    def add_edge(self, u, v, weight):
        self.edges.append((u, v, weight))

    def mst(self):
        self.edges.sort(key=lambda x: x[2])  # Sort edges by weight
        n = len(self.edges)
        uf = UnionFind(n)
        mst_graph = Graph()

        for u, v, weight in self.edges:
            if uf.find(u) != uf.find(v):
                uf.union(u, v)
                mst_graph.add_edge(u, v, weight)

        return mst_graph

# Example usage:
# Create a graph
g = Graph()
g.add_edge(0, 3, 3)
g.add_edge(0, 4, 12)
g.add_edge(3, 2, 3)
g.add_edge(3, 1, 5)
g.add_edge(1, 2, 2)
g.add_edge(2, 4, 7)


# Calculate MST
mst = g.mst()

# Visualize the MST
Gnx = nx.Graph()
for u, v, weight in mst.edges:
    Gnx.add_edge(u, v, weight=weight)

nx.draw(Gnx, with_labels=True)
plt.show()
