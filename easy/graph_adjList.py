class Graph:
    def __init__(self, edges):
        self.adjacencyList = {}
        self.makeAdjacencyList(edges)

    def addEdge(self, vertex1, vertex2):
        vertex1 = str(vertex1)
        vertex2 = str(vertex2)
        if(vertex1 in self.adjacencyList):
            self.adjacencyList[vertex1].append(vertex2)
        else:
            self.adjacencyList[vertex1] = [vertex2]

    def makeAdjacencyList(self, edges):
        for edge in edges:
            self.addEdge(edge[0], edge[1])
            self.addEdge(edge[1], edge[0])

    def printAdjacencyList(self):
        for vertex in self.adjacencyList:
            print('vertex: ', vertex, 'list: ', self.adjacencyList[vertex])

g = Graph([[1,0], [0,2], [2,3], [2,1], [1,3]])
g.printAdjacencyList()

