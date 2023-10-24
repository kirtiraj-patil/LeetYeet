# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if root == None and targetSum == 0:
            return False

        self.targetSum = targetSum
        return self.DFS(0, root)

    def DFS(self, currentSum, node):
        if node == None:
            return False

        newSum = currentSum + node.val

        if newSum == self.targetSum and node.left == None and node.right == None:
            return True

        return self.DFS(newSum, node.left) or self.DFS(newSum, node.right)

        