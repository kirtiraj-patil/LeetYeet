class Item:

  def __init__(self, data, index):
    self.data = data
    self.index = index


class Solution(object):

  def __init__(self):
    self.res = [0]

  def modifyNumsItems(self, nums):
    for idx, i in enumerate(nums):
      nums[idx] = Item(i, idx)

  def merge(self, leftList, rightList):
    mergedList = []
    lLen = len(leftList)
    rLen = len(rightList)
    i = 0
    j = 0

    carry = 0
    while i < lLen and j < rLen:
      if rightList[j].data < leftList[i].data:
        carry = carry + 1
        mergedList.append(rightList[j])
        j = j + 1
      else:
        self.res[leftList[i].index] = self.res[leftList[i].index] + carry
        mergedList.append(leftList[i])
        i = i + 1

    while i < lLen:
      self.res[leftList[i].index] = self.res[leftList[i].index] + carry
      mergedList.append(leftList[i])
      i = i + 1

    while j < rLen:
      mergedList.append(rightList[j])
      j = j + 1

    return mergedList

  def mergeSort(self, numList):
    l = len(numList)
    if l == 1:
      return numList

    midIndex = int(l / 2)
    leftList = self.mergeSort(numList[0:midIndex])
    rightList = self.mergeSort(numList[midIndex:l])
    return self.merge(leftList, rightList)

  def countSmaller(self, nums):
    """
        :type nums: List[int]
        :rtype: List[int]
        """
    self.res = self.res * len(nums)
    self.modifyNumsItems(nums)
    self.mergeSort(nums)
    return self.res
