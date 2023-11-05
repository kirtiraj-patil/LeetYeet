class QSort:
  def __init__(self, arr) -> None:
    self.arr = arr

  def swap(self, i, j):
    temp = self.arr[i]
    self.arr[i] = self.arr[j]
    self.arr[j] = temp

  def QSort(self, start, end):
    if start >= end:
      return
    
    self.partition(start, end)
    
  def partition(self, start, end):
    pivot = self.arr[end]

    i = start - 1
    j = start
    while j < end:
      if self.arr[j] < pivot:
        i += 1
        self.swap(i, j)
      
      j += 1

    i += 1
    self.swap(i, end)
    self.QSort(start, i - 1)
    self.QSort(i + 1, end)

  def printArr(self):
    print(self.arr)

arr = [9,8,3,90,76,1,0,6]
q = QSort(arr)
q.QSort(0, len(arr) - 1)
q.printArr()