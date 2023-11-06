class Node:
  def __init__(self, val) -> None:
    self.key = val
    self.next = None

class LL:
  def __init__(self) -> None:
    self.head = None
    self.tail = None

  def insertNode(self, val):
    newNode = Node(val)
    if self.head == None:
      self.head = newNode
      self.tail = newNode
    else:
      self.tail.next = newNode
      self.tail = newNode

  def printMiddle(self):
    oneStepPointer = self.head
    twoStepPointer = self.head.next

    midVal = None

    while twoStepPointer != None:
      if twoStepPointer.next == None:
        midVal = oneStepPointer.key
        break
      elif twoStepPointer.next.next == None:
        midVal = oneStepPointer.next.key
        break
      twoStepPointer = twoStepPointer.next.next
      oneStepPointer = oneStepPointer.next

    print(midVal)

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

ll.printMiddle()