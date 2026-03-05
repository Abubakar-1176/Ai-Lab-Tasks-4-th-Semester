print("______________________ Graph Class Implementation Using List ________________________")
from collections import deque
class Graph:
    def __init__(self):
        self.edges = {}
        

    def addVertex(self, vertex):
       self.edges[vertex] = deque()
     
    def addEdge(self, u,v):
      if u in self.edges and v not in self.edges[u]:
          self.edges[u].append(v)
      if v in self.edges and u not in self.edges[v]:
           self.edges[v].append(u)    
    def printGraph(self):
        for vertex, neighbors in self.edges.items():
            print(f"{vertex}: {list(neighbors)}") 

# List of vertices and edges

vertices = ["Seattle", "San Francisco", "Los Angeles", "Denver", 
            "Kansas City", "Chicago", "Boston", "New York", 
            "Atlanta", "Miami", "Dallas", "Houston"]

edges = [
    [0, 1], [0, 3], [0, 5],            # Seattle - San Francisco, Denver, Chicago
    [1, 2], [1, 3],                    # San Francisco - Los Angeles, Denver
    [2, 3], [2, 4], [2, 10],           # Los Angeles - Denver, Kansas City, Dallas
    [3, 4], [3, 5],                    # Denver - Kansas City, Chicago
    [4, 5], [4, 7], [4, 8], [4, 10],   # Kansas City - Chicago, New York, Atlanta, Dallas
    [5, 6], [5, 7],                    # Chicago - Boston, New York
    [6, 7],                            # Boston - New York
    [7, 8],                            # New York - Atlanta
    [8, 9], [8, 10], [8, 11],          # Atlanta - Miami, Dallas, Houston
    [9, 11],                           # Miami - Houston
    [10, 11]                           # Dallas - Houston
]
graph2=Graph()
for vertex in vertices:
    graph2.addVertex(vertex)

for edge in edges:
    graph2.addEdge(vertices[edge[0]], vertices[edge[1]])

print("Graph representation:")
graph2.printGraph()   

# Visualize the graph using NetworkX      
import matplotlib.pyplot as plt
import networkx as nx
G = nx.Graph()
G.add_nodes_from(vertices)
nx_edges=[(vertices[u], vertices[v]) for u,v in edges]
G.add_edges_from(nx_edges)
nx.draw(G, with_labels=True, node_color='lightblue', node_size=500, font_size=10)
plt.title("Graph Visualization")
plt.show()


print("______________________ Graph Implementation Using Dictionary ________________________")

romania = {
   'Sibiu': ['Fagaras','Rimnicu Vilcea'],
    'Fagaras': ['Bucharest'],
    'Rimnicu Vilcea': [ 'Pitesti'],
    'Pitesti': ['Bucharest'],
}
def breadth_first(start,goal,neighbors):
    frontier=[start]
    previous={start:None}
    while frontier:
        current=frontier.pop(0)
        if current==goal:
            path=[]
            while current is not None:
                path.append(current)
                current=previous[current]
            return path[::-1]
        for neighbor in neighbors.get(current,[]):
            if neighbor not in previous:
                frontier.append(neighbor)
                previous[neighbor]=current
    return []        
start='Sibiu'
goal='Bucharest'
path=breadth_first(start,goal,romania)
print(f"Path from {start} to {goal}: {path}")   

# Using NetworkX to visualize the graph
import networkx as nx
import matplotlib.pyplot as plt
G = nx.from_dict_of_lists(romania)
nx.draw_networkx(G,node_size=1000,node_color='red')
plt.show()

   