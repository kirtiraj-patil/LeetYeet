import queue

WHITE = 'white'
BLACK = 'black'
GREY = 'grey'

class Node:
    def __init__(self, key, neighbor):
        self.key = key
        self.color = WHITE
        self.neighbors = [neighbor]

class Graph:
    nodes = {}
    def __init__(self, edges):
        self.createNodes(edges)

    def addEdge(self, vertex1, vertex2):
        vertex1 = str(vertex1)
        vertex2 = str(vertex2)
        if(vertex1 in self.nodes):
            self.nodes[vertex1].neighbors.append(vertex2)
        else:
            newNode = Node(vertex1, vertex2)
            self.nodes[vertex1] = newNode

    def createNodes(self, edges):
        for edge in edges:
            self.addEdge(edge[0], edge[1])
            self.addEdge(edge[1], edge[0])

    def printGraph(self):
        for node in self.nodes:
            print('node: ', node, ' list: ', self.nodes[node].neighbors)

    def BFS(self, startPoint):
        self.BFS_helper(startPoint)
        for node in self.nodes:
            if self.nodes[node].color == WHITE:
                self.BFS_helper(node)

    def BFS_helper(self, start):
        q = queue.Queue()
        q.put(start)
        self.nodes[start].color = GREY

        while not q.empty():
            currentNode = self.nodes[q.get()]
            for i in currentNode.neighbors:
                if(self.nodes[i].color == WHITE):
                    q.put(i)
                    self.nodes[i].color = GREY
            
            currentNode.color = BLACK
            print(currentNode.key)

    def DFS(self,start):
        self.DFS_helper(start)
        for n in self.nodes:
            if self.nodes[n].color == WHITE:
                self.DFS_helper(n)

    def DFS_helper(self, start):
        print(start)
        currentNode = self.nodes[start]
        currentNode.color = GREY

        for n in currentNode.neighbors:
            if self.nodes[n].color == WHITE:
                self.DFS_helper(n)

        currentNode.color = BLACK



g = Graph([[1,0], [0,2],[6,7], [2,3], [2,1], [1,3], [4,5], [5,6], [4,6]])
g.printGraph()
g.DFS('3')