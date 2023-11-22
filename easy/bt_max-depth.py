# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    maxD = 0

    def maxDepth(self, root: Optional[TreeNode], currentDepth=0) -> int:
        if root == None:
            if self.maxD < currentDepth:
                self.maxD = currentDepth
            return self.maxD

        self.maxDepth(root.left, currentDepth + 1)
        self.maxDepth(root.right, currentDepth + 1)
        return self.maxD
