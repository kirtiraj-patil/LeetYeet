# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution(object):

  def __init__(self):
    self._res = None
    self._head = None

  def filterEmptyLists(self, lists):
    newList = []
    for i in xrange(0, len(lists)):
      if lists[i] != None:
        newList.append(lists[i])

    return newList

  def insertToRes(self, data):
    newNode = ListNode(data)
    if self._head == None:
      self._head = newNode
      self._res = newNode
    else:
      self._head.next = newNode
      self._head = newNode

  def swap(self, index1, index2):
    temp = self._heap[index1]
    self._heap[index1] = self._heap[index2]
    self._heap[index2] = temp

  def getParentIndex(self, i):
    if i == 0:
      return -1
    if i % 2 == 0:
      return int(i / 2) - 1
    return int(i / 2)

  def heapifyUp(self, index):
    parentIndex = self.getParentIndex(index)
    if parentIndex == -1:
      return

    if self._heap[parentIndex].val > self._heap[index].val:
      self.swap(parentIndex, index)
      self.heapifyUp(parentIndex)

  def heapifyDown(self, pI=0):
    lI = 2 * pI + 1
    rI = 2 * pI + 2

    if lI > self._heapEnd:
      return

    minI = lI
    minData = self._heap[lI].val

    if rI <= self._heapEnd and self._heap[rI].val < minData:
      minI = rI
      minData = self._heap[rI].val

    if minData < self._heap[pI].val:
      self.swap(minI, pI)
      self.heapifyDown(minI)

  def buildHeap(self):
    i = self._heapEnd + 1
    while i < self._dataLength:
      self._heapEnd = self._heapEnd + 1
      self.heapifyUp(self._heapEnd)
      i = i + 1

  def popMin(self):
    if self._heapEnd == -1:
      return None

    minData = self._heap[0].val
    if self._heap[0].next == None:
      self.swap(0, self._heapEnd)
      self._heapEnd = self._heapEnd - 1
    else:
      self._heap[0] = self._heap[0].next

    self.heapifyDown()
    return minData

  def printHeap(self):
    print([x.val for x in self._heap])

  def mergeKLists(self, lists):
    """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
    filteredLists = self.filterEmptyLists(lists)

    if len(filteredLists) == 0:
      return None

    self._dataLength = len(filteredLists)
    self._heapEnd = 0
    self._heap = filteredLists
    self.buildHeap()

    nextMin = self.popMin()
    while nextMin != None:
      self.insertToRes(nextMin)
      nextMin = self.popMin()
    return self._res
