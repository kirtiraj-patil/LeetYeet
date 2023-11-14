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

    def heapifyDown(self, index):
        if index > self.heapSize:
            return

        leftChildIndex = 2 * index + 1
        rightChildIndex = leftChildIndex + 1

        if leftChildIndex > self.heapSize:
            return
        if (
            rightChildIndex > self.heapSize
            and self.heap[leftChildIndex] < self.heap[index]
        ):
            self.heap[leftChildIndex], self.heap[index] = (
                self.heap[index],
                self.heap[leftChildIndex],
            )
            return

        indexToSwap = -1
        if self.heap[leftChildIndex] < self.heap[rightChildIndex]:
            indexToSwap = leftChildIndex
        else:
            indexToSwap = rightChildIndex

        if self.heap[index] < self.heap[indexToSwap]:
            self.heap[indexToSwap], self.heap[index] = (
                self.heap[index],
                self.heap[indexToSwap],
            )

    def pop_min(self):
        min = self.heap[1]
        self.heap[1], self.heap[self.heapSize] = self.heap[self.heapSize], self.heap[1]
        self.heapSize -= 1
        self.heapifyDown(1)
        return min


h = Heap([3, 5, 6, 2, 1])
