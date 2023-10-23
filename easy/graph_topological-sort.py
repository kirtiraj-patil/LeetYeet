
WHITE = 'white'
BLACK = 'black'
GREY = 'grey'

class Node:
    def __init__(self, key):
        self.key = key
        self.outgoing = []
        self.incoming = []
        self.color = WHITE

class Graph:
    nodes = {}
    def __init__(self, edges) -> None:
        self.createGraph(edges)

    def addEdge(self, vertex1, vertex2):
        if not vertex1 in self.nodes:
            self.nodes[vertex1] = Node(vertex1)

        self.nodes[vertex1].outgoing.append(vertex2)
        
        if not vertex2 in self.nodes:
            self.nodes[vertex2] = Node(vertex2)
        
        self.nodes[vertex2].incoming.append(vertex1)

    def createGraph(self, edges):
        for edge in edges:
            self.addEdge(edge[0], edge[1])

    def topological_sort(self):
        self.sortOrder = []
        for n in self.nodes:
            if len(self.nodes[n].incoming) == 0:
                self.DFS(n)

        # reverse the order in which the nodes are fully explored, that is the topological sort
        # as the nodes which are not a dependency on anyone are fully explored first.
        self.sortOrder = self.sortOrder[::-1]
        print(self.sortOrder)

    def DFS(self, start):
        currentNode = self.nodes[start]
        currentNode.color = GREY

        for o in currentNode.outgoing:
            if self.nodes[o].color == WHITE:
                self.DFS(o)

        currentNode.color = BLACK
        self.sortOrder.append(start)

g = Graph([[0, 1], [1, 3], [2, 3], [3, 4], [3, 5], [4, 6], [5, 6], [5,7]])
g.topological_sort()