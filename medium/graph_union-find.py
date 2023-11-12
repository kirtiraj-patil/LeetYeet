class DisjointSet:
    def __init__(self, nodes):
        self.rank = [0] * len(nodes)
        self.parent = []
        for i in range(len(nodes) + 1):
            self.parent.append(i)
