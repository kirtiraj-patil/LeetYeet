class Solution:

  def __init__(self):
    self.firstFound = False
    self.mode = 0
    self.left = -1
    self.right = -1

  def modBinarySearch(self, start, end):
    if start > end:
      return

    mid = int((start + end) / 2)
    if self.mode == -1:
      if self._nums[mid] == self._key:
        self.left = mid
        self.modBinarySearch(start, mid - 1)
      else:
        self.modBinarySearch(mid + 1, end)
    elif self.mode == 1:
      if self._nums[mid] == self._key:
        self.right = mid
        self.modBinarySearch(mid + 1, end)
      else:
        self.modBinarySearch(start, mid - 1)

  def binarySearch(self, start, end):
    if start > end:
      return

    mid = int((start + end) / 2)
    if self._nums[mid] == self._key:
      self.firstFound = True
      self.left = mid
      self.right = mid
      self.mode = -1
      self.modBinarySearch(start, mid - 1)
      self.mode = 1
      self.modBinarySearch(mid + 1, end)
    elif self._nums[mid] > self._key:
      self.binarySearch(start, mid - 1)
    else:
      self.binarySearch(mid + 1, end)

  def searchRange(self, nums: List[int], target: int) -> List[int]:
    self._nums = nums
    self._key = target

    self.binarySearch(0, len(nums) - 1)
    return [self.left, self.right]
