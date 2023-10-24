# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        self.targetSum = targetSum
        self.res = []
        self.currentActivePath = []

        self.DFS(0, root)
        return self.res

    def save(self):
        self.res.append([] + self.currentActivePath)

    def DFS(self, currentSum, node):
        if node == None:
            return

        newSum = currentSum + node.val
        self.currentActivePath.append(node.val)
        if(newSum == self.targetSum and node.left == None and node.right == None):
            self.save()
            self.currentActivePath.pop()
            return

        self.DFS(newSum, node.left)
        self.DFS(newSum, node.right)
        self.currentActivePath.pop()
        return


        