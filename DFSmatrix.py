from pyvis.network import Network

'''
Cristian Aurelio Ramírez Anzaldo    A01066337
Algorithms
'''
class Graph:
      
    adjacency = []
  
    # Initializing adjacency matrix
    def __init__(self, v, e):
          
        self.v = v
        self.e = e
        Graph.adjacency = [[0 for i in range(v)] 
                        for j in range(v)]
  
    # New Edge to graph
    def addEdge(self, start, e):
          
        # bidirectional edge
        Graph.adjacency[start][e] = 1
        Graph.adjacency[e][start] = 1
  
    # DFS algorithm
    def DFS(self, start, visited):
          
        # Printing current node
        print(start, end = ' ')
  
        # Setting current node as visited
        visited[start] = True
  
        # For every node of the graph
        for i in range(self.v):
              
            # check if there is an unvisited node there
            if (Graph.adjacency[start][i] == 1 and
                    (not visited[i])):
                self.DFS(i, visited)
  

v, e = 10, 14
  
network = Network()

# Create the graph
G = Graph(v, e)

nodes = [j for j in range(10)]
network.add_nodes(nodes)

for i in nodes[1:]:
    G.addEdge(0, i)
    network.add_edge(0, i, weight=.87)

G.addEdge(5,2)
network.add_edge(5, 2, weight=.87)

network.toggle_physics(True)
network.show('mygraph.html')
network.show_buttons(filter_=['physics'])
  
visited = [False] * v
  
# DFS
G.DFS(0, visited) 