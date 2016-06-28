# Directed Graph
#  -(c, d) is not same as (d, c)
# Undirected, Weighted Graph
#  -Weights may be negative

# Graph Data Structure API
# Construction
#   - addEdge(u, v, weight)
#   - addNode(u)

# Query
#   - getEdgeWeight(u, v)
#   - neighbors(u)

# Graph Representation Alternative: Adjancency Matrix
# Graph Data Structure Adjacency Matrix in Python
# Adjacency matrix: O(V2) space
#     -No 2-d matrices in Python
#     -Use dict objects with entries
#     -Find edge weight by vertices[i][j]

class DirectedGraphAM:
    def __init__(self, size):
        self.vertices = {}
        self.size = size
        
    def addEdge(self, u, v, weight):
        if not u in self.vertices:
            self.vertices[u] = {}
    
        self.vertices[u][v] = weight
        
    def neighbors(self, u):
        if u in self.vertices:
            for v in self.vertices[u]:
                yield(v, self.vertices[u][v])
                
    def __repr__(self):
        rep = 'graph:['
        for u in range(self.size):
            if u in self.vertices:
                rep += str(u) + ":"
                for v in self.vertices[u]:
                    rep += '(' + str(v) + "," + str(self.vertices[u][v]) + "),"
                
        return rep + ']'
    
