class Node:

  def __init__(self, data):
    self.data = data
    self.frequency = 1
    self.next = None
    self.prev = None


class LL:

  def __init__(self, newNode):
    self._head = newNode
    self._tail = newNode

  def insertNode(self, newNode):
    if self._head == None:
      self._head = newNode
      self._tail = newNode
    else:
      self._tail.next = newNode
      newNode.prev = self._tail
      self._tail = newNode

  def removeNode(self, node):
    if node.prev == None:
      self._head = node.next
    else:
      node.prev.next = node.next

    if node.next == None:
      self._tail = node.prev
    else:
      node.next.prev = node.prev

    node.next = None
    node.prev = None


class Solution:

  def __init__(self):
    self.frequencyDict = {}
    self.dataDict = {}

  def updateDataLL(self, node, oldFrequency=0):
    try:
      if oldFrequency != 0:
        oldLL = self.frequencyDict[oldFrequency]
        oldLL.removeNode(node)
        # if oldLL._head == None:
        #     self.frequencyDict.pop(oldFrequency, None)

      newLL = self.frequencyDict[node.frequency]
      newLL.insertNode(node)

    except KeyError:
      self.frequencyDict[node.frequency] = LL(node)

  def updateFrequency(self, data):
    try:
      oldFrequency = self.dataDict[data].frequency
      self.dataDict[data].frequency = oldFrequency + 1
      self.updateDataLL(self.dataDict[data], oldFrequency)

    except KeyError:
      self.dataDict[data] = Node(data)
      self.updateDataLL(self.dataDict[data])

  def returnTopKFrequenctArray(self, k):
    res = []
    keys = list(self.frequencyDict.keys())
    # keys.sort()

    while len(res) < k:
      currentKey = keys.pop()
      currentLL = self.frequencyDict[currentKey]
      head = currentLL._head
      # print('printing LL: ', currentKey)
      while head != None:
        res.append(head.data)
        head = head.next

    return res

  # def printData(self):
  #     # print(self.dataDict)
  #     for i in self.dataDict:
  #         print(str(i) + ': ' + str(self.dataDict[i].frequency))

  def topKFrequent(self, nums: List[int], k: int) -> List[int]:
    for n in nums:
      self.updateFrequency(n)

    return self.returnTopKFrequenctArray(k)
