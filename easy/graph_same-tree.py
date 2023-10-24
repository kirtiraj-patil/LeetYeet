import queue
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        q1 = queue.Queue()
        q2 = queue.Queue()

        q1.put(p)
        q2.put(q)


        while not q1.empty() and not q2.empty():
            currentNodeP = q1.get()
            currentNodeQ = q2.get()

            if(currentNodeP == None and currentNodeQ == None):
                continue
            elif(currentNodeP == None or currentNodeQ == None):
                return False

            if(currentNodeP.val != currentNodeQ.val):
                return False

            q1.put(currentNodeP.left)
            q2.put(currentNodeQ.left)
            q1.put(currentNodeP.right)
            q2.put(currentNodeQ.right)

        if q1.empty() and q2.empty():
            return True

        return False
            


