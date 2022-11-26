class Solution:
  
  def twoSum(self, numbers: List[int], target: int) -> List[int]:
    d = {}
    res = []
    for idx, i in enumerate(numbers):
      try:
        if d[target - i] != None:
          res.append(d[target - i] + 1)
          res.append(idx + 1)
          break
      except KeyError:
        d[i] = idx

    return res
