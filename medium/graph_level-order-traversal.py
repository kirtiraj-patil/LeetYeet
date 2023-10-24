import queue
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        q1 = queue.Queue()
        q2 = queue.Queue()

        if(root == None):
            return []
        
        q1.put(root)
        res = [[root.val]]
        tempList = []

        while not q1.empty() or not q2.empty():
            if q1.empty():
                res.append(tempList)
                tempList = []
                q1 = q2
                q2 = queue.Queue()

            currentNode = q1.get()
            if currentNode.left != None:
                q2.put(currentNode.left)
                tempList.append(currentNode.left.val)
            
            if currentNode.right != None:
                q2.put(currentNode.right)
                tempList.append(currentNode.right.val)

        print(res)

        return res


        