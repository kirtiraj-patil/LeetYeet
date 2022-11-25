class Solution:

  def findDuplicate(self, nums: List[int]) -> int:
    d = {}
    for i in nums:
      try:
        if d[i]:
          return i
      except KeyError:
        d[i] = True
