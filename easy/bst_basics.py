class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class BST:
    root = None
    def __init__(self, nodes):
        self.root = Node(nodes[0])
        for node in nodes[1:]:
            self.insert(self.root, node)

    def insert(self, root, val):
        if root == None:
            return Node(val)
        else:
            if val <= root.val:
                root.left = self.insert(root.left, val)
            else:
                root.right = self.insert(root.right, val)

        return root
            
                    