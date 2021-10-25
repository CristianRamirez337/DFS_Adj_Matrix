from pyvis.network import Network

# Python3 implementation of the approach 
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
              
            # If some node is adjacent to the 
            # current node and it has not 
            # already been visited
            if (Graph.adjacency[start][i] == 1 and
                    (not visited[i])):
                self.DFS(i, visited)
  

v, e = 5, 4
  
network = Network()

# Create the graph
G = Graph(v, e)

nodes = [0, 1, 2, 3, 4]
network.add_nodes(nodes)

for i in nodes:
    G.addEdge(0, i)
    network.add_edge(0, i, weight=.87)


network.toggle_physics(True)
network.show('mygraph.html')
network.show_buttons(filter_=['physics'])
  
# Visited vector to so that a vertex
# is not visited more than once
# Initializing the vector to false as no
# vertex is visited at the beginning
visited = [False] * v
  
# Perform DFS
G.DFS(0, visited);
  
# This code is contributed by ng24_7