# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):

  def removeNthFromEnd(self, head, n):
    """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
    forwardPointer = head
    dataPointer = head
    dataPrevious = None
    i = n - 1
    while i > 0:
      forwardPointer = forwardPointer.next
      i = i - 1

    while forwardPointer.next != None:
      dataPrevious = dataPointer
      dataPointer = dataPointer.next
      forwardPointer = forwardPointer.next

    if dataPrevious == None:
      return head.next

    dataPrevious.next = dataPointer.next
    return head
