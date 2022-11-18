# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):

  def deleteMiddle(self, head):
    """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
    dataPointer = head
    dataPrevious = None
    forwardPointer = head.next

    if forwardPointer == None:
      return None

    while True:
      try:
        if forwardPointer != None:
          dataPrevious = dataPointer
          dataPointer = dataPointer.next
        forwardPointer = forwardPointer.next.next
      except AttributeError:
        dataPrevious.next = dataPointer.next
        return head
