class Heap:
    def __init__(self, arr: list) -> None:
        self.heap = arr
        self.heap.insert(0, 0)
        self.numberOfElements = len(arr)
        self.heapSize = 0
        self.createHeap()

    def createHeap(self):
        while self.heapSize < self.numberOfElements - 1:
            self.heapSize += 1
            self.heapifyUp(self.heapSize)

    def heapifyUp(self, index):
        print("currentHeap: ", self.heap[1 : self.heapSize + 1])
        parentIndex = index // 2
        if parentIndex == 0:
            return

        currentItem = self.heap[index]
        parent = self.heap[parentIndex]
        if currentItem < parent:
            self.heap[index], self.heap[parentIndex] = (
                self.heap[parentIndex],
                self.heap[index],
            )
            self.heapifyUp(parentIndex)


h = Heap([3, 5, 6, 2, 1])
