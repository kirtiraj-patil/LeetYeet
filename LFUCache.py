class UseLLNode:

  def __init__(self, key, value):
    self.key = key
    self.value = value
    self.use = 0
    self.prev = None
    self.next = None


class UseLL:

  def __init__(self, useLLNode):
    self._head = useLLNode
    self._tail = useLLNode

  def insertNode(self, newNode):
    self._tail.next = newNode
    newNode.prev = self._tail
    self._tail = newNode

  def removeNode(self, node):
    if node.next != None:
      node.next.prev = node.prev
    else:
      self._tail = node.prev

    if node.prev != None:
      node.prev.next = node.next
    else:
      self._head = node.next

    node.next = None
    node.prev = None

  def removeOldestNode(self):
    returnVal = self._head.key
    self._head = self._head.next
    if self._head != None:
      self._head.prev.next = None
      self._head.prev = None
    return returnVal


class LFUCache:

  def __init__(self, capacity: int):
    self.capacity = capacity
    self.cache = {}
    self.useLLs = {}
    self.minLL = 1
    # print('capacity', self.capacity)

  def removeLLIfEmpty(self, LLKey):
    if self.useLLs[LLKey]._head == None:
      self.useLLs.pop(LLKey, None)
      if LLKey == self.minLL:
        self.minLL = LLKey + 1

  def updateUse(self, key):
    node = self.cache[key]
    oldUse = node.use
    if oldUse != 0:
      self.useLLs[oldUse].removeNode(node)
      self.removeLLIfEmpty(oldUse)

    node.use = oldUse + 1
    if node.use < self.minLL:
      self.minLL = node.use
    try:
      self.useLLs[node.use].insertNode(node)
    except KeyError:
      self.useLLs[node.use] = UseLL(node)

  def insertNewNode(self, key, value):
    if len(self.cache) == self.capacity:
      removedKey = self.useLLs[self.minLL].removeOldestNode()
      self.removeLLIfEmpty(self.minLL)
      self.minLL = 1
      self.cache.pop(removedKey, None)

    newNode = UseLLNode(key, value)
    self.cache[key] = newNode
    self.updateUse(key)

  def printCache(self):
    for i in self.cache.keys():
      print('key: ', i)
      print('value: ', self.cache[i].value)
      print('use: ', self.cache[i].use)

  def get(self, key: int) -> int:
    returnVal = None
    try:
      returnVal = self.cache[key].value
      self.updateUse(key)
    except KeyError:
      returnVal = -1

    # self.printCache()
    # print('****** returing ', returnVal)

    return returnVal

  def put(self, key: int, value: int) -> None:
    if self.capacity == 0:
      return
    try:
      self.cache[key].value = value
      self.updateUse(key)
    except KeyError:
      self.insertNewNode(key, value)


# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
