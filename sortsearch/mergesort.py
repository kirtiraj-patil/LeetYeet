class MSort:
  def mergeSort(self, arr):
    if len(arr) == 1:
      return arr

    mid = len(arr) // 2
    left = self.mergeSort(arr[:mid])
    right = self.mergeSort(arr[mid:])

    return self.merge(left, right)
  
  def merge(self, left, right):
    
    sortedArr = []
    i = 0
    j = 0

    while i < len(left) and j < len(right):
      if left[i] <= right[j]:
        sortedArr.append(left[i])
        i += 1
      else:
        sortedArr.append(right[j])
        j += 1

    while i < len(left):
      sortedArr.append(left[i])
      i += 1

    while j < len(right):
      sortedArr.append(right[j])
      j += 1

    return sortedArr
  
m = MSort()
print(m.mergeSort([9,1,32,6,34,90,100,43,0,-25]))