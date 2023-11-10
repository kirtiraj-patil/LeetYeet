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

    def searchNode(self, val):
        res = self.searchNodeHelper(self.root, val)
        return res

    def searchNodeHelper(self, root, val):
        if root == None:
            return None

        if root.val == val:
            return root
        elif root.val > val:
            return self.searchNodeHelper(root.left, val)
        return self.searchNodeHelper(root.right, val)

    def inorderSuccessor(self, root):
        root = root.right
        while root.left != None:
            root = root.left
        return root

    def deleteNode(self, val, root=None):
        parent = None
        whichChild = None
        currentNode = root or self.root

        while currentNode != None:
            if currentNode.val == val:
                break
            parent = currentNode
            if currentNode.val < val:
                currentNode = currentNode.right
                whichChild = "right"
            else:
                currentNode = currentNode.left
                whichChild = "left"

        if currentNode == None:
            return False

        if parent == None or (currentNode.left != None and currentNode.right != None):
            inSuccessor = self.inorderSuccessor(currentNode)
            currentNode.val = inSuccessor.val
            return self.deleteNode(inSuccessor.val, currentNode.right)
        elif currentNode.left != None and currentNode.right == None:
            if whichChild == "right":
                parent.right = currentNode.left
            else:
                parent.left = currentNode.left
        elif currentNode.left == None and currentNode.right != None:
            if whichChild == "right":
                parent.right = currentNode.right
            else:
                parent.left = currentNode.right
        else:
            if whichChild == "right":
                parent.right = None
            else:
                parent.left = None

        return True


arr = [5, 2, 4, 1, 8, 11, 6, 9, 12, 10, 11.5]
b = BST(arr)


def printTree():
    for n in arr:
        r = b.searchNode(n)
        if r == None:
            continue
        print(r.val, r.left and r.left.val, r.right and r.right.val)


printTree()
b.deleteNode(12)
print("")
printTree()
