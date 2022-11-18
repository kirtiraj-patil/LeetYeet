# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):

  def __init__(self):
    self.resHead = None
    self.resFirst = None

  def insertNode(self, newVal):
    newNode = ListNode(newVal)
    if (self.resHead == None):
      self.resHead = newNode
      self.resFirst = newNode
    else:
      self.resHead.next = newNode
      self.resHead = newNode

  def addTwoNumbers(self, l1, l2):
    """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
    carry = 0
    while l1 != None and l2 != None:
      newValue = l1.val + l2.val + carry
      carry = newValue / 10
      newValue = newValue % 10
      self.insertNode(newValue)
      l1 = l1.next
      l2 = l2.next

    while l1 != None:
      newValue = l1.val + carry
      carry = newValue / 10
      newValue = newValue % 10
      self.insertNode(newValue)
      l1 = l1.next

    while l2 != None:
      newValue = l2.val + carry
      carry = newValue / 10
      newValue = newValue % 10
      self.insertNode(newValue)
      l2 = l2.next

    if carry != 0:
      self.insertNode(carry)

    return self.resFirst
