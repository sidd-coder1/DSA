# Graph consist of a finite set of vertices(or nodes) and a set of edges connecting these vertices.
#  Graphs can be directed or undirected, weighted or unweighted,
#  and can be used to model various real-world problems such as social networks, transportation systems, and computer networks.
# weighted graph: a graph in which each edge has a weight or cost associated with it. The weight can represent distance, time, or any other measure of cost.
# Unweighted graph : a graph in which all edges have the same weight or cost, typically represented as 1. In an unweighted graph, the focus is on the presence or absence of edges rather than their weights.
# Directed graph: a graph in which edges have a direction, meaning they go from one vertex to another. In a directed graph, the edges are represented as ordered pairs of vertices (u, v), where u is the starting vertex and v is the ending vertex.
# Undirected graph: a graph in which edges do not have a direction, meaning they can be traversed in both directions. In an undirected graph, the edges are represented as unordered pairs of vertices {u, v}, where u and v are connected by an edge.  
# cyclic graph: a graph that contains at least one cycle, which is a path that starts and ends at the same vertex without repeating any edges or vertices (except for the starting/ending vertex).
# acyclic graph: a graph that does not contain any cycles. In an acyclic graph, there are no paths that start and end at the same vertex without repeating edges or vertices.
# complete graph: a graph in which every pair of distinct vertices is connected by a unique edge. In a complete graph with n vertices, there are n(n-1)/2 edges.

  

# if a graph is complete or almost complete, then we can use adjacency matrix to represent the graph.
# If the number of edges are few (sparse), then we can use adjacency list to represent the graph.




class Graph:
    def __init__(self):
        self.adjacency_List = {}
    def add_vertex(self,vertex):
        if vertex not in self.adjacency_List:
            self.adjacency_List[vertex]=[]
            return True
        return False
    def printGraph(self):
        for vertex in self.adjacency_List:
            print(vertex,":",self.adjacency_List[vertex])
    def add_edge(self,vertex1,vertex2):
        if vertex1 in self.adjacency_List .keys() and vertex2 in self.adjacency_List.keys():
            self.adjacency_List[vertex1].append(vertex2)
            # self.adjacency_List[vertex2].append(vertex1)
            return True
        return False

myGraph=Graph() 
myGraph.add_vertex("A")
myGraph.add_vertex("B") 
myGraph.add_vertex("C")
myGraph.add_vertex("D")
myGraph.add_vertex("E")
myGraph.add_edge("A","B")
myGraph.add_edge("A","C")
myGraph.add_edge("A","D")
myGraph.add_edge("B","A")
myGraph.add_edge("B","E")
myGraph.add_edge("C","A")
myGraph.add_edge("C","D")
myGraph.add_edge("D","A")
myGraph.add_edge("D","C")
myGraph.add_edge("D","E")
myGraph.add_edge("E","B")
myGraph.add_edge("E","D")
myGraph.printGraph()
 