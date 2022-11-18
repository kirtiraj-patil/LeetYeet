import math


class Solution:

  def __init__(self):
    self._min = math.inf

  def modBinarySearch(self, start, end):
    if start > end:
      return

    mid = int((start + end) / 2)
    if self._nums[mid] > self._nums[end]:
      if self._min > self._nums[end]:
        self._min = self._nums[end]
      self.modBinarySearch(mid + 1, end - 1)
    else:
      if self._min > self._nums[mid]:
        self._min = self._nums[mid]
      self.modBinarySearch(start, mid - 1)

  def findMin(self, nums: List[int]) -> int:
    self._nums = nums
    self.modBinarySearch(0, len(nums) - 1)
    return self._min
