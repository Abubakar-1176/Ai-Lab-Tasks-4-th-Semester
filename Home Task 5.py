import networkx as nx
import matplotlib.pyplot as plt
from collections import deque

#  This is creating a graph
G = nx.Graph()

cities = ["Seattle", "San Francisco", "Los Angeles", "Denver", "Kansas City", "Chicago", "New York", "Boston", "Atlanta", "Miami", "Dallas", "Houston"]
G.add_nodes_from(cities)

# edges of the graph (connections between cities)
edges = [
    ('Seattle', 'San Francisco'),
    ('Seattle', 'Denver'),
    ('Seattle', 'Chicago'),
    ('San Francisco', 'Los Angeles'),
    ('San Francisco', 'Denver'),
    ('Los Angeles', 'Denver'),
    ('Los Angeles', 'Dallas'),
    ('Denver', 'Kansas City'),
    ('Denver', 'Chicago'),
    ('Kansas City', 'Chicago'),
    ('Kansas City', 'New York'),
    ('Kansas City', 'Atlanta'),
    ('Kansas City', 'Dallas'),
    ('Chicago', 'Boston'),
    ('Chicago', 'New York'),
    ('New York', 'Boston'),
    ('New York', 'Atlanta'),
    ('Atlanta', 'Miami'),
    ('Atlanta', 'Dallas'),
    ('Atlanta', 'Houston'),
    ('Dallas', 'Houston'),
    ('Houston', 'Miami')
]

G.add_edges_from(edges)

# Function for BFS
def bfs(graph, start):
    visited = set()
    queue = deque([start])
    bfs_order = []

    while queue:
        vertex = queue.popleft()
        if vertex not in visited:
            visited.add(vertex)
            bfs_order.append(vertex)
            queue.extend(neighbor for neighbor in graph[vertex] if neighbor not in visited)

    return bfs_order

# Function for DFS
def dfs(graph, start):
    visited = set()
    stack = [start]
    dfs_order = []

    while stack:
        vertex = stack.pop()
        if vertex not in visited:
            visited.add(vertex)
            dfs_order.append(vertex)
            stack.extend(neighbor for neighbor in graph[vertex] if neighbor not in visited)

    return dfs_order

# Call BFS and DFS on the graph
print("BFS starting from Seattle:", bfs(G, 'Seattle'))
print("DFS starting from Seattle:", dfs(G, 'Seattle'))

# Draw the graph
plt.figure(figsize=(10, 8))
pos = nx.spring_layout(G)

nx.draw(G, pos, with_labels=True, node_color='lightblue', node_size=500, font_size=10)
plt.title("Graph shows the cities of United States and their connections")
plt.show()