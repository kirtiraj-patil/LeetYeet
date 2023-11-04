class BSearch:
  def __init__(self, arr, key) -> None:
    self.arr = arr
    self.key = key

  def bsearch(self, min, max):
    if min > max:
      return -1
    
    mid = (min + max) // 2
    # print(mid, self.arr[mid])
    if self.arr[mid] == self.key:
      return mid
    if self.arr[mid] < self.key:
      return self.bsearch(mid + 1, max)
    else:
      return self.bsearch(min, mid - 1)
    
l = [1,2,2,3,4,5,7,8,8,8,9]
b = BSearch(l, 8)

print(b.bsearch(0, len(l) - 1))