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
myGraph.add_vertex("F")
myGraph.add_edge("A","B")
myGraph.add_edge("A","C")
myGraph.add_edge("B","A")
myGraph.add_edge("B","D")
myGraph.add_edge("B","E")
myGraph.add_edge("C","A")
myGraph.add_edge("C","E")
myGraph.add_edge("D","B")
myGraph.add_edge("D","E")
myGraph.add_edge("D","F")
myGraph.add_edge("E","B")
myGraph.add_edge("E","C")
myGraph.add_edge("E","D")
myGraph.add_edge("E","F")
myGraph.add_edge("F","D")
myGraph.add_edge("F","E")
myGraph.printGraph()
 