# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from collections import deque


class Solution(object):

  def __init__(self):
    self._head = None

  def insertNode(self, data):
    newNode = ListNode(data)
    newNode.next = self._head
    self._head = newNode

  def addTwoNumbers(self, l1, l2):
    """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
    stack1 = deque()
    stack2 = deque()

    while l1 != None:
      stack1.append(l1.val)
      l1 = l1.next

    while l2 != None:
      stack2.append(l2.val)
      l2 = l2.next

    carry = 0
    while len(stack1) and len(stack2):
      try:
        currentVal = stack1.pop() + stack2.pop() + carry
        carry = currentVal / 10
        currentVal = currentVal % 10
        self.insertNode(currentVal)
      except IndexError:
        break

    while len(stack1):
      try:
        currentVal = stack1.pop() + carry
        carry = currentVal / 10
        currentVal = currentVal % 10
        self.insertNode(currentVal)
      except IndexError:
        break

    while len(stack2):
      try:
        currentVal = stack2.pop() + carry
        carry = currentVal / 10
        currentVal = currentVal % 10
        self.insertNode(currentVal)
      except IndexError:
        break

    if carry != 0:
      self.insertNode(carry)

    return self._head
