# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        self.targetSum = targetSum
        self.count = 0
        self.DFS(root)

        return self.count

    def DFS(self, node):
        if node == None:
            return {}

        leftObj = self.DFS(node.left)
        rightObj = self.DFS(node.right)
        newObj = {node.val: 1}
        
        for i in leftObj:
            newObj[i + node.val] = leftObj[i]

        for i in rightObj:
            newSum = i + node.val
            if newSum in newObj:
                newObj[newSum] += rightObj[i]
            else:
                newObj[newSum] = rightObj[i]

        if self.targetSum in newObj:
            self.count += newObj[self.targetSum]

        return newObj
