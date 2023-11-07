class Node:
  def __init__(self, key) -> None:
    self.key = key
    self.next = None

class LL:
  def __init__(self) -> None:
    self.head = None
    self.tail = None

  def insertNode(self, key):
    newNode = Node(key)
    if self.head == None:
      self.head = newNode
      self.tail = newNode
    else:
      self.tail.next = newNode
      self.tail = newNode

  def printLL(self):
    currentNode = self.head

    while currentNode != None:
      print(currentNode.key)
      currentNode = currentNode.next

  def reverseLL(self):
    if self.head == None or self.head.next == None:
      return
    
    self.tail = self.head
    
    pointer1 = None
    pointer2 = self.head
    pointer3 = self.head.next

    while pointer2 != None:
      pointer2.next = pointer1
      pointer1 = pointer2
      pointer2 = pointer3
      if pointer3 != None:
        pointer3 = pointer3.next

    self.head = pointer1

ll = LL()

ll.insertNode(1)
ll.insertNode(2)
ll.insertNode(3)
ll.insertNode(4)
ll.insertNode(5)
ll.insertNode(6)
ll.insertNode(7)
ll.insertNode(8)
ll.insertNode(9)

ll.printLL()
ll.reverseLL()
ll.printLL()